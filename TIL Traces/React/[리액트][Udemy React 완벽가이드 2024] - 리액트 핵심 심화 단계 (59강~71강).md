## [리액트][Udemy React 완벽가이드 2024] - 리액트 핵심 심화 단계 (59강~71강)
### Fragments 사용법
- JSX return에서는 하나의 상위 요소 혹은 부모 요소가 항상 있어야 함
  - return 이후 최상위 요소는 한개만 있어야 함, 같은 계층에 형제가 존재하면 안됨
  - JSX는 자바스크립트 함수와 같으며 이는 한 가지의 값만 반환할 수 있기 때문에 형제 요소가 있으면 에러가 남
  - 이렇게 만들어주기 위해 div로 감싸고 그 안에 원하는 요소를 포함시킴
  => Dom에 중복되어 div가 생길 수 있음
    - 이를 위해 리액트가 대안으로 fragments를 제공함, root 컴포넌트가 필요한 경우 fragments를 통해 형제 컴포넌트들을 감쌀 수 있음, 대신 화면 상으로 나타나는 실제 요소를 렌더링하면 안됨

- Fragement를 import하여 형제 컴포넌트들을 감싸기 위해 작성한 div 대신 태그로 사용
```
import { Fragment } from 'react';

return (
    <Fragment>
      <Header />
      ...
    </Fragment>
  );

```
   
- Fragments 대신 빈태그를 사용하여 div를 대신하기도 함
```
return (
    <>
      <Header />
      ...
    </>
  );
  
```
- 컴포넌트를 나눠서 useState가 컴포넌트 안으로 쪼개지는 경우 App.jsx에 포함된 게 아니라서 다시 렌더링 되지 않아 변경되지 않음


### 내부 요소에 props(속성)가 전달되지 않을 경우
- 비슷한 구조로 이루어진 경우 따로 컴포넌트를 만들 수 있음
- 이때 컴포넌트를 따로 만드는 경우 상위 태그의 속성이 구조 분해 할당되지 않는 경우 컴포넌트 내부로 전달되지는 않음
  - 스타일링이 달라질 수 있음
  
=> forwarded props(전달 속성), proxy props(대리 속성)을 통해 하나씩 구조 분해 할당을 하지 않더라도 내부 컴포넌트로 속성 전달 가능

- 나머지 매개변수를 통해 수동으로 지정해준 매개변수 외의 다른 매개변수들을 그룹핑해줌
- section 영역에서 스프레드 연산자로서 나머지 매개변수를 전부 펼쳐서 적용해줌

```
export default function Section({title, children, ...props}){
    return <section {...props}>
        <h2>{title}</h2>
        {children}
    </section>
}
```

<br>

### 여러 JSX 슬롯 사용법
```
export default function Tabs({ children, buttons }) {
    return <>
        <menu>
            {buttons}
        </menu>
        {children}
    </>
}
```
```
    return (
        <Section id="examples">
            <Tabs buttons={
                <>
                    <TabButton isSelected={selectedTopic === 'components'}
                        onClick={() => handleSelect("components")}>
                        Components
                    </TabButton>

                    <TabButton isSelected={selectedTopic === 'jsx'}
                        onClick={() => handleSelect("jsx")}>
                        JSX
                    </TabButton>

                    <TabButton isSelected={selectedTopic === 'props'}
                        onClick={() => handleSelect("props")}>
                        Props
                    </TabButton>

                    <TabButton isSelected={selectedTopic === 'state'}
                        onClick={() => handleSelect("state")}>
                        State
                    </TabButton>
                </>}>
                {tabContent}
            </Tabs>
          </Section>
    )
}
```
- jsx 코드는 결국 정규값으로 코드에서 여느 값으로 사용됨
  - 따라서 위의 코드처럼 들어가야할 jsx 코드의 내용을 속성으로 넘길 수가 있음
  - 대신 jsx 코드는 형제 요소가 있는 경우 값으로 넘길 수 없으니 fragments를 사용하여 root를 만들어서 값을 넘기고, 매개변수로 받기


### 컴포넌트 타입 동적으로 설정하기
```
export default function Tabs({ children, buttons, ButtonsContainer }) {
    // buttonsContainer는 소문자로 시작하여 내장 속성을 검색함, 하지만 이런 빌트인 요소는 없음, 이를 커스텀 컴포넌트로 사용하기 위해서는 대문자로 시작하는 변수를 선언하여 할당해줘야 함
    // const ButtonsContainer = buttonsContainer
    return <>
        <ButtonsContainer>
            {buttons}
        </ButtonsContainer>
        {children}
    </>
}
```
```
<Section id="examples">
            <Tabs 
            ButtonsContainer="menu"
```
- 식별자와 커스텀 컴포넌트 둘 다 사용 가능
  - 내장 식별자를 사용하는 경우 문자열로 작성
  - 커스텀 컴포넌트나 변수를 사용하는 경우 중괄호 문법 사용
  ``` <Section id="examples">
            <Tabs 
            ButtonsContainer={section} 
  ```
- 위와 같이 사용하는 경우 내장 식별자나 커스텀 컴포넌트를 상위 컴포넌트에 매개변수로 전달하여 사용할 수 있음, 대신 속성 변수의 이름을 대문자로 시작해줘야 컴포넌트로 인식함

### 기본 props(속성) 값 설정
```
export default function Tabs({ children, buttons, ButtonsContainer='menu' }) {
    // buttonsContainer는 소문자로 시작하여 내장 속성을 검색함, 하지만 이런 빌트인 요소는 없음, 이를 커스텀 컴포넌트로 사용하기 위해서는 대문자로 시작하는 변수를 선언하여 할당해줘야 함
    // const ButtonsContainer = buttonsContainer
    return <>
        <ButtonsContainer>
            {buttons}
        </ButtonsContainer>
        {children}
    </>
}
```
```
 return (
        <Section id="examples">
            <Tabs
```
- 상단에 정리한 컴포넌트 타입을 속성으로 받아서 사용하는 것은 동일하지만 자바스크립트 문법인 기본값 매개변수(default parameter)를 사용하여 ButtonsContainer의 기본이 되는 'menu' 빌트인 속성을 작성할 수 있음
- 이렇게 된 경우 menu 속성을 사용하는 경우 따로 ButtonsContainer 속성을 Tabs의 속성으로 따로 보내주지 않아도 됨


### 모든 콘텐츠가 컴포넌트에 담기지 않아도 되는 이유
- 만약 변경되지 않는 정적인 콘텐츠라면 굳이 컴포넌트에 넣지 않아도 됨
- index.html에 넣을 수 있음

### 이미지 저장소 Public VS Assets
- public에 저장된 이미지는 어디서나 따로 경로를 지정하지 않아도 파일 이름으로 불러 쓸 수 있으며 웹사이트 방문객들에게 공개적으로 파일이 제공됨

- assets에 저장된 이미지는 경로를 지정하여 파일을 불러 쓸 수 있음, 웹사이트 방문객들에게 공개적으로 파일이 제공되지 않음(웹사이트 방문자가 해당 파일에 접근할 수 없음)
  - 대신,src/ (및 하위 폴더)에 저장된 파일은 코드 파일에서 사용할 수 있음. 코드 파일에 가져온 이미지는 빌드 프로세스에 의해 인식되어 최적화되며, 웹사이트에 제공하기 직전에 public/ 폴더에 "삽입"됨, 가져온 이미지는 참조한 위치에서 자동으로 링크가 생성되어 사용됨

<br>

- 빌드 프로세스에 의해 처리되지 않는 이미지는 public/폴더를 사용 (예: index.html 파일이나 파비콘과 같은 이미지)

- 컴포넌트 내에서 사용되는 이미지는 일반적으로 src/폴더(예: src/assets/)에 저장

