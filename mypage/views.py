from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
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
        nickname = request.POST.get('nickname')  # 업데이트할 닉네임
        password = request.POST.get('password')  # 업데이트할 새 비밀번호
        confirm_password = request.POST.get('confirm_password')  # 비밀번호 확인

        # 기존 사용자 정보 업데이트
        user.username = username
        user.email = email
        user.nickname = nickname

        # 새 비밀번호가 입력되었는지 확인
        if password:
            # 새 비밀번호와 비밀번호 확인이 일치하는지 확인
            if password == confirm_password:
                user.set_password(password)
            else:
                messages.error(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')  # 오류 메시지
                return redirect('/mypage_update/')  # 내 정보 수정 페이지로 리다이렉트

        user.save()  # 변경사항 저장
        messages.success(request, '비밀번호가 바뀌었습니다.')  # 성공 메시지
        update_session_auth_hash(request, request.user)  # 세션에 로그인 정보 갱신
        logout(request)
        return redirect('/')  # 홈페이지로 리다리렉트
    else:
        return render(request, 'mypage/mypage_update.html')

