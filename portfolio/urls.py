from django.urls import path
from . import views
# from portfolio.views import portfolio_views


urlpatterns = [
    path('/view', views.stock_or_bit , name='stock_or_bit') ,
    path('', views.portfolio_views , name='portfolio_views') ,
    path('/edit', views.portfolio_edit_views , name='portfolio_edit_views') ,
    path('/deletestock/<int:stock_id>', views.delete_portfolio_edit_views,name='delete_portfolio_edit_views'),
    path('/update_portfolio/<str:pk>', views.update_portfolio , name='update_portfolio') ,

    path('/crypto/edit', views.edit_crypto_portfolio_views , name='edit_crypto_portfolio_views') ,
    path('/crypto/deletestock/<int:crypto_id>', views.delete_crypto_portfolio_edit_views , name='delete_crypto_portfolio_edit_views') ,
    path('/crypto/portfolio', views.crypto_portfolio_views , name='crypto_portfolio_views') ,
]