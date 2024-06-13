// 이미지 파일을 사용하는 경우 import하여 사용하는 것을 권장
import componentsImg from './assets/components.png'
import { CORE_CONCEPTS } from './data';
import Header from './components/Header/Header';
import CoreConcept from './components/CoreConcept';
import TabButton from './components/TabButton';
import { EXAMPLES } from './data'

// React Hook
import { useState } from 'react';


// props는 object로 정보가 전달되어 key, value 쌍으로 정보를 가지고 있음
// props를 통해 비슷한 구조의 여러 데이터를 한꺼번에 볼 수 있음
// function CoreConcept(props) {
//   return (
//     <li>
//       <img src={props.image} alt={props.title} />
//       <h3>{props.title}</h3>
//       <p>{props.description}</p>
//     </li>
//   )
// }


function App() {
  // const stateArray = useState("Please click a button")
  // selectedTopic = 기존 작성된 내용 또는 초기내용, setSelectedTopic = 변경된 내용을 업데이트 시키는 함수, 저장된 값을 업데이트 함
  // 초기 내용을 EXAMPLES에서 찾을 수 있는 내용으로 변경
  const [selectedTopic, setSelectedTopic] = useState(null)

  function handleSelect(selectedButton) {
    // console.log(selectedButton)
    // 
    setSelectedTopic(selectedButton)
    // console 찍으면 리액트가 작동하는 방식 때문에 과거 정보가 나옴
    console.log(selectedTopic)
  }

  let tabContent = <p>Please select a topic.</p>
  if (selectedTopic) {
    tabContent = (
      <div id="tab-content">
        <h3>{EXAMPLES[selectedTopic].title}</h3>
        <p>{EXAMPLES[selectedTopic].description}</p>
        <pre>
          <code>
            {EXAMPLES[selectedTopic].code}
          </code>
        </pre>
      </div>
    )
  }

  return (
    <div>
      <Header />
      <main>
        <section id='core-concepts'>
          <h2>Core Concepts</h2>
          <ul>
            {/* JSX는 코드 배열과 같이 렌더링 가능한 데이터 배열을 처리할 수 있음 */}
            {/* {[<p>Hello</p>,<p>World</p>]} */}
            {/* 동적으로 CoreConcept을 출력해야 나중에 데이터 수가 줄어들거나 늘어나도 깨지지 않음 */}

            {/* JSX 안에서 객체를 읽도록 해서 동적으로 이미지나 데이터를 처리할 수 있도록 함 */}
            {CORE_CONCEPTS.map((conceptItem) => (
              <CoreConcept key={conceptItem.title} {...conceptItem} />
            ))}

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
            <TabButton isSelected={selectedTopic === 'components'}
              onSelect={() => handleSelect("components")}>
              Components
            </TabButton>

            <TabButton isSelected={selectedTopic === 'jsx'}
              onSelect={() => handleSelect("jsx")}>
              JSX
            </TabButton>

            <TabButton isSelected={selectedTopic === 'props'}
              onSelect={() => handleSelect("props")}>
              Props
            </TabButton>

            <TabButton isSelected={selectedTopic === 'state'}
              onSelect={() => handleSelect("state")}>
              State
            </TabButton>

          </menu>
          {tabContent}
          {/* 삼항연산자를 사용하여 selectedTopic이 초기값인 null로 undefined 상태라면 글을 보여주고 그렇지 않다면 선택한 것의 글자들을 보여주게 함 */}
          {/* {!selectedTopic ? (
            <p>Please select a topic.</p>
          ) : (
            <div id="tab-content"> */}
          {/* EXAMPLES 객체의 속성이 변수명이 되어야 하기 때문에 []를 사용, 자바스크립트 문법 */}
          {/* <h3>{EXAMPLES[selectedTopic].title}</h3>
              <p>{EXAMPLES[selectedTopic].description}</p>
              <pre>
                <code>
                  {EXAMPLES[selectedTopic].code}
                </code>
              </pre>
            </div>
          )} */}

          {/* && 연산자를 활용해서도 작성 가능, 논리 AND 연산자로 조건이 사실이라면 AND 바로 뒤에 나온 것을 출력함 */}
          {/* {!selectedTopic && <p>Please select a topic.</p>}
          {selectedTopic && <div id="tab-content">
            <h3>{EXAMPLES[selectedTopic].title}</h3>
            <p>{EXAMPLES[selectedTopic].description}</p>
            <pre>
              <code>
                {EXAMPLES[selectedTopic].code}
              </code>
            </pre>
          </div>
          } */}
        </section>
      </main>
    </div>
  );
}

export default App;