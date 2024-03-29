from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 내장 user 클래스를 상속받아서 가져옴
class User(AbstractUser):
    pass


