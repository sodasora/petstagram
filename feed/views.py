from django.shortcuts import render, redirect
from .models import FeedModel
from django.contrib.auth.decorators import login_required


# 메인페이지 게시글 피드
def mainpage_feed(request):
    if request.method == 'GET':
        all_feed = FeedModel.objects.all().order_by('-created_at')

        return render(request, 'feed/petstagram.html', {'all_feed': all_feed})



