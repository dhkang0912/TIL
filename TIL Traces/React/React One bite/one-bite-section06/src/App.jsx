import { useState } from "react";
import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Controller";

// 모든 데이터들은 가장 상단으로 끌어올려져야 함 => State lifting
// 위에서 아래로 단방향 데이터 흐름을 가지고 있음
function App() {
  const [count, setCount] = useState(0);
  // 이벤트 핸들러 자체를 만들어서 그걸 그대로 props로 넘기는 방법이 있음
  const onClickButton=(value)=>{
    setCount(count+value)
  }

  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section>
        <Viewer count={count}/>
      </section>
      <section>
        <Controller onClickButton={onClickButton}/>
      </section>
    </div>
  );
}

export default App;
