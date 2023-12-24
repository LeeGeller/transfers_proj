from config import DATA_TEST, DATA_TEST_LIST
from src.Transfers import Transfer


def test_get_transfers_list():
    assert Transfer().get_transfers_list(DATA_TEST) == [1, 2, 3]


def test_clean_transfers_list():
    transfers = Transfer()
    transfers.get_transfers_list(DATA_TEST)
    assert Transfer().clean_transfers_list([{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
        {'state': 'EXECUTED'}]
    assert Transfer().clean_transfers_list([{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
        {'state': 'EXECUTED'}]
    assert len(transfers.list_transfer) == 3
