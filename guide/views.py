from django.shortcuts import render

# Create your views here.


def guide_list_view(request) :
    context = { }
    return render(request, 'guide/guide_list.html',context) 


def finance_guide(request) :
    context = { }
    return render(request, 'guide/finance.html',context) 


def stock(request) :
    context = { }
    return render(request, 'guide/stock.html',context) 


def crypto(request) :
    context = { }
    return render(request, 'guide/crypto.html',context) 


def real_estate(request) :
    context = { }
    return render(request, 'guide/real_estate.html',context) 
