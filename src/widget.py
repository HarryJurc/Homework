from .masks import get_mask_account, get_mask_card_number


def mask_account_card(number_with_type: str) -> str:
    acceptable_types = {"card": " Visa Platinum , Maestro ", "account": " Счет "}
    only_number = ""
    only_type = ""
    for symbol in number_with_type:
        if symbol.isdigit():
            only_number += symbol
        else:
            only_type += symbol
    if only_type in acceptable_types["account"] and len(only_number) == 20:
        return only_type + get_mask_account(int(only_number))
    elif only_type in acceptable_types["card"] and len(only_number) == 16:
        return only_type + get_mask_card_number(int(only_number))
    else:
        return "Ошибка: Данные введены неверно!"


def get_date(date_input: str) -> str:
    return f'"{date_input[8:10]}.{date_input[5:7]}.{date_input[:4]}"'
