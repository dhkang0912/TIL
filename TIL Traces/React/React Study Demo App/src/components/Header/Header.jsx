import reactImg from '../../assets/react-core-concepts.png'
import './Header.css'

const reactDescriptions = ['Fundamental', 'Crucial', 'Core'];

// 무작위로 숫자를 만드는 함수를 만듦
function genRandomInt(max) {
  return Math.floor(Math.random() * (max + 1));
}

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