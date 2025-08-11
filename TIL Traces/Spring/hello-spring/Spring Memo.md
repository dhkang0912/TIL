### 1. MVC와 템플릿 엔진
- MVC : Model, View, Controller
  - Model: 비지니스 로직, 내부 처리, 데이터베이스 처리 계산
  - View: 화면 그리는 것에 집중
  - Controller : Model과 View 사이의 중재아 역할
    - @Controller 어노테이션 사용


- MVC의 흐름
1. 사용자가 Controller에 요청
2. Controller가 Model에서 데이터 처리
3. Controller가 View에 데이터 전달
4. View가 사용자에게 결과 표시

