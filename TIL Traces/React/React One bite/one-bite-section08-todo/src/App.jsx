import Header from "./components/Header";
import Editor from "./components/Editor";
import List from "./components/List";
import "./App.css";
import { useState, useRef } from "react";

const mockData = [
  {
    id: 0,
    isDone: false,
    content: "React 공부하기",
    // 현재 날짜를 타임스탬프 형식으로 기록
    date: new Date().getTime(),
  },
  {
    id: 1,
    isDone: false,
    content: "빨래하기",
    // 현재 날짜를 타임스탬프 형식으로 기록
    date: new Date().getTime(),
  },
  {
    id: 2,
    isDone: false,
    content: "노래 연습하기",
    // 현재 날짜를 타임스탬프 형식으로 기록
    date: new Date().getTime(),
  },
];

function App() {
  // 임시로 체크하기 위한 데이터
  const [todos, setTodos] = useState(mockData);
  // id를 기억하기 위해서는 ref 객체가 필요함
  const idRef = useRef(3);

  const onCreate = (content) => {
    const newTodo = {
      id: idRef.current++,
      isDone: false,
      content: content,
      date: new Date().getTime(),
    };

    // State 값은 직접 바꾸면 되지 않고 무조건 State 함수를 통해 추가해야한다.
    // 인자에 적힌 배열로 todos를 업데이트함
    // => newTodo + todos의 내용을 배열에서 펼쳐서 객체들끼리만 모아서 spread syntax를 활용하여 배열에 추가
    setTodos([newTodo, ...todos]);
  };

  return (
    <div className="App">
      <Header />
      <Editor onCreate={onCreate} />
      <List />
    </div>
  );
}

export default App;
