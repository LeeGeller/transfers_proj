from Transfers import Transfer
from config import DATA


def main():
    transfers = Transfer()
    transfers.get_transfers_list(DATA)
    transfers.clean_transfers_list(transfers.list_transfer)
    transfers.sort_list(transfers.list_transfer)
    print(transfers.get_last_info())




if __name__ == "__main__":
    main()
