## [리액트][Udemy React 완벽가이드 2024] - 리액트 핵심 : 컴포넌트, JSX, Prop(속성), 상태 등 (48~54강)
### children
- 컴포넌트 사이에 별 다른 조작없이 글을 작성하기만 하면 어디에 출력할지 리액트가 알지 못해서 무시함
- 컴포넌트 사이에 작성한 글자를 기본적으로 children으로 받게 됨
  - 이렇게 받은 children은 따로 props로 작성하지 않아도 컴포넌트 매개변수로 받을 수 있음
- 이를 components composition(컴포넌트 합성)이라고 함
```
<section id="examples">
    <h2>Examples</h2>
    <menu>
        {/* 아래와 같이 컴포넌트 사이에 글을 별 다른 조작없이 작성만 하면 어디에 출력할지 정해지지 않아 리액트가 자동으로 무시함 */}
        {/* <TabButton>Components</TabButton> */}

        {/* 이렇게 props로 작성할 수도 있음 */}
        {/* <TabButton label="components"></TabButton> */}

        {/* 이렇게 작성하는 걸 컴포넌트 합성이라고 함 */}
        <TabButton>Components</TabButton>
        <TabButton>JSX</TabButton>
        <TabButton>Props</TabButton>
        <TabButton>State</TabButton>
    </menu>
</section>
```

- 기본적으로 props를 매개변수로 받으면 컴포넌트 사이에 작성한 글자를 children 객체로 받음
- props로 받는 것도 가능함
```
// props로 받기
// export default function TabButton ({label}){
//     return <li><button>{label}</button></li>
// }

// 기본적으로 children을 받는 법
export default function TabButton (props){
    return <li><button>{props.children}</button></li>
}

// 구조분해 할당으로 children을 받는 법
export default function TabButton ({children}){
    return <li><button>{children}</button></li>
}
```

### 이벤트 처리하기
- 이벤트를 추가할 때도 prop을 통해 추가하여 컴포넌트 함수에 작성해줌
- on을 먼저 작성하면 자동완성 리스트로 사용할 수 있는 prop들이 나옴
- 이벤트 추가 시 행동할 함수를 값으로 작성해줘야 함 (소괄호를 넣으면 안됨)
  - 소괄호를 넣어서 함수로 작성하면 이벤트 발생 시에 함수가 실행되는게 아니라 페이지가 렌더링되기 때문에 함수 이름만 작성
```
export default function TabButton ({children}){

// 이벤트 발생 시 동작할 함수 선언
    function handleClick(){
        console.log("Hello World")
    }
    // 이벤트를 추가할 때도 prop을 넣어줌
    // on~은 prop을 추가하는 것으로 함수로 작성해야함
    // 함수 값을 넣고 싶기 때문에 소괄호를 넣으면 안되고 함수 이름만 작성해야함 
    return <li><button onClick={handleClick}>{children}</button></li>
}
```

### 이벤트 함수를 prop으로 전달하기
- 이벤트 리스너를 컴포넌트 함수에서가 아니라 적용될 상단의 jsx 파일에서도 선언할 수 있음

```
export default function TabButton ({children, onSelect}){

    // 이벤트를 추가할 때도 prop을 넣어줌
    // on~은 prop을 추가하는 것으로 함수로 작성해야함
    // 함수 값을 넣고 싶기 때문에 소괄호를 넣으면 안되고 함수 이름만 작성해야함 
    return <li><button onClick={onSelect}>{children}</button></li>
}
```
```
// 함수 선언 후 return 전
function handleSelect() {
    console.log("Hello World - selected!")
  }

//return 후

<section id="examples">
    <h2>Examples</h2>
    <menu>
        <TabButton onSelect={handleSelect}>Components</TabButton>
        <TabButton onSelect={handleSelect}>JSX</TabButton>
        <TabButton onSelect={handleSelect}>Props</TabButton>
        <TabButton onSelect={handleSelect}>State</TabButton>
    </menu>
</section>
```

### 이벤트 함수에 커스텀 인자 전달하기
- 기존 코드에서 이벤트 함수에서 소괄호를 작성하면 함수 값인 이름이 전달되는게 아니라 렌더링될 때 함수가 실행돼서 매개변수를 가질 수 없었음
- 이를 해결하기 위해 익명함수를 사용하게 됨
  - 익명함수를 사용하면 이벤트 함수 매개변수에서 함수 호출이 아닌 함수 정의가 되어 매개변수를 넣어서 사용할 수 있음
  - 익명함수는 간단하게 화살표 함수로 사용할 수 있음 
    - ()=>
  - 물론 익명의 함수 선언도 가능하다 function (){}

```
// 함수 선언 후 return 전
function App() {
  function handleSelect(selectedButton) {
    console.log(selectedButton)
  }

// return 후
<section id="examples">
    <h2>Examples</h2>
    <menu>
        <TabButton onSelect={() => handleSelect("components")}>Components</TabButton>
        <TabButton onSelect={() => handleSelect("jsx")}>JSX</TabButton>
        <TabButton onSelect={() => handleSelect("props")}>Props</TabButton>
        <TabButton onSelect={() => handleSelect("state")}>State</TabButton>
    </menu>
</section>
```

### UI 업데이트 안되는 이유
- tabContent를 선언하고 클릭 시 재할당되게 코드를 적었음에도 화면에 보여지는 tabContent의 내용은 변동이 없음
- 하지만 console 창을 보면 tabContent 내용이 바뀌어 console이 찍히는 것을 확인할 수 있음
- 이유가 무엇일까?
  - 자바스크립트의 특성 상 한번 ui가 실행되면 따로 설정을 해주지 않는 이상 업데이트가 되지 않음
  - 리액트에게 ui가 업데이트 되어야 한다는 걸 알려줘야 함
  => 그렇기 때문에 state가 필요함

```
function App() {
  // tabContent를 선언
  let tabContent = "Please click a button"

  function handleSelect(selectedButton) {
    // console.log(selectedButton)
    // 클릭 시 내용 변경
    tabContent = selectedButton
    console.log(tabContent)
  }

  return (
    <div>
      <Header />
      <main>
        <section id='core-concepts'>
          <h2>Core Concepts</h2>
          <ul>
            <CoreConcept
              // 이런 식으로 props를 통해 object, array, string, number 정보를 컴포넌트에 넘겨줄 수 있음
              title="Components"
              description="The core UI building block"
              image={componentsImg}
            />
            {/* 속성 이름과 props의 속성 이름이 동일한 경우 직접 중괄호를 추가할 수 있음, 속성이 아니라 자바스크립트 기능인 스프레드 연산자를 통해 모든 키 값 쌍을 펼침 */}
            {/* 이걸 더 추천함 */}
            <CoreConcept {...CORE_CONCEPTS[1]} />
            <CoreConcept
              title={CORE_CONCEPTS[2].title}
              image={CORE_CONCEPTS[2].image}
              description={CORE_CONCEPTS[2].description}
            />
            <CoreConcept
              title={CORE_CONCEPTS[3].title}
              image={CORE_CONCEPTS[3].image}
              description={CORE_CONCEPTS[3].description}
            />
          </ul>
        </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
            {/* 아래와 같이 컴포넌트 사이에 글을 별 다른 조작없이 작성만 하면 어디에 출력할지 정해지지 않아 리액트가 자동으로 무시함 */}
            {/* <TabButton>Components</TabButton> */}

            {/* 이렇게 props로 작성할 수도 있음 */}
            {/* <TabButton label="components"></TabButton> */}

            {/* 이렇게 작성하는 걸 컴포넌트 합성이라고 함 */}
            <TabButton onSelect={()=>handleSelect("components")}>Components</TabButton>
            <TabButton onSelect={()=>handleSelect("jsx")}>JSX</TabButton>
            <TabButton onSelect={()=>handleSelect("props")}>Props</TabButton>
            <TabButton onSelect={()=>handleSelect("state")}>State</TabButton>
          </menu>
          {tabContent}
        </section>
      </main>
    </div>
  );
}

export default App;
```

![](https://velog.velcdn.com/images/sarah0912/post/511240cb-3687-42a8-987f-413d2d5b0191/image.png)

### State 관리 및 Hook 사용법
#### Hook 사용법
- Hook은 component 안에서 호출되어야 하지만 중첩되면 안 된다.
  - 내부 함수에 작성되면 안됨
- Hook은 component의 제일 첫 줄에 작성되어야 한다.
- useState를 사용하여 데이터가 변경되면 상태를 업데이트 시킬 수 있음

#### useState
- 기본적으로 배열을 반환함
- const [selectedTopic, setSelectedTopic] = useState("Please click a button")
  - useState("초기내용 작성")
  - selectedTopic = 기존 작성된 내용 또는 초기내용
  - setSelectedTopic = 변경된 내용을 업데이트 시키는 함수, 저장된 값을 업데이트 함
- 리액트가 작동하는 방식에 의해 selectedTopic이 가지고 있는 값은 업데이트 됐지만 console에 찍히는 내용은 과거 내용

```
import { useState } from 'react';

function App() {
  // const stateArray = useState("Please click a button")
  // selectedTopic = 기존 작성된 내용 또는 초기내용, setSelectedTopic = 변경된 내용을 업데이트 시키는 함수, 저장된 값을 업데이트 함
  const [selectedTopic, setSelectedTopic] = useState("Please click a button")

  function handleSelect(selectedButton) {
    // console.log(selectedButton)
    // 
    setSelectedTopic(selectedButton)
    // console 찍으면 리액트가 작동하는 방식 때문에 과거 정보가 나옴
    console.log(selectedTopic)
  }

  return (
    <div>
      <Header />
      <main>
        <section id='core-concepts'>
          <h2>Core Concepts</h2>
          <ul>
            <CoreConcept
              // 이런 식으로 props를 통해 object, array, string, number 정보를 컴포넌트에 넘겨줄 수 있음
              title="Components"
              description="The core UI building block"
              image={componentsImg}
            />
            {/* 속성 이름과 props의 속성 이름이 동일한 경우 직접 중괄호를 추가할 수 있음, 속성이 아니라 자바스크립트 기능인 스프레드 연산자를 통해 모든 키 값 쌍을 펼침 */}
            {/* 이걸 더 추천함 */}
            <CoreConcept {...CORE_CONCEPTS[1]} />
            <CoreConcept
              title={CORE_CONCEPTS[2].title}
              image={CORE_CONCEPTS[2].image}
              description={CORE_CONCEPTS[2].description}
            />
            <CoreConcept
              title={CORE_CONCEPTS[3].title}
              image={CORE_CONCEPTS[3].image}
              description={CORE_CONCEPTS[3].description}
            />
          </ul>
        </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
            {/* 아래와 같이 컴포넌트 사이에 글을 별 다른 조작없이 작성만 하면 어디에 출력할지 정해지지 않아 리액트가 자동으로 무시함 */}
            {/* <TabButton>Components</TabButton> */}

            {/* 이렇게 props로 작성할 수도 있음 */}
            {/* <TabButton label="components"></TabButton> */}

            {/* 이렇게 작성하는 걸 컴포넌트 합성이라고 함 */}
            <TabButton onSelect={()=>handleSelect("components")}>Components</TabButton>
            <TabButton onSelect={()=>handleSelect("jsx")}>JSX</TabButton>
            <TabButton onSelect={()=>handleSelect("props")}>Props</TabButton>
            <TabButton onSelect={()=>handleSelect("state")}>State</TabButton>
          </menu>
          {selectedTopic}
        </section>
      </main>
    </div>
  );
}

export default App;
```

### Data 기반 State 가져와서 출력하기
```
// 관련 정보가 있는 파일을 가져와서 import함
import {EXAMPLES} from './data'


// 초기 내용을 EXAMPLES에서 찾을 수 있는 내용으로 변경
  const [selectedTopic, setSelectedTopic] = useState("components")


<div id="tab-content">
    {/* EXAMPLES 객체의 속성이 변수명이 되어야 하기 때문에 []를 사용, 자바스크립트 문법 */}
    {/* EXAMPLES 객체에서 선택된 변수명을 속성으로 한 값들을 찾아서 출력 */}
    <h3>{EXAMPLES[selectedTopic].title}</h3>
    <p>{EXAMPLES[selectedTopic].description}</p>
    <pre>
        <code>
            {EXAMPLES[selectedTopic].code}
        </code>
    </pre>
</div>
```