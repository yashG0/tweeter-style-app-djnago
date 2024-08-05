from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.contrib.auth import login

from .forms import TweetForm, UserRegistrationForm



# Create your views here.
def test(request) -> HttpResponse:
    return HttpResponse("welcome to testing screen")


def register(request:HttpRequest):
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request,user)
            return redirect("tweets")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form":form})

def home(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="index.html")


def tweets(request: HttpRequest) -> HttpResponse:
    res = Tweet.objects.all().order_by("-created_at")
    return render(request, template_name="tweets.html", context={"tweets": res})

@login_required
def createTweet(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweets")
    else:
        form = TweetForm()

    return render(request, template_name="tweetsForm.html", context={"form": form})

@login_required
def editTweet(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweets")
    else:
        form = TweetForm(instance=tweet)

    return render(request, "tweetsForm.html", context={"form": form})

@login_required
def removeTweet(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect("tweets")

    return render(request, "tweetDeleted.html", context={"form":tweet})
