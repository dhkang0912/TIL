import { TodoDispatchContext } from "../App";
import "./TodoItem.css";
import { memo, useContext } from "react";

// todoItem의 경우 객체값을 받기 때문에 같은 값을 받아도 메모리 주소가 달라지기 때문에 다른 props를 받는다고 여겨져서 제대로 리렌더링됨
// 얕은 비교를 하기 때문에 객체 타입의 값은 props가 바뀌었다고 판단하게 됨
// => 이런 경우 함수 자체를 메모이제이션 하거나 memo 함수의 두번째 인자에 콜백함수를 넣어서 커스터마이징 할 수 있음
const TodoItem = ({ id, isDone, content, date }) => {
  const {onUpdate, onDelete} = useContext(TodoDispatchContext)
  const onChangeCheckBox = () => {
    onUpdate(id);
  };

  const onDeleteBtn = () => {
    onDelete(id);
  };

  return (
    <div className="TodoItem">
      {/* onClick이 아니라 onChange로 작성한 이유는 button이 아니라 input 요소이기 때문 */}
      <input
        readOnly
        onChange={onChangeCheckBox}
        checked={isDone}
        type="checkbox"
      />
      <div className="content">{content}</div>
      {/* 문자열 datestamp를 새로운 date 객체를 생성하고 날짜 형태의 문자열로 보여지게 변환 */}
      <div className="date">{new Date(date).toLocaleDateString()}</div>
      <button onClick={onDeleteBtn}>삭제</button>
    </div>
  );
};

export default memo(TodoItem)

// 고차 컴포넌트
// 두번째 인자에 콜백함수를 넣어서 해당 콜백함수에 의해 props가 변경됐는지 여부를 확인
// export default memo(TodoItem, (prevProps, nextProps) => {
//   // 반환값에 따라, Props가 바뀌었는지 안 바뀌었는지 판단
//   // T -> Props 바뀌지 않음 -> 리렌더링을 하지 말라
//   // F -> Props 바뀜 -> 리렌더링을 해라
//   if (prevProps.id !== nextProps.id) return false;
//   if (prevProps.isDone !== nextProps.isDone) return false;
//   if (prevProps.content !== nextProps.content) return false;
//   if (prevProps.date !== nextProps.date) return false;

//   return true;
// });

