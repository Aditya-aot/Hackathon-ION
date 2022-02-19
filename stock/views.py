from django.shortcuts import render
from datetime import timedelta, date


from .forms import search_from ,search_day


# Create your views here.
import yfinance as yf
from datetime import timedelta, date

from json import dumps

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# news
from bs4 import BeautifulSoup
import pandas as pd
import requests





def test(request) :
    context = {}
    return render(request, 'stock/base2.html',context)

def discuess(request) :
    context = {}
    return render(request, 'discuss/discuss.html',context)

def about(request) :
    context = {}
    return render(request, 'stock/about.html',context)


def welcome(request) :
    today = date.today()
    d = today.strftime("%d-%b-%Y")

    context = {"day":d}
 
    return render(request, 'stock/welcome.html',context)


def home(request) :
    symbol=''
    year=''
    month=''
    day=''
    a=0
    list=[]
    label = ['Open','High','Low','Close','Volume','Dividends','Stock Splits']
    full_list = {}

    form = search_from()
    if request.method =='POST' :
        form = search_from(request.POST, request.FILES)
        if form.is_valid() :
            symbol = form.cleaned_data['symbol']
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']


    #  .
        # TATAPOWER.NS
        msft = yf.Ticker(symbol)
        hist = msft.history(period="500d")
        new_df = hist.copy()
        new_df['year'], new_df['month'], new_df['day'] = hist.index.year, hist.index.month, hist.index.day

        new_df.reset_index(inplace=True,drop=False)
        new_df= new_df.drop(['Date'],axis='columns')

            
        scaled_close= new_df.drop(['Open','High','Low','Close','Volume','Dividends','Stock Splits'],axis='columns')
        scaled_open = new_df[['Close','High','Low','Open','Volume','Dividends','Stock Splits']]

        inputs= scaled_close
        target = scaled_open

                
        x_train, x_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
                
        model = RandomForestRegressor()
        model.fit(x_train, y_train)

        score=model.score(x_test, y_test)
        a=model.predict([[year,month,day]])

        for each in a :
            for e in each :
                list.append(e)

        
        for key in label :
            for value in list :
                full_list[key] = value
                # list.remove(value)
        mylist = zip(label,list)

        label1=dumps(label)
        list1=dumps(list)

        print(full_list)
        context = { 'form':form ,
                                'score':score ,
                                'list' : list1 ,
                                'a' : a ,
                                'label':label1 ,
                                'full_list' : full_list,
                                'mylist' :mylist
                                
                            }        
        return render(request, 'stock/home.html', context)   
    else :
        context={'form':form}
        return render(request, 'stock/home.html',context) 




def chart(request) :
    symbol=''
    day=''
    close=[]
    high=[]
    low=[]
    openn=[]
    # label = ['Open','High','Low','Close']
    label = []
    full_list = {}

    form = search_day()
    if request.method =='POST' :
        form = search_day(request.POST, request.FILES)
        if form.is_valid() :
            symbol = form.cleaned_data['symbol']
            days = form.cleaned_data['days']


    #  .
        # TATAPOWER.NS
        msft = yf.Ticker(symbol)
        hist = msft.history(period="500d")
        new_df = hist.copy()
        new_df['year'], new_df['month'], new_df['day'] = hist.index.year, hist.index.month, hist.index.day

        new_df.reset_index(inplace=True,drop=False)
        new_df= new_df.drop(['Date'],axis='columns')

            
        scaled_close= new_df.drop(['Open','High','Low','Close','Volume','Dividends','Stock Splits'],axis='columns')
        scaled_open = new_df[['Close','High','Low','Open','Volume','Dividends','Stock Splits']]

        inputs= scaled_close
        target = scaled_open

                
        x_train, x_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
                
        model = RandomForestRegressor()
        model.fit(x_train, y_train)

        score=model.score(x_test, y_test)

        date_req = date.today() + timedelta(days=50)

        year = date_req.strftime("%Y")
        month = date_req.strftime("%m")
        day = date_req.strftime("%d")

        lab=[]
        for i in range(int(days)) :
            date_req = date.today() + timedelta(days=i)
            all_date=(date.today() + timedelta(i))
            lab.append(str(all_date))

            label.append(i)
            year = date_req.strftime("%Y")
            month = date_req.strftime("%m")
            day = date_req.strftime("%d")
            
            a=model.predict([[year,month,day]])
            for l in a :
                close.append(l[0])
                high.append(l[1])
                low.append(l[2])
                openn.append(l[3])
    
        lab=dumps(lab)
        label1=dumps(label)
        close1=dumps(close)
        high1=dumps(high)
        low1=dumps(low)
        open1=dumps(openn)

        print(full_list)
        context = { 'form':form ,
                                'lab' : lab ,
                                'score':score ,
                                'label':label1 ,
                                'close':close1,
                                'high':high1 ,
                                'low': low1 ,
                                'open':open1 ,
                                
                            }        
        return render(request, 'stock/chart.html', context)   
    else :
        context={'form':form}
        return render(request, 'stock/chart.html',context) 



def news(request) :
    url='https://finance.yahoo.com/news'
    page = requests.get(url)

    page.text
    soup = BeautifulSoup(page.text,'html.parser')
    yahoo_news = soup.find_all("div", {"class": "Ov(h) Pend(44px) Pstart(25px)"})
    y_news = {}
    n=0 
    for news in yahoo_news :
        url='https://finance.yahoo.com/news'
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        heading = news.find('a', {'class':'js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'}).text
        link = news.find('a',{'class':'js-content-viewer wafer-caas Fw(b) Fz(18px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled'}).get('href')
        link =('https://finance.yahoo.com/'+link)
        summary = news.find('p',{'class':'Fz(14px) Lh(19px) Fz(13px)--sm1024 Lh(17px)--sm1024 LineClamp(2,38px) LineClamp(2,34px)--sm1024 M(0)'})
        if summary :
            summary=summary.text 
        else :
            summary="nope"


        n=1+n
        y_news[n] = [heading,link,summary]
        
    context={'y_news':y_news}
    return render(request, 'stock/news.html',context) 

def predict_view(request) :
    context = { }
    return render(request, 'stock/predict.html',context) 
