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


def test_sort_list():
    assert Transfer().sort_list([{'date': '2018-01-21T01:10:28.317704'}, {'date': '2018-12-18T17:07:09.800800'},
                                 {'date': '2019-12-08T22:46:21.935582'}]) == [{'date': '2019-12-08T22:46:21.935582'},
                                                                              {'date': '2018-12-18T17:07:09.800800'},
                                                                              {'date': '2018-01-21T01:10:28.317704'}]


def test_print_first_line():
    assert Transfer().print_first_line("2019-12-08T22:46:21.935582", "Открытие вклада") == "08.12.2019 Открытие вклада"
