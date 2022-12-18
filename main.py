import re


def main():
    currency_check(input("Введите конвертируемую валюту (BTC|ETH): "))
    amount_check(input("Введите количество конвертируемой валюты: "))


def currency_check(currency):
    while not(re.fullmatch(r"^b|btc|e|eth$", currency.lower())):
        print("Неверный формат ввода валюты\n"
              "Допустимые варианты ввода: b|B|btc|BTC|e|E|eth|ETH\n")
        currency = input("Введите конвертируемую валюту (BTC|ETH): ")
    if re.fullmatch(r"^b|btc$", currency.lower()):
        return "BTC"
    if re.fullmatch(r"^e|eth$", currency.lower()):
        return "ETH"


def amount_check(amount):
    while not(re.fullmatch(r"^\d+(\.\d+)?", amount)):
        print("Неверный формат ввода числа\n"
              "Допустимые варианты ввода: число | целая часть цисла.дробная часть числа\n"
              "Примеры: 123 | 100.12\n")
        amount = input("Введите количество конвертируемой валюты: ")
    return float(amount)


if __name__ == '__main__':
    main()
