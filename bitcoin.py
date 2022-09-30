from requests import get
from api.models import Bitcoin

def get_price():
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=INR'
    response = get(url)
    data = response.json()
    inr_price = data['INR']
    return inr_price

def add_price():
    price = get_price()
    Bitcoin.objects.create(price=price)


if __name__ == '__main__':
    print(get_price())