from django.shortcuts import render, redirect
from .models import DetailPost
from board.models import Post
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, TemplateView

### 중간 생략 #############


@login_required
def detail_post(request, id):
    post_detail = Post.objects.get(id=id)
    return render(request,'detailpost/post_detail.html',{'detailpost':post_detail})

@login_required()
def delete_post(request, id):
    my_tweet = Post.objects.get(id=id)
    my_tweet.delete()
    return redirect('/main')