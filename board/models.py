from django.db import models

# Create your models here.
class Post(models.Model):  # 새로운 모델을 생성
    class Meta:
        db_table = "post"

    title = models.CharField("제목",max_length=50,default='제목을 입력해주세요.')
    # author = models.ForeignKey(User, on_delete=models.CASCADE) # user의 model 이 없습니다.
    content = models.CharField("내용",max_length=225)
    create_at = models.DateTimeField("작성시간",auto_now_add=True)
    update_at = models.DateTimeField("수정시간",auto_now=True)
