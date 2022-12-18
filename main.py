import re


def main():
    currency_check(input("Введите конвертируемую валюту (BTC|ETH): "))


def currency_check(currency):
    while not(re.fullmatch(r"^b|btc|e|eth$", currency.lower())):
        print("Неверный формат ввода валюты\n"
              "Допустимые варианты ввода: b|B|btc|BTC|e|E|eth|ETH\n")
        currency = input("Введите конвертируемую валюту (BTC|ETH): ")
    if re.fullmatch(r"^b|btc$", currency.lower()):
        return "BTC"
    if re.fullmatch(r"^e|eth$", currency.lower()):
        return "ETH"


if __name__ == '__main__':
    main()
