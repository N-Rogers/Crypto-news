from django.shortcuts import render
from django.http import request
import requests
import json

# Create your views here.

def home(request):
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'Crypto_news_app/home.html',{'api': api})

def cryptoprice(request):
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,EOS,TRX,LTC,ZEC,BCH&tsyms=USD')
    price_api = json.loads(price_request.content)
    return render(request, 'Crypto_news_app/cryptoprice.html', {'price_api': price_api})
    