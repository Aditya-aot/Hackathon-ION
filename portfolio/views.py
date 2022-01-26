from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import stock_port
from .forms import stock_port_form

import yfinance as yf
# Create your views here.


def portfolio_views(request) :
    stock_dict={}
    # what we get from user 
    name_list=[]
    price_list=[]
    quantity_list=[]
    #what we have to show to the user 
    current_price=[]
    total_spent = []
    total_current_price=[]
    # p_or_l = []


    model_stock = stock_port.objects.all()

    for i in model_stock :
        name_list.append(i.name)
        price_list.append(i.price)
        quantity_list.append(i.quantity)

    a=0
    for ticker in name_list:
        name_stock=name_list[a]
        price=price_list[a]
        quantity=quantity_list[a] 

        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history(period="1d")
        current_price = (data.tail(1)['Close'].iloc[0])
        # print(last_quote)
        # current_price.append(last_quote)

    # for j in current_price: 
        t_current_price = current_price * int(quantity)
        t_spent         = int(price) * int(quantity)
        p_or_l = t_current_price-t_spent
        

        a=a+1
        stock_dict[a] =[name_stock,price,quantity,current_price,t_current_price,t_spent,p_or_l]
        # total_current_price.append(t_current_price)
        
    # stock_dict=list(reversed(sorted(stock_dict.items() )))
    print(total_current_price)
    context = {'all' : model_stock[::-1] ,
                "stock_dict":stock_dict ,
                #  "stock_dict":
                }

    return render(request, 'portfolio/stock.html', context)


def portfolio_edit_views(request) :
    form = stock_port_form()
    model_stock = stock_port.objects.all()

    if request.method == 'POST':
        form = stock_port_form(request.POST) 
        if form.is_valid() :
            form.save()

    context = {'form': form ,
                'all' : model_stock[::-1] ,
                }

    return render(request, 'portfolio/stock_edit.html', context)


def delete_portfolio_edit_views(request,stock_id) :
    item_to_delete = stock_port.objects.get(id=stock_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/portfolio/edit')

