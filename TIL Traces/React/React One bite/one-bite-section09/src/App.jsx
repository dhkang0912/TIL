import Header from "./components/Header";
import Editor from "./components/Editor";
import List from "./components/List";
// import Exam from "./components/Exam";
import "./App.css";
import { useState, useRef, useReducer } from "react";

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

function reducer(state, action) {
  switch (action.type) {
    // 새로운 todoItem을 배열에 넣고, 기존 state를 펼쳐서 새로운 배열을 state로 반환함
    case "CREATE":
      return [action.data, ...state];
    case "UPDATE":
      return state.map((item) =>
        item.id === action.targetId ? { ...item, isDone: !item.isDone } : item
      );
    case "DELETE":
      return state.filter((item) => item.id !== action.targetId);
    default:
      return state;
  }
}

function App() {
  // 임시로 체크하기 위한 데이터
  // const [todos, setTodos] = useState(mockData);
  // 첫번째 인자 = 컴포넌트 외부의 상태관리 함수, 두번째 인자 = 초기값
  const [todos, dispatch] = useReducer(reducer, mockData);

  // id를 기억하기 위해서는 ref 객체가 필요함
  const idRef = useRef(3);

  const onCreate = (content) => {
    dispatch({
      type: "CREATE",
      data: {
        id: idRef.current++,
        isDone: false,
        content: content,
        date: new Date().getTime(),
      },
    });
    // State 값은 직접 바꾸면 되지 않고 무조건 State 함수를 통해 추가해야한다.
    // 인자에 적힌 배열로 todos를 업데이트함
    // => newTodo + todos의 내용을 배열에서 펼쳐서 객체들끼리만 모아서 spread syntax를 활용하여 배열에 추가
  };

  // 조건문으로 길게 작성
  // const onUpdate = (targetId)=>{
  //   // todos State의 값들 중에 tagetId와 일치하는 id를 갖는 todo Item의 isDone 변경
  //   setTodos(todos.map((todo)=>{
  //     if(todo.id === targetId){
  //       return {
  //         ...todo,
  //         // 기존 todo의 isDone 상태를 토글시키기
  //         isDone: !todo.isDone
  //       }
  //     }
  //     // 만약 targetId와 id가 일치하지 않는 todo라면 isDone을 변경하지 않고 기존 todo를 리턴
  //     return todo
  //   }))
  // }

  // 삼항연산자 활용하여 간단하게 작성
  const onUpdate = (targetId) => {
    // todos State의 값들 중에 tagetId와 일치하는 id를 갖는 todo Item의 isDone 변경
    dispatch({
      type: "UPDATE",
      targetId: targetId,
    });
  };

  const onDelete = (targetId) => {
    // 인수 : todos 배열에서 targetId와 일치하는 id를 갖는 요소만 삭제한 새로운 배열
    // => targetId와 같지 않은 todo로만 배열을 만들어서 반환
    dispatch({
      type: "DELETE",
      targetId: targetId,
    });
  };

  return (
    <div className="App">
      <Header />
      <Editor onCreate={onCreate} />
      <List todos={todos} onUpdate={onUpdate} onDelete={onDelete} />
    </div>
  );
}

export default App;
