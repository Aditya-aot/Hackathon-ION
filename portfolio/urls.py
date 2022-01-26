from django.urls import path
from . import views
# from portfolio.views import portfolio_views


urlpatterns = [
    path('', views.portfolio_views , name='portfolio_views') ,
    path('/edit', views.portfolio_edit_views , name='portfolio_edit_views') ,
    path('/deletestock/<int:stock_id>', views.delete_portfolio_edit_views,name='delete_portfolio_edit_views')


]