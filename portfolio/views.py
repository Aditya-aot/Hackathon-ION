from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import stock_port , crypto_port
from .forms import stock_port_form  , crypto_port_form
from django.contrib.auth.models import  User, auth

import yfinance as yf
# Create your views here.

def stock_or_bit(request) :
    context = {
                }

    return render(request, 'portfolio/stock_or_bit.html', context)



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
    username = request.user
    # user_chat = model_stock.filter(user__username__iexact = username)
    user_chat = model_stock.filter(user = username)


    for i in user_chat :
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
    context = {'all' : user_chat[::-1] ,
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
            # form.save()
            obj = form.save(commit=False)
            obj.user = request.user or None
            obj.save()
    
    # username = request.GET.get('username')
    username = request.user
    # user_chat = model_stock.filter(user__username__iexact = username)
    user_chat = model_stock.filter(user = username)
    context = {'form': form ,
                'all' : user_chat[::-1] ,
                }

    return render(request, 'portfolio/stock_edit.html', context)


def delete_portfolio_edit_views(request,stock_id) :
    item_to_delete = stock_port.objects.get(id=stock_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/portfolio/edit')


def update_portfolio(request, pk) :
    model_stock = stock_port.objects.get(id=pk)
    from_stock =  stock_port_form(instance=model_stock)

    if request.method =='POST' :
        form_stock = stock_port_form(request.POST, instance=model_stock)
        if form_stock.is_valid() :
            form_stock.save()
            return redirect('/portfolio/edit')

    context = {'form':form_stock}
    return render(request, 'portfolio/update_stock.html',context)        

# <-------------- Crypto Portfolio code here ------------->
# <-------------- Crypto Portfolio code here ------------->
# <-------------- Crypto Portfolio code here ------------->
# <-------------- Crypto Portfolio code here ------------->
def crypto_portfolio_views(request) :

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


    model_stock = crypto_port.objects.all()

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

    return render(request, 'portfolio/crypto_portfolio.html', context)

def edit_crypto_portfolio_views(request) :
    form = crypto_port_form()
    model_crypto = crypto_port.objects.all()

    if request.method == 'POST' :
        form = crypto_port_form(request.POST)
        if form.is_valid() :
            # form.save()
            obj = form.save(commit=False)
            obj.user = request.user or None
            obj.save()

    username = request.user
    # user_chat = model_crypto.filter(user__username__iexact = username)
    user_chat = model_crypto.filter(user = username)
    

    context = {'form':form ,
                'all' : user_chat[::-1]
                }

    return render(request, 'portfolio/crypto_edit.html', context)


def delete_crypto_portfolio_edit_views(request,crypto_id) :
    item_to_delete = crypto_port.objects.get(id=crypto_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/portfolio/crypto/edit')


# def update_portfolio(request, pk) :
#     model_stock = stock_port.objects.get(id=pk)
#     from_stock =  stock_port_form(instance=model_stock)

#     if request.method =='POST' :
#         form_stock = stock_port_form(request.POST, instance=model_stock)
#         if form_stock.is_valid() :
#             form_stock.save()
#             return redirect('/portfolio/edit')

#     context = {'form':form_stock}
#     return render(request, 'portfolio/update_stock.html',context)        
