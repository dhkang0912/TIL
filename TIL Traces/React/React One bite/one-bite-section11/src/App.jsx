import Header from "./components/Header";
import Editor from "./components/Editor";
import List from "./components/List";
// import Exam from "./components/Exam";
import "./App.css";
import {
  useState,
  useRef,
  useReducer,
  useCallback,
  createContext,
  useMemo,
} from "react";

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

// 데이터를 하위 컴포넌트에 전달, 웬만하면 컴포넌트 외부에 선언
// useContext를 통해 업데이트 되면 객체가 다시 생성되는 것과 같아서 useMemo가 안 먹힘
// => state와 함수를 분리하기
// export const TodoContext = createContext();
// console.log(TodoContext)
// TodoContext.Provider가 중요함 => 컴포넌트로 컨텍스트가 공급하거나 공급받을 데이터를 설정하기 위한 프로퍼티
export const TodoStateContext = createContext()
export const TodoDispatchContext = createContext()


function App() {
  // 임시로 체크하기 위한 데이터
  // const [todos, setTodos] = useState(mockData);
  // 첫번째 인자 = 컴포넌트 외부의 상태관리 함수, 두번째 인자 = 초기값
  const [todos, dispatch] = useReducer(reducer, mockData);

  // id를 기억하기 위해서는 ref 객체가 필요함
  const idRef = useRef(3);

  const onCreate = useCallback((content) => {
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
  }, []);

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
  const onUpdate = useCallback((targetId) => {
    // todos State의 값들 중에 tagetId와 일치하는 id를 갖는 todo Item의 isDone 변경
    dispatch({
      type: "UPDATE",
      targetId: targetId,
    });
  }, []);

  // const onDelete = (targetId) => {
  //   // 인수 : todos 배열에서 targetId와 일치하는 id를 갖는 요소만 삭제한 새로운 배열
  //   // => targetId와 같지 않은 todo로만 배열을 만들어서 반환
  //   dispatch({
  //     type: "DELETE",
  //     targetId: targetId,
  //   });
  // };

  // deps가 변경됐을 때만 리렌더링하고 함수를 메모이제이션해줌
  // deps를 빈 배열로 두면 마운트될 때만 함수 렌더링
  const onDelete = useCallback((targetId) => {
    dispatch({
      type: "DELETE",
      targetId: targetId,
    });
  }, []);

  const memoizedDispatch = useMemo(()=> {
    return {onCreate, onUpdate, onDelete}
  },[])

  return (
    <div className="App">
      <Header />
      {/* 하위에 있는 모든 데이터는 TodoContext로 공급됨 */}
      {/* value props로 객체로 묶어서 전달해줌 */}
      <TodoStateContext.Provider value={todos}>
        <TodoDispatchContext.Provider value={memoizedDispatch}>
        <Editor/>
        <List/>
        </TodoDispatchContext.Provider>
      </TodoStateContext.Provider>
    </div>
  );
}

export default App;
