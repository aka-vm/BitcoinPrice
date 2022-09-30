from bitcoin import get_price
from django.db.models import query

from .models import Bitcoin

def add_price():
    price = get_price()
    Bitcoin.objects.create(price=price)