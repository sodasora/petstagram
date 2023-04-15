from django.db import models
from user.models import UserModel
from board.models import Post


# 마이페이지 게시물 모델
class MypageModel(models.Model):
    class Meta:
        db_table = "mypage"

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    title = models.CharField("제목",max_length=50)
    content = models.CharField("내용",max_length=225)

    created_at = models.DateTimeField("작성시간",auto_now_add=True)
    updated_at = models.DateTimeField("수정시간",auto_now=True)
