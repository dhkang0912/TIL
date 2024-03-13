## Django Template system
- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
### HTML의 콘텐츠를 변수 값에 따라 바꾸고 싶다면?
- view.py의 함수에 context를 추가하고 render함수에 3번째 인자로 추가
- Django Template Language를 통해 HTML 파일에서 {{}}을 통해 키 지정

### DTL Syntax
- Variable
    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    - dot을 사용하여 변수 속성에 접근할 수 있음
    - 예: {{variable}}, {{variable.attribute}}
- Filters
    - 표시할 변수를 수정할 때 사용 (변수 + | + 필터) 
    - 보여지는 것만 달라짐
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
    - 예 : {{variable|filter}}, {{name | truncatewords:30}}
- Tag
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags를 제공
    - 예 : {%tag%}, {%if%}-시작, {%endif%}-종료
- Comments
    - {# #} -> 한줄 주석처리
    - {% comment %} -> 여러줄 주석처리

## 템플릿 상속
- 만약 모든 템플릿에 bootstrap을 적용하려면?
- 모든 템플릿에 bootstrap CDN을 작성해야 할까?

### 템플릿 상속
- Template inheritance
    1.  페이지의 공통요소를 포함하고, 
    2. 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축

### 상속 구조 만들기
- skeleton 역할을 하게 되는 상위 템플릿 작성
    - body에 {% block 'name' %} {% endblock 'name'%}을 작성
- 하위 템플릿에 {% extends '상위템플릿 주소' %} -> 가장 상위에 작성
    {% block 'name' %} 내용 {% endblock 'name'%}

- extends tag
    - 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
    - 반드시 자식 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가)
 
- block tag
    - 하위 템플릿에서 재정의할 수 있는 블록을 정의 (상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것)

## HTML form (요청과 응답)
### form element
- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공

- action & method
    - 데이터를 어디(action)로 어떤 방식(method)로 요청할지

- action
    - 입력 데이터가 전송될 URL을 지정(목적지)
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
- method
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    - 데이터의 HTTP requests methods (GET, POST)를 지정
    - GET을 사용한 경우 입력한 것이 드러남
- input
    - 사용자의 데이터를 입력 받을 수 있는 요소
    - type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
    - name attribute : input의 핵심 속성, 입력한 데이터에 붙이는 이름 (key), 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음
- Query String Parameters
    - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버를 보내는 방법
    - 문자열은 앰퍼샌드 ('&')로 연결된 key=value 쌍으로 구성되며 기본 URL과는 물음표로 구분됨
    - 예 : https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=ssafy

```
<form action="https://search.naver.com/search.naver">
        <label for="query">검색 :</label>
        <input type="text" id="message" name="query" >
        <input type="submit">
    </form>
```