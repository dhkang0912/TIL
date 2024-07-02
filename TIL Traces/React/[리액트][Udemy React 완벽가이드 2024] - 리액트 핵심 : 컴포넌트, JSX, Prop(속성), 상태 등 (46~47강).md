## [리액트][Udemy React 완벽가이드 2024] 리액트 핵심 - 컴포넌트, JSX, Prop(속성), 상태 등 (46~47강)
### 컴포넌트 별로 쪼개기
- 한 파일에 모든 컴포넌트를 저장하는 것을 추천하지 않음, 별도의 컴포넌트는 각 파일에 저장하는 것을 추천함
- src 폴더 안에 components 폴더를 만들고 그 안에 파일을 생성하는 것이 기본적임
- 이후 각 컴포넌트가 되는 함수마다 파일을 생성하여 export하고, 기본 골조가 되는 App.jsx에서 import 해줌

<br>

  - 컴포넌트 예시 : Header.jsx
```
import reactImg from '../assets/react-core-concepts.png'

const reactDescriptions = ['Fundamental', 'Crucial', 'Core'];

// 무작위로 숫자를 만드는 함수를 만듦
function genRandomInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

// Header function을 기본적으로 export해줌
export default function Header() {
    // JSX로 return 되기 전 상수나 변수로 할당하면 이를 가지고 return의 JSX 코드에서 활용할 수 있음
    // 직접 작성하는 것도 가능하지만 이렇게 하는 경우 좀 더 Lean하고 명확하게 코드를 확인할 수 있어서 더 추천됨
    const description = reactDescriptions[genRandomInt(2)]

    return (
        <header>
            {/* 이런 식으로 파일을 가져오면 배포 시 최적화 단계를 거치면서 이미지가 사라질 수도 있음, 권장되지 않는 방식 */}
            {/* <img src="src/assets/react-core-concepts.png" alt="Stylized atom" /> */}
            {/* 아래 방식처럼 "" 없이 중괄호문법을 통해 import한 이미지를 사용하는 것을 추천 */}
            <img src={reactImg} alt="Stylized atom" />
            <h1>React Essentials</h1>
            <p>
                {/* {} 중괄호를 통해서 동적인 표현값을 넣을 수 있음 */}
                {/* {reactDescriptions[genRandomInt(2)]} React concepts you will need for almost any app you are going to build! */}
                {description} React concepts you will need for almost any app you are going to build!
            </p>
        </header>
    );
}
```

<br>

  - App.jsx
```
// 이미지 파일을 사용하는 경우 import하여 사용하는 것을 권장
import componentsImg from './assets/components.png'
import { CORE_CONCEPTS } from './data';
// 파일을 분리해준 컴포넌트의 이름을 정해주고 import 해줌
import Header from './components/Header';
import CoreConcept from './components/CoreConcept';


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
      </main>
    </div>
  );
}

export default App;
```
<br>

### css 파일 쪼개기
- css 파일도 컴포넌트처럼 쪼갤 수 있음
- 하지만 적용하기 위해서는 적용하고자 하는 컴포넌트 파일에 css 파일을 import 해야함
- 이렇게 import된 css 파일의 문제점은 css 적용 범위가 제한된 것이 아니라 해당 컴포넌트가 import된 곳에서 다른 요소들을 추가했을 때도 스타일이 적용될 수 있다.
- scoped하게 css 파일을 적용하는 방법은 향후 나올 예정

