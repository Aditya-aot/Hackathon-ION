from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import  User
# urlpatterns = [
#     path('', views.home, name='home'),
#     # path('print', views.print, name='print'),
# ]
urlpatterns = [
    path('', views.chat_view , name='chat_view') ,
    path('chat', views.chat_view , name='chat_view') ,
    path("deleteChat/<int:chat_id>", views.delete_chat, name='delete_chat'),
    path("like_chat/<int:pk>", views.like_chat, name='like_chat'),
    path("chat/<int:pk>", views.comment_view, name='comment_view'),
    path("user/<str:pk>", views.other_user_post, name='other_user_post'),
    path("follow/<str:pk>", views.follow, name='follow'),
    path('update_chat/<str:pk>', views.update_chat, name='update_chat'),
    path('user_post', views.user_post , name='user_post') ,
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

