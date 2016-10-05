from django.db import models

# Create your models here.
class Post(models.Model):
    # 글 제목
    title = models.CharField(max_length=40)
    # 간단설명
    description = models.CharField(max_length=100)
    # 본문내용
    content = models.TextField()
    # 좋아요 수
    like_count = models.IntegerField(default=0) 
    # 조회수
    view_count = models.IntegerField(default=0)
    # 생성일자
    created = models.DateTimeField(auto_now_add=True)
    # Shell 환경에서 ORM으로 접근했을 때 각각의 데이터의 정보를 보여주는 것.
    def __str__(self):
        return self.title
