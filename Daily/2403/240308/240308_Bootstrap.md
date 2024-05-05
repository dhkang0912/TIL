## CSS 배운 것들
1. 구조 / 스타일링
2. 레이아웃, 배치, 공간 배분, 정렬 (position, flexbox)

## Bootstrap
- CSS 프론트엔드 프레임워크 (Toolkit)
    - 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

- CDN
    - Content Delivery Network
    - 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
    - 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높임)
    - 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

## Bootstrap 기본 사용법
- {property}{sides}-{size}
    - ex) mt-5 => 이게 클래스
- property
    1. m : margin
    2. p : padding
- Sides
    1. t : top
    2. b : bottom
    3. s : left
    4. e : right
    5. y : top, bottom
    6. x : left, right
    7. blank : 4 sides
- size
    - rem
    - 1 단위마다 0.25rem씩 늘어남
        => 4px씩 이전 단위에 곱해짐

## Reset CSS
- 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
    -> HTML element, Table, List 등의 요소들에 일관성 있게 스타일을 적용 시키는 기본 단계

- 모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음
    - 웹사이트를 보다 읽기 편하게 하기 위해 설정되어있음
- 모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야 하는 개발자에겐 매우 골치 아픈 일
- 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자!

### Normalize CSS
- Reset CSS 방법 중 대표적인 방법
- 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

## Bootstrap 활용
### Typography
- 제목, 본문, 텍스트, 목록 등

### Colors
### 대표 components
- Alerts
- Badges
- Buttons
- Cards
- Navbar
- carousel : 회전목마, 이미지 넘어가는 것
    => 버튼과 연결된 id를 잘 확인해야함
- Modal
- modal id 값과 버튼의 data-bs-target이 각각 올바르게 일치하는지 확인
- 주의사항
    1. modal 코드와 button 코드가 반드시 함께 다녀야 할까?
    서로 같이 안 다녀도 버튼만 잘 끌고 다니면 됨
    2. modal 코드가 다른 코드 안쪽에 중첩되어 들어가버리면 modal이 켜졌을 때 회식 화면 뒤로 감춰질 수 있음
    3. modal 코드는 주로 body 태그가 닫히는 곳에 모아두는 것을 권장


## Bootstrap을 사용하는 이유
- 장점
    - 크로스 브라우징 지원
        - 모든 주요 브라우저에서 작동하도록 설계되어있음
    - 가장 많이 사용되는 CSS 프레임 워크
    - 사전에 디자인된 다양한 컴포넌트 및 기능
        - 빠른 개발과 유지 보수
    - 손쉬운 반응형 웹 디자인 구현
    - 커스터마이징이 용이

- 단점
    - 자유도가 제한됨


## Semantic Web
- 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식
- 이 요소가 가진 의미는 무엇일까?를 고민하는 것

### HTML 요소가 의미를 가진다는 것
- p태그에서 크기를 준 것과 H1을 쓴 것
    -> 단순한 크기와 최상위 제목이라는 의미를 주는 것
- 검색 시 웹사이트 정보만 나오는 게 아니라 웹사이트의 상세 정보도 같이 나옴
    -> SEO (검색 엔진 최적화)를 함
- 대표적인 Semantic Element
    - div랑 완전히 똑같은 기능을 가지고 있지만 의미론적으로 나누는 태그
        1. header
        2. nav
        3. main
        4. articl
        5. section
        6. aside
        7. footer

### OOCSS
- Object Oriented CSS
    - 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론

- 기본 원칙
    1. 구조와 스킨을 분리
    2. 컨테이너와 콘텐츠를 분리


## 책임과 역할
- HTML : 콘텐츠의 구조와 의미
- CSS : 레이아웃과 디자인

## 의미론적인 마크업이 필요한 이유
- 검색엔진 최적화 (SEO)
    - 검색엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌

- 웹 접근성