## HTML 'form'
- 지금까지 사용자로부터 데이터를 받기 위해 활용한 방법
- 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
    -> 유효한 데이터인지에 대한 확인이 필요

## 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

## Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공
```
#articles/forms.py
from Django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

## Widgets
- HTML 'input' element의 '표현'을 담당

## Django ModelForm
- HTML form과 동일한 기능이지만 더 강력하고 유연하며 유효성 검사를 할 수 있음

### Form VS ModelForm
- Form : 사용자 입력 데이터를 DB에 저장하지 않을 때 (로그인 - 매칭만 시키고 정보를 저장하지 않음)
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (게시글 작성, 회원가입)

## New & Create view 함수 간 공통점과 차이점
### 공통점 : 데이터 생성을 구현하기 위함
### 차이점 : new = Get method 요청만을 create = POST method 요청만 처리
