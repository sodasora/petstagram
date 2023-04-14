from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MypageModel

# - 내 게시물 보기 → 모든 유저
# - 프로필 수정 기능 → 나만
#로그인이 필요한 페이지


@login_required
def mypage_view(request):
    #로그인한 사용자인 경우
    if request.method == 'GET':
        Mypage = MypageModel.objects.all().order_by('-created_at')


        return render(request, 'mypage/mypage.html', {'mypage': Mypage})


@login_required
def mypage_update_view(request):
    # 로그인한 사용자인 경우
    if request.method == 'POST':
        user = request.user  # 현재 로그인한 사용자
        username = request.POST.get('username')  # 업데이트할 사용자 이름
        email = request.POST.get('email')  # 업데이트할 이메일 주소
        # 기존 사용자 정보 업데이트
        user.username = username
        user.email = email
        user.save()  # 변경사항 저장
        messages.success(request, '정보가 성공적으로 업데이트되었습니다.')  # 성공 메시지
        return redirect('/mypage/')  # 마이페이지로 리다이렉트
    else:
        return render(request, 'mypage/mypage_update.html')