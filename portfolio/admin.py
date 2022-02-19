from django.contrib import admin
from .models import stock_port , crypto_port
# Register your models here.

class portfolio(admin.ModelAdmin) :

    list_display = ['__str__', 'user']
    search_fields = ['content','user__username' , 'user__email']

    class Meta :
        model = stock_port


admin.site.register(stock_port, portfolio)
# admin.site.register(stock_port)

admin.site.register(crypto_port)