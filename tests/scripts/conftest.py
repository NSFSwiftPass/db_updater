import uuid

from pytest import fixture
from sqlalchemy import event

from db_updater.database.connection import Session, engine
from db_updater.scripts.daily_sync import DailySync


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
def daily_sync(external_transaction_session) -> DailySync:
    daily_sync = DailySync()
    daily_sync.SCRIPT_NAME = f'{daily_sync.SCRIPT_NAME}-{uuid.uuid4().hex}'
    daily_sync.session = external_transaction_session

    yield daily_sync


@fixture
def external_transaction_session() -> Session:
    external_transaction_suite = ExternalTransactionSuite()

    try:
        yield external_transaction_suite.session
    finally:
        external_transaction_suite.tear_down()
