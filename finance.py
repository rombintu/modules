from pycbrf.toolbox import ExchangeRates
from datetime import datetime

def convert_rub(summa=0):
    today = datetime.today().strftime("%Y-%m-%d")
    rates = ExchangeRates(today)

    # print("USD: ", round(rates['USD'].value, 2))
    # print("EUR: ", round(rates['EUR'].value, 2))

    usd = rates['USD'].value
    eur = rates['EUR'].value

    return usd, eur, [summa*usd, summa*eur]