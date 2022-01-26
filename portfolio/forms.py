from django import forms
from django.forms import ModelForm
from .models import stock_port

class stock_port_form(ModelForm) :
    name = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))
    price = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))
    quantity = forms.CharField(label='',widget=forms.TextInput(attrs={"placholder":"write here"}))

    class Meta:
        model = stock_port
        fields = '__all__'

