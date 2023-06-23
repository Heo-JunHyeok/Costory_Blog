from django.db import models


# Create your models here.
class Post(models.Model):
    # 제목, 내용, 작성일, 수정일
    title = models.CharField(max_length=50)
    content = models.TextField()
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title
