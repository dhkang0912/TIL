import { useState,useEffect,useRef } from "react";
import "./App.css";
import Viewer from "./components/Viewer";
import Controller from "./components/Controller";
import Even from "./components/Even";

// 모든 데이터들은 가장 상단으로 끌어올려져야 함 => State lifting
// 위에서 아래로 단방향 데이터 흐름을 가지고 있음
function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("")

  const isMount = useRef(false)

  // 1. 마운트 : 탄생
  // 마운트의 경우 처음 연결될 때만 실행되기에 이후 다른 게 변경되어도 실행되지 않음, deps로 빈 배열을 넘기면 됨
  useEffect(()=>{
    console.log("mount")
  },[])
  // 2. 업데이트 : 변화, 리렌더링
  // deps 생략 시 처음 마운트할 때와 리렌더링될 때마다 콜백함수 실행
  useEffect(()=>{
    // mount 시 console이 찍히지 않고 리렌더링 시에만 console을 찍고 싶은 경우
    // useRef를 통해 Mount 여부를 저장하는 변수를 만들고 mount 여부를 바꿔주고 return을 통해 콜백함수를 나가게 함으로써 업데이트 되지 않고 Mount만 된 경우에는 console이 찍히지 않게 함
    if(!isMount.current){
      isMount.current = true
      return
    }
    console.log("update")
  })
  // 3. 언마운트 : 죽음

  // 이벤트 핸들러 자체를 만들어서 그걸 그대로 props로 넘기는 방법이 있음
  const onClickButton=(value)=>{
    setCount(count+value)
  }

  return (
    <div className="App">
      <h1>Simple Counter</h1>
      <section><input value={input} onChange={(e)=>{
        setInput(e.target.value)
      }} /></section>
      <section>
        <Viewer count={count}/>
        {count % 2 === 0 ? <Even/> : null}
      </section>
      <section>
        <Controller onClickButton={onClickButton}/>
      </section>
    </div>
  );
}

export default App;
