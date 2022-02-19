from django import forms
from django.forms import ModelForm
from .models import Full_chat , Comment


class ChatForm(ModelForm):
    content =  forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your topic "}))
    message  =   forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your Message"}))
    # images = forms.ImageField()
    # null = True, blank = True

    class Meta:
        model = Full_chat
        fields = [
            'content' ,
            'message' ,
            # 'images' ,
 ]


class CommentForm(ModelForm):
    comment =  forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your comment "}))
    class Meta:
        model = Comment
        fields = [
            'comment' ,]

class RawCustomerForm(forms.Form):
    todo      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your first name"}))
    last_date = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your last name"}))

