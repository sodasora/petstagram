from django.db import models
from user.models import UserModel
from board.models import Post


# 피드 게시물 모델
class FeedModel(models.Model):
    class Meta:
        db_table = "board_feed"

    feed = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField("제목",max_length=50)
    content = models.CharField("내용",max_length=225)
    # content = 게시글.내용
    # feed_content = content[:100]

    created_at = models.DateTimeField(auto_now_add=True)
    # tweet_created = 게시글.생성일
    updated_at = models.DateTimeField(auto_now=True)
    # 수정시 수정됨 표시? 뷰?
