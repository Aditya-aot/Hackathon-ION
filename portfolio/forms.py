from django import forms
from django.forms import ModelForm
from .models import stock_port , crypto_port

class stock_port_form(ModelForm) :
    name = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))
    price = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))
    quantity = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))

    class Meta:
        model = stock_port
        fields = [
            'name' ,
            'price',
             'quantity'
        ]


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url  = 'https://coinmarketcap.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

name_list=[]
names = soup.find_all("div", {"class": "sc-16r8icm-0 sc-1teo54s-1 dNOTPP"})

for name in names :
#     print(name.text)

    name_list.append((name.text , name.text))
name_list= (name_list[9:19])    

tables = soup.find_all("div", {"class": "sc-131di3y-0 cLgOOr"})


class crypto_port_form(ModelForm) :
    name =  forms.CharField(label='Select Crypto ', widget=( forms.Select(choices=name_list )   ) )  
    price = forms.CharField(label='Price',widget=forms.TextInput(attrs={"placholder":"write here"}))
    quantity = forms.CharField(label='Quantity',widget=forms.TextInput(attrs={"placholder":"write here"}))

    class Meta:
        model = crypto_port
        fields = [
            'name' ,
            'price',
             'quantity'
        ]
