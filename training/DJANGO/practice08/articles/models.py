from django.db import models
from django.contrib.auth import get_user_model 

class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    writer = models.ForeignKey(get_user_model(), verbose_name = "작성자", on_delete = models.CASCADE)