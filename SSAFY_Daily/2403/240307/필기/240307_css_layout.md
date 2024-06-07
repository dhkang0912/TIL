## CSS Box Model
- 모든 HTML 요소를 사각형 박스로 표현하는 개념
    - 만약 원을 표현한다면 네모 박스 공간을 가지고 그 안에 원이 있는 것
    - 모든 영역은 네모난 박스 공간을 가진다

- 내용 (content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되는 개념  
![Alt text](Box의구성요소.png)
![Alt text](Box구성의방향별명칭.png)

- 요소의 너비와 높이를 지정할 때 콘텐츠 영역을 대상으로 함
![Alt text](width&height속성.png)
    *{
        box-sizing: border-box;
    }
    => 위 코드를 통해 width, height의 속성을 box size로 지정할 수 있게 됨

## Box Type
- Normal flow
    - CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향 좌측 위에서 시작
- Block 
    - 무언가를 막는 타입
    - 위아래로 배치
    - 항상 새로운 행으로 나뉨 => 한줄을 차지하기 때문
    - width와 height를 지정할 수 있음
        - 지정하지 않으면 한줄을 다 채움
    - h1~6, p, div
- Inline
    - 어딘가에 들어갈 수 있는 타입
    - 좌우로 배치
    - 새로운 행으로 나뉘지 않음
    - width와 height 속성을 사용할 수 없음 
        => 본인이 가진 콘텐츠의 크기만큼만 차지함
    - 수직 방향
        - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수 없음
        - inline으로 위아래 margins를 주는게 의미가 없음
    - 수평 방향
        - padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
        (흐르는 방향이 수평 방향이기 때문)

- 배치할 때 관점을 바꿔야 함
    - 영역 이동하고 조정하는 싸움
    - 둘어싸고 있는 영역을 어떻게 배치할 것인가?
    - 보통 배치할 객체를 옮기려고 생각하지만 그렇게 생각하면 어려움
    - 그게 아니라 margin이나 영역을 어떻게 배치해야할지를 고민해야함

- Inline-block
    - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
    - inline + block => 둘의 장단점을 보완
    - block 요소의 특징을 가짐
        - width 및 height 속성 사용 가능
        - padding, margin 및 border로 인해 다른 요소가 밀려남
    - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용

- None
    - 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

- shorthand 속성 :
    - border
        - border-width, border-style, border-color를 한번에 설정하기 위한 속성
        - 작성 순서는 영향을 주지 않음
    - margin & padding
        - 4방향의 속성을 각각 지정하지 않고 한번에 지정할 수 있는 속성
        - 4개일 때 : 상우하좌
        - 3개일 때 : 상/좌우/하

- Margin Collapsing
    - 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상
        - 상하만 상쇄됨, 좌우는 상쇄되지 않음
    - 더 작은 쪽이 상쇄됨
    - 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
    - 양쪽을 계속 밀어내지 않고 한쪽에서만 설정하기 위함 => 유지보수가 편하게 하기 위해


## CSS Layout
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
    - Display, Position, Float, Flexbox(최신) 등

### CSS Position
- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 디자인을 한다는 건 먼저 Normal Flow에서 벗어나는 것 => 그래야 원하는 위치에 이동할 수 있음
- Normal flow를 제거하여 원하는 위치에 고정하는 것
- 이동 방향
    - top, bottom, left, right, Z Axis

## Position의 예시
- static
    - 기본 값
    - 요소를 Normal Flow에 따라 배치
- relative
    - 요소를 Normal Flow에 따라 배치
    - 자기 자신을 기준으로 이동
    - 요소가 차지하는 공간은 static일 때와 같음
- absolute
    - 요소를 Normal Flow에서 제거
    - 가장 가까운 relative 부모 요소를 기준으로 이동 (아무리 가도 부모가 없다면 body를 기준으로 이동)
    (부모가 이동하면 따라서 가기 위해, fixed가 아님)
    - 문서에서 요소가 차지하는 공간이 없어짐
- fixed
    - 요소를 Normal Flow에서 제거
    - 현재 화면 영역(viewport)을 기준으로 이동
    - 문서에서 요소가 차지하는 공간이 없어짐
- sticky
    - 요소를 Normal Flow에 따라 배치
    - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨(fixed)
    - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
        => 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
- Z-index
    - 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
    - 정수 값을 사용해 Z축 순서를 지정
    - 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

## 참고
### Position의 역할
- 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것

## CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 공간배열 & 정렬
- 부모 설정을 잘해놓고, 자식 요소들을 어떻게 배치할지 할 수 있음 => 부모가 컨트롤
(Flex container, Flex item)
- 좌상단이 시작점
![Alt text](flexbox구성요소.png)
- main axis, cross axis
    -> main axis는 좌우로 흐름
- 부모 요소에 flex 값을 넣어주고 배치 컨트롤

- Flex box 요소
1. Flex container 지정
    - display : flex ;
    - 기본적인 가로 방향으로 나열
2. Flex-direction 
    - flex item이 나열되는 방향
    - row, column 방향 
        - reverse 방향 가능
3. Flex-wrap
    - flex item 목록이 flex container의 한 행에 들어가지 않을 경우 다른 행에 배치할지 여부 설정
4. justify-content
    - 주 축을 따라 flex item과 주위에 공간을 분배
5. align-content
    - 교차 축을 따라 flex item과 주위에 공간을 분배
    - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
6. align-items
    - 교차 축을 따라 flex item 행을 정렬
7. align-self
    - 교차 축을 따라 개별 flex item을 정렬
8. flex-grow
    - 남는 행 여백을 비율에 따라 각 flex item에 분배
9. flex-basis
    - flex item의 초기 크기 값을 지정


- 목적에 따른 속성 분류
    - 배치 : flex-direction, flex-wrap
    - 공간 분배 : justify-content, align-content
    - 정렬 : align-items, align-self

- 속성명 Tip
    - justify : 주축
    - align : 교차 축
    - content : 여러줄
    - items : 한줄
    - self : 요소 한개