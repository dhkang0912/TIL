// 이미지 파일을 사용하는 경우 import하여 사용하는 것을 권장
import componentsImg from './assets/components.png'
import Header from './components/Header/Header';
import CoreConcepts from './components/CoreConcepts';
import Examples from './components/Examples';

// React Hook
import { useState, Fragment } from 'react';


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
    <Fragment>
      <Header />
      <main>
        <CoreConcepts/>
        <Examples/>
      </main>
    </Fragment>
  );
}

export default App;