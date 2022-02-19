from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth


# class Chat_Like(models.Model) :
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tweet = models.ForeignKey("Full_Chat" , on_delete=models.CASCADE)
#     pub_date = models.DateTimeField( auto_now_add=True, null=True)

class Full_chat(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL , default=1 , on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
    # user = models.OneToOneField(User , null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="tweet_user" , blank=True )
    content = models.TextField()
    follow = models.ManyToManyField(User, related_name="tweet_follow" , blank=True )
    message = models.TextField( null= True)
    images = models.ImageField(null=True , blank= True ,upload_to = "images/" )
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def total_likes(self):
        return self.likes.count()




class Comment(models.Model):
    chat = models.ForeignKey(Full_chat ,related_name="comments", on_delete= models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __aiter__(self):
        return "%s - %s" % (self.chat.content , self.name)

