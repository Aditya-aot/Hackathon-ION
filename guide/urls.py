from django.urls import path
from . import views



urlpatterns = [
    path('', views.guide_list_view , name='guide_list_view') ,
    path('/finance_guide', views.finance_guide , name='finance_guide') ,
    path('/stock_guide', views.stock , name='stock') ,
    path('/crypto_guide', views.crypto , name='crypto') ,
    path('/real_estate_guide', views.real_estate , name='real_estate') ,

]

