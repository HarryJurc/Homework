from src.masks import get_mask_account, get_mask_card_number

try:
    user_card_number = int(input("Введите номер карты: "))
except ValueError:
    print("Ошибка: Номер карты должен состоять только из цифр!")
else:
    print(f"Номер карты: {get_mask_card_number(user_card_number)}")

try:
    user_account_number = int(input("Введите номер счета: "))
except ValueError:
    print("Ошибка: Номер счета должен состоять только из цифр!")
else:
    print(f"Номер счета: {get_mask_account(user_account_number)}")
