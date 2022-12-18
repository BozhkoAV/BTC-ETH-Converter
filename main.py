import re
import requests


def main():
    currency = currency_check(input("Введите конвертируемую валюту (BTC|ETH): "))
    amount = amount_check(input("Введите количество конвертируемой валюты: "))
    result = exchange(amount, currency)
    if currency == "BTC":
        print(str(float(result)) + " ETH")
    else:
        print(str(float(result)) + " BTC")


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


def exchange(amount, currency):
    rate = get_exchange_rate(currency)
    return round(amount * rate, 6)


def get_exchange_rate(currency):
    try:
        if currency == "BTC":
            response = requests.get('https://www.coingecko.com/en/coins/bitcoin/eth')
            info = re.findall(r"1 BTC = ETH\d+\.\d+", response.text)
        else:
            response = requests.get('https://www.coingecko.com/en/coins/ethereum/btc')
            info = re.findall(r"1 ETH = BTC\d+\.\d+", response.text)
        return float(re.findall(r"\d+\.\d+", info[0])[0])
    except Exception:
        raise Exception("Проблемы с доступом к сайту")


if __name__ == '__main__':
    main()
