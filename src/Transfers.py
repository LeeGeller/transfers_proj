import json


class Transfer:
    def __init__(self):
        self.list_transfer = []

    def __repr__(self):
        return (f"Return file with informstion\n"
                f"about users transfers:\n"
                f"{self.list_transfer}\n")

    def get_transfers_list(self, data_path):
        """
        Get list with transfers from data file
        :param data_path: path to data file
        :return: list with user transfers
        """
        with open(data_path, 'r', encoding='UTF-8') as data_file:
            self.list_transfer = json.load(data_file)
        return self.list_transfer
