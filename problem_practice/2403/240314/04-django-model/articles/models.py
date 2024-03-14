from django.db import models

# Create your models here.
# 데이터의 설계도 초안을 작성한 것
class Article(models.Model):
    # 테이블의 필드(컬럼)이름 = 필드의 데이터 타입(제약 조건)
    # 데이터 타입마다 제약조건으로 걸 수 있는게 있음

    # CharField는 max_length가 필수적인 제약조건임
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    # 최종 테이블 이름은 '앱이름_모델클래스이름'으로 합성해서 만들어짐
    # 1. model class 변경
    # 2. makemigrations
    # 3. migrate