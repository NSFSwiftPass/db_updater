import uuid

from pytest import fixture

from db_updater.scripts.daily_sync import DailySync
from tests.confest import external_transaction_session


@fixture
def daily_sync(external_transaction_session) -> DailySync:
    daily_sync = DailySync()
    daily_sync.SCRIPT_NAME = f'{daily_sync.SCRIPT_NAME}-{uuid.uuid4().hex}'
    daily_sync.session = external_transaction_session

    yield daily_sync
