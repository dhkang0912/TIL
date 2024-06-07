## ORM 
### Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

### ORM의 역할
- 사용하는 언어가 다르기 때문에 소통이 불가하지만 Django에 내장된 ORM이 중간에서 이를 해석해줌


## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리  
  

- QuerySet = 다중 데이터, 데이터 묶음
- Instance = 단일 데이터

### QuerySet API 구문
- Article.objects.all() # 전체를 주는 것
    =  Model class, Manager, Queryset API
  
### Query
- 데이터베이스에 특정한 데이터를 보여달라는 요청
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터 베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환

## QuerySet API는?
- python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것  
= CRUD

## 외부 라이브러리 설치 및 설정
1. pip install ipython
2. pip install django-extensions
3. pip freeze > requirements.txt
4. settings에서 'django_extensions' 앱 등록해주기
5. python manage.py shell_plus


## 대표적인 조회 메서드
### 1. Return new QuerySets
- all(): 전체 데이터 조회
  - Article.objects.all()
- filter() : 특정 조건 데이터 조회
    - Article.objects.filer(title='abc')

### 2. Do not return Querysets
- get() : 단일 데이터 조회
    - 객체를 찾을 수 없으면 Does not Excist 예외를 발생
    - 둘 이상 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
    - primary key와 같이 고유성을 보장하는 조회에서 사용해야 함
    - Article.objects.get(pk=100)
    
## 데이터 수정
```
# 수정할 인스턴스 조회
article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
article.title = 'byebye'

# 저장
article.save()

# 정상적으로 변경된 것을 확인
article.title

```


##데이터 삭제
```
# 삭제할 인스턴스 조회
article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제된 객체가 반환)
article.delete()

# 삭제한 데이터는 더 이상 조회할 수 없음
Article.objects.get(pk=1)
```

## 참고
### Field lookups
- 특정 레코드에 대한 조건을 설정하는 법
- Queryset 메서드 filter(), exclude(), get()에 대한 키워드 인자로 지정
```
# Field lookups 예시
# "content 컬럼에서 'dja'가 포함된 모든 데이터 조회"
Article.objects.filter(content__contains='dja')
```

## ORM, QuerySet API를 사용하는 이유
- 데이터 베이스 쿼리를 추상화하여 Django 개발자가 데이터 베이스와 직접 상호작용하지 않아도 되도록함
- 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움
