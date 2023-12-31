import json
from datetime import datetime as date


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

    def clean_transfers_list(self, transfers_list):
        """
        Clean None dict, info with CANCELED state and other artifacts
        :param transfers_list: user's transfer list
        :return: clean self.list_transfer
        """
        new_list = []
        for info in transfers_list:
            if info.get('state') == 'EXECUTED':
                new_list.append(info)
        self.list_transfer = new_list
        return self.list_transfer

    def sort_list(self, clean_transfers_list):
        """
        Sort transfers list
        :param clean_transfers_list: clean transfers list
        :return: self.list_transfer fith 5 sort last transfers
        """
        sorted(clean_transfers_list, key=lambda dictionary: dictionary['date'], reverse=True)
        self.list_transfer = sorted(clean_transfers_list, key=lambda dictionary: dictionary['date'], reverse=True)
        self.list_transfer = self.list_transfer[:5]
        return self.list_transfer

    def print_first_line(self, date_info, description):
        """
        Get formatted date and description
        :param date_info: info about date
        :param description: description
        :return: formatted date and description
        """
        date_class = date.fromisoformat(date_info)
        date_formatted = date_class.strftime("%d.%m.%Y")
        return f"{date_formatted} {description}"

    def hide_card_info(self, card_info):
        """
        Get hide info about card's number
        :param card_info: name and number card
        :return: name card and hide number
        """
        list_card_info = card_info.split()
        new_list = []
        for info in list_card_info:
            if 'счет' in card_info.lower() and info.isdigit():
                new_list.append(f'**{info[-4:]}')
            elif 'счет' not in card_info.lower() and info.isdigit():
                new_list.append(f'{info[:4]} {info[4:6]}** **** {info[-4:]}')
            else:
                new_list.append(info)
        return ' '.join(new_list)

    def get_last_info(self):
        """
        Get 5 formatted info about transfers
        :return: text for user
        """
        list_transfers = self.list_transfer
        new_list = []
        for info in list_transfers:
            new_list.append(f"\n{self.print_first_line(info['date'], info['description'])}\n")
            if info.get('from') is None:
                info['from'] = "операция со счетом"

            info_from = self.hide_card_info(info.get('from'))
            info_to = self.hide_card_info(info.get('to'))
            new_list.append(f"{info_from} -> {info_to}\n")
            new_list.append(f"{info['operationAmount']['amount']} {info['operationAmount']['currency']['name']}\n")
        return ''.join(new_list)
