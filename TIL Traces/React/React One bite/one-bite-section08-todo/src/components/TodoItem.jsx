import "./TodoItem.css"

const TodoItem = ({id, isDone, content, date, onUpdate, onDelete}) => {
  const onChangeCheckBox = ()=>{
    onUpdate(id)
  }

  const onDeleteBtn = ()=>{
    onDelete(id)
  }

  return (
    <div className="TodoItem">
      {/* onClick이 아니라 onChange로 작성한 이유는 button이 아니라 input 요소이기 때문 */}
      <input readOnly onChange={onChangeCheckBox} checked={isDone} type="checkbox" />
      <div className="content">{content}</div>
      {/* 문자열 datestamp를 새로운 date 객체를 생성하고 날짜 형태의 문자열로 보여지게 변환 */}
      <div className="date">{new Date(date).toLocaleDateString()}</div>
      <button onClick={onDeleteBtn}>삭제</button>
    </div>
  );
};

export default TodoItem;
