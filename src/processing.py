from typing import Any


def filter_by_state(dictionary_list: list, state_value: Any = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    отбирая их по заданному значению ключа "state" (по-умолчанию: "EXECUTED")"""
    new_dictionary_list = []
    for dictionary in dictionary_list:
        if dictionary["state"] == state_value:
            new_dictionary_list.append(dictionary)
    return new_dictionary_list

