from typing import Any


def filter_by_state(dictionary_list: list[dict], state_value: Any = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    отбирая их по заданному значению ключа "state" (по-умолчанию: "EXECUTED")"""

    new_dictionary_list = []
    for dictionary in dictionary_list:
        if dictionary["state"] == state_value:
            new_dictionary_list.append(dictionary)
    return new_dictionary_list


def sort_by_date(dictionary_list: list[dict], is_reverse: bool = True) -> list:
    """Функция принимает список словарей и сортирует их по датам (по-умолчанию: по убыванию)"""

    return sorted(dictionary_list, key=lambda x: x["date"], reverse=is_reverse)
