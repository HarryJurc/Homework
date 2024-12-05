def get_mask_card_number(user_card_number: int) -> str:
    """Функция принимает номер карты пользователя
    и возвращает его в формате ХХХХ ХХ** **** ХХХХ,
    где Х - это цифра номера. Если количество цифр
    отличается от 16, то возвращается ошибка"""
    if len(str(user_card_number)) == 16 and user_card_number == int(user_card_number):
        return f"{str(user_card_number)[:4]} {str(user_card_number)[4:6]}** **** {str(user_card_number)[-4:]}"
    else:
        return f"Ошибка: Номер карты должен состоять из 16 цифр! Вы ввели {len(str(user_card_number))} цифр"


def get_mask_account(user_account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает
    его маску. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера."""
    if len(str(user_account_number)) == 20:
        return str(user_account_number).replace(str(user_account_number)[:-4], "**")
    else:
        return f"Ошибка: Номер счета должен состоять из 20 цифр! Вы ввели {len(str(user_account_number))} цифр"
