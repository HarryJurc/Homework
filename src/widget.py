from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_with_type: str) -> str:
    """Функция принимает номер карты или счета в формате "Visa Platinum 7000792289606361",
    или "Maestro 7000792289606361", или "Счет 73654108430135874305" и маскирует
    их в зависимости от типа"""
    acceptable_types = {
        "card": "Visa Classic , Visa Gold , Visa Platinum , Maestro , MasterCard ",
        "account": " Счет ",
    }
    only_number = ""
    only_type = ""
    for symbol in number_with_type:
        if symbol.isdigit():
            only_number += symbol
        else:
            only_type += symbol
    if only_type in acceptable_types["account"] and len(only_number) == 20:
        return f"{only_type + get_mask_account(int(only_number))}"
    elif only_type in acceptable_types["card"] and len(only_number) == 16:
        return f"{only_type + get_mask_card_number(int(only_number))}"
    else:
        return "Ошибка: Данные введены неверно!"


def get_date(date_input: str) -> str:
    """Функция принимает строку в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    return f'"{date_input[8:10]}.{date_input[5:7]}.{date_input[:4]}"'
