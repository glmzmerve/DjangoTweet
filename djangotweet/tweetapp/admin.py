from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Message',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]})
    ]
    #fields=['message','nickname']



admin.site.register(Tweet,TweetAdmin)

