## HTTP
- 네트워크 상에서 데이터를 주고 받기 위한 약속

## HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
    - GET, POST
    
### Get Method
- 특정 리소스를 조회하는 요청 (데이터를 전달할 때 URL에서 Query String 형식으로 보내짐)

### POST Method
- 특정 리소스에 변경(생성, 수정, 삭제 -> DB에 변화를 줌)를 요구하는 요청
  (데이터는 전달할 때 HTTP Body에 담겨 보내짐)
  
- 게시글을 작성하겠다는 의미
- request.POST를 사용해야함

## HTTP response status code
- 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것
### 403 Forbidden
- 서버에 요청이 전달외었지만, 권한 때문에 거절되었다는 것을 의미
- 거절된 이유 : CSRF token(사용자 인증)이 누락됨 
  -> Cross-Site-Request-Forgery : 사이트 간 요청 위조
  

- POST 방식으로 하는 경우 DB에 영향을 주는 요청 
- 겉모습이 똑같은 위조 사이트나 정상적이지 않은 요청에 대한 방어 수단 
  (dajngo가 만든 사이트가 맞는지 확인)  
  -> 요청 데이터 + 인증 토큰 -> 게시글 작성
  
- input하고 submit하는 곳에 {% csrf_token %}을 작성하여 토큰을 확인할 수 있음
    - 숨겨져서 token이 매번 랜덤으로 주어짐

## Redirect
- 게시글 작성 후 완료를 알리는 페이지를 응답하는 페이지가 뜨나 사용자의 경우 다른 페이지가 보이게 해야한다
  (사용자를 보냄 == 사용자가 GET 요청을 한번 더 보내도록 해야함)
  
- redirect를 해서 원래 페이지로 돌아가더라도 되돌아가는 기능이 있는게 아니라 메인 페이지로 가라는 요청을 다시 보낸 것
### redirect()
- 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
- create view 함수 개선

### redirect 특징
- 작성한 url로 요청을 다시 보내게 됨
- 결과적으로 detail view 함수가 호출되어 detail view 함수의 반환 결과인 detail 페이지를 응답 받음
```
def create(request):
    ...
    return redirect('articles:detail', article.pk)
```

## Delete
- 삭제 시 띠울 url을 만들고 -> view 함수를 만듦
- 조회를 먼저 하고 삭제를 할 수 있음
- redirect를 통해 삭제된 결과를 보여줌

## Update
### Update 로직을 구현하기 위해 필요한 view 함수 개수 = 2개
- 사용자 입력 데이터를 받을 페이지를 렌더링 = edit
- 사용자가 입력한 데이터를 받아 DB에 저장 = update

-> 조회를 먼저하고, 조회한 것을 가져와서 수정

## 참고
### HTTP request methods를 활용한 효율적인 URL 구성
- URL 한개로 method에 따라 서버에 요구하는 행동을 다르게 요구
= get, post를 한 url에서 표현

### 이전 과정들을 다 연습해야함 -> CRUD 기능을 구현할 줄 아는 것이 핵심, 정말 많이 쓰임