# from django.db import models
# # from 회원폴더명.models import 회원모델명
#
#
# # 피드 게시물 모델
# class FeedModel(models.Model):
#     class Meta:
#         db_table = "board_feed"
#
#     author = models.ForeignKey(게시글, on_delete=models.CASCADE)
#
#     content = models.CharField(max_length=256)
#     # content = 게시글.내용
#     # feed_content = content[:100]
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     # tweet_created = 게시글.생성일
#     updated_at = models.DateTimeField(auto_now=True)
#     # 수정시 수정됨 표시? 뷰?
