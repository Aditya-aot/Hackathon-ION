from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect
from .models import Full_chat , Comment
from .forms import ChatForm , CommentForm
from django.contrib.auth.models import  User, auth
from django.urls import reverse
from django.views import generic



from django import forms

# print(request.user.username)

def chat_view(request) :
    a=(request.user.username)
    form = ChatForm()
    chat = Full_chat.objects.all()

    liked = False
    if Full_chat.objects.filter(likes=request.user.id).exists() :
        liked = True
    else:
        liked = False


    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user or None
            obj.save()


    context = { 'form' : form ,
                 'all_chat' : chat[::-1] ,
                'a':a ,
                'liked' : liked ,
                }

    return render(request, 'chat/chat.html', context)



def user_post(request) :
    chat = Full_chat.objects.all()
    username = request.GET.get('username')
    # if username != None :
    user_chat = chat.filter(user__username__iexact = username)
    context = {'user_chat':user_chat}

    return render(request, 'chat/user_post.html' ,context)

def other_user_post(request , pk) :
    chat = Full_chat.objects.all()
    pk=pk
    user = chat.filter(user__username__iexact = pk)
    context = {'user_chat': user[::-1] ,
               'chat' : chat ,
               'pk':pk}
    return render(request, 'chat/following_post.html' ,context)


# @permission_classes([IsAuthenticated])

def search(requrst) :
    chat = Full_chat.objects.all()
    # set_user = []
    # for users in set_user :
    #     user = chat.filter(request.user.id)

def follow(request, pk) :
    chat = Full_chat.objects.all()
    chat = Full_chat.objects.get(id=pk)
    pk = pk
    user = chat.filter(user__username__iexact=pk)
    # chat = Full_chat.objects.get(id= pk)
    liked = False
    if chat.follow.filter(pk=request.user.username).exists():
        chat.follow.remove(request.user)
        liked = False

    else :
        chat.follow.add(request.user)
        liked = True

    return HttpResponseRedirect('/chat/')

def like_chat(request, pk) :
    chat = Full_chat.objects.get(id= pk)
    liked = False
    if chat.likes.filter(id=request.user.id).exists() :
        chat.likes.remove(request.user)
        liked = False

    else :
        chat.likes.add(request.user)
        liked = True

    return HttpResponseRedirect('/chat/')

# def total_likes(request , pk ) :
#     chat = Full_chat.objects.get(id=pk)
#     total = chat.total_likes()
#     liked = False
#     if chat.likes.filter(id=request.user.id).exists():
#         liked = True
#     else :
#         liked =False
#
#     context = {'total_likes': total ,
#                'liked': liked ,
#                }
#     return render(request, 'chat/chat.html', context)




def comment_view(request, pk) :
    form = CommentForm()
    chat_comment = Full_chat.objects.get(id= pk)
    total = chat_comment.total_likes()
    comment = chat_comment.comments.all()

    form.instance.user = request.user

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.chat = Full_chat.objects.get(id= pk) or None
        obj.save()

    context = {'chat_comment': chat_comment ,
               'comment': comment[::-1] ,
               'total_likes': total ,
               'form':form ,
               }

    return render(request, 'accounts/front_page.html' ,context)





def delete_chat(request, chat_id) :
    chat_to_delete = Full_chat.objects.get(id= chat_id)
    chat_to_delete.delete()
    return HttpResponseRedirect('/chat/')



def update_chat(request , pk) :
    all_chat = Full_chat.objects.get(id=pk)
    form = ChatForm(instance= all_chat)

    context = {'form' : form}

    if request.method == 'POST' :
        form = ChatForm(request.POST, instance=all_chat)
        if form.is_valid():
            form.save()
            return redirect('/chat/')

    return render(request, 'chat/update.html', context)



