from django.db import models
from django.conf import settings


class Movie(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Review')
    code = models.IntegerField(primary_key=True)            # 영화 식별 코드
    title = models.TextField()                              # 영화명(국문)
    title_origin = models.TextField()                       # 영화명(원문)
    release_date = models.TextField()                       # 개봉일
    status = models.BooleanField()                          # 개봉여부
    overview = models.TextField()                           # 줄거리
    language = models.CharField(max_length=20)              # 언어
    poster = models.TextField(blank=True, null=True)        # 포스터 image URL

    def __str__(self):
        return self.title


class Actor(models.Model):
    movie = models.ManyToManyField(Movie)
    code = models.IntegerField(primary_key=True)            # 배우 식별 코드
    name = models.CharField(max_length=50)                  # 배우 이름
    profile = models.TextField(blank=True, null=True)       # 배우 프로필 image URL

    def __str__(self):
        return self.name


class Genre(models.Model):
    movie = models.ManyToManyField(Movie)
    code = models.IntegerField(primary_key=True)            # 장르 식별 코드
    name = models.CharField(max_length=10)                  # 장르 이름

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HashTag(models.Model):
    review = models.ManyToManyField(Review)
    tag = models.CharField(max_length=20)                   # 태그명

    def __str__(self):
        return self.tag