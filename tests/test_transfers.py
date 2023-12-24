from config import DATA_TEST, DATA_TEST_LIST
from src.Transfers import Transfer


def test_get_transfers_list():
    assert Transfer().get_transfers_list(DATA_TEST) == [1, 2, 3]