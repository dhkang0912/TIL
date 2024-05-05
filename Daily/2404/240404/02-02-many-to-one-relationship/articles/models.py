from django.db import models
# django에서는 User 모델을 직접 참조하지 않음
from accounts.models import User #get_user_model()을 사용하는 경우 객체가 미리 생성되지 않는 경우 에러가 남, 모델 이후 객체가 생성되기 때문, 모델 이외 전체 사용
from django.conf import settings # settings.AUTH_USER_MODEL = 문자열을 반환, 모델에서는 이걸로 사용함

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

