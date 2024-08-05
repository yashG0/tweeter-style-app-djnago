from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("tweets/", tweets, name="tweets"),
    path("create/", createTweet, name="createTweet"),
    path("<int:tweet_id>/editTweet/", editTweet, name="editTweet"),
    path("<int:tweet_id>/removeTweet/", removeTweet, name="removeTweet"),
    path("register/", register, name="register"),
    path("accounts/", include('django.contrib.auth.urls')),  # Include authentication URLs
]