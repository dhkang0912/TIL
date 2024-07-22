import "./List.css";
import TodoItem from "./TodoItem";
import { useMemo, useState, useContext } from "react";
import { TodoStateContext } from "../App";

const List = () => {
  const todos = useContext(TodoStateContext)
  const [search, setSearch] = useState("");

  const onChangeSearch = (e) => {
    setSearch(e.target.value);
  };

  const getFilteredData = () => {
    if (search === "") {
      // 검색어가 없다면 전체 todos를 반환
      return todos;
    }

    return todos.filter((todo) =>
      // 배열의 모든 todos를 순회하면서 각 todo의 content에 {search}에 들어있는 단어가 포함되면 true를 반환하고 그 값들만 배열에 모아서 반환함
      // 소문자로 전환한 검색어가 소문자로 전환한 내용에 포함되어있는 것들을 배열로 반환
      todo.content.toLowerCase().includes(search.toLowerCase())
    );
  };

  const filteredTodos = getFilteredData();

  // useMemo도 deps가 변경됐을 때 콜백함수를 다시 호출해줌
  // + 콜백함수에서 return하는 값을 반환도 해줌
  // 첫번째 인자에는 메모이제이션을 하고 싶은 값을 넣어야 함
  const {totalCount, doneCount, notDoneCount} = useMemo(()=>{
    console.log("getAnalyzedData 호출")
    const totalCount = todos.length;
    const doneCount = todos.filter((todo) => todo.isDone).length;
    const notDoneCount = totalCount - doneCount;

    return {
      totalCount,
      doneCount,
      notDoneCount,
    };
    // 빈 배열이 들어가면 처음 렌더링 될 때만 계산됨, 일반 함수를 넣어서 호출했을 때는 리렌더링 될 때마다 계산되지만 이 경우에는 딱 한번만 수행하게 됨
    // todos state의 변화에 따라 콜백함수가 실행되고 값을 반환하고 싶은 경우에는 deps에 todos state를 작성한다.
  }, [todos])
  // 의존성 배열 : deps
  // 비슷한 hook : useEffect => deps가 변경됐을 때 콜백함수를 다시 호출해주는 react hook

  

  return (
    <div className="List">

      <h4>Todo List✨</h4>
      <div>
        <div>total : {totalCount}</div>
        <div>done :{doneCount}</div>
        <div>notDone : {notDoneCount}</div>
      </div>
      <input
        value={search}
        onChange={onChangeSearch}
        placeholder="검색어를 입력하세요"
      />
      <div className="todos_wrapper">
        {filteredTodos.map((todo) => {
          return (
            <TodoItem
              key={todo.id}
              {...todo}
            />
          );
        })}
      </div>
    </div>
  );
};

export default List;
