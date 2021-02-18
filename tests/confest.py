from pytest import fixture
from sqlalchemy import event

from db_updater.database.connection import Session, engine


class ExternalTransactionSuite:
    """
    As seen from https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
    """

    def __init__(self):
        self.connection = engine.connect()
        self.transaction = self.connection.begin()
        self.session = Session(bind=self.connection)

        self.nested = self.connection.begin_nested()

        @event.listens_for(self.session, "after_transaction_end")
        def end_savepoint(session, transaction):
            if not self.nested.is_active:
                self.nested = self.connection.begin_nested()

    def tear_down(self):
        self.session.close()
        self.transaction.rollback()
        self.connection.close()


@fixture
def external_transaction_session() -> Session:
    external_transaction_suite = ExternalTransactionSuite()

    try:
        yield external_transaction_suite.session
    finally:
        external_transaction_suite.tear_down()
