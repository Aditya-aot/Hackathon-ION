from django.contrib import admin
from .models import Full_chat , Comment

# Register your models here.

# admin.site.register(Full_chat )
# class Like_Admin(admin.TabularInline) :
#     model = Chat_Like

class TweetAdmin(admin.ModelAdmin) :
    # inlines = [Like_Admin]
    list_display = ['__str__', 'user']
    search_fields = ['content','user__username' , 'user__email']
    class Meta :
        model = Full_chat

admin.site.register(Full_chat , TweetAdmin)

admin.site.register(Comment)
