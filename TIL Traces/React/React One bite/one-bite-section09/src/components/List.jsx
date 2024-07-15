import "./List.css";
import TodoItem from "./TodoItem";
import { useState } from "react";

const List = ({ todos, onUpdate, onDelete }) => {
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

  return (
    <div className="List">
      <h4>Todo List✨</h4>
      <input
        value={search}
        onChange={onChangeSearch}
        placeholder="검색어를 입력하세요"
      />
      <div className="todos_wrapper">
        {filteredTodos.map((todo) => {
          return <TodoItem key={todo.id} {...todo} onUpdate={onUpdate} onDelete={onDelete} />;
        })}
      </div>
    </div>
  );
};

export default List;
