from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 나를 기준으로 확인하면 됨, 팔로잉한 user를 확인하기 위함, 자동 맞팔로우 기능을 원하지 않으면 symetrical= False
    # related_name을 설정 안 하는 경우 user1.user_set.all이 되기 때문에 역참조 매니저 이름을 변경
    # 따로 필드를 만든 것이 아니라 중개 테이블을 만들어냄
    followings = models.ManyToManyField('self',symmetrical=False, related_name='followers')
