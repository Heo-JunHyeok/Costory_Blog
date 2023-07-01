from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols


# Create your models here.
class Post(models.Model):
    # 제목, 내용, 작성일, 수정일
    title = models.CharField(
        max_length=50,
        unique=True,  # 1. Field 인자로 유효성 검증
        error_messages={"unique": "이미 있는 제목이네요!"},
    )
    content = models.TextField(
        validators=[  # 2. Built-in Validator
            MinLengthValidator(10, "너무 짧군요! 10자 이상 적어주세요."),
            validate_symbols,  # 3. Custom Validator
        ]
    )
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title
