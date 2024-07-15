import "./Editor.css";
import { useState, useRef } from "react";

const Editor = ({ onCreate }) => {
  const [content, setContent] = useState("");
  const contentRef = useRef();

  const onChangeContent = (e) => {
    setContent(e.target.value);
  };

  // 키보드의 키값을 누를 때 누른 키의 값이 event에 저장
  const onKeyDown = (e) => {
    if (e.keyCode === 13) {
      // todo에 추가되도록 함수 호출
      onSubmit();
    }
  };

  const onSubmit = () => {
    // content의 내용이 비어있다면 추가되지 않도록 추가 전 강제로 함수 종료하게 return
    if (content === "") {
      contentRef.current.focus();
      return;
    }
    onCreate(content);
    // todo에 추가 이후 content를 초기화하여 입력된 내용 비워주기
    setContent("");
  };

  return (
    <div className="Editor">
      <input
        ref={contentRef}
        value={content}
        onKeyDown={onKeyDown}
        onChange={onChangeContent}
        placeholder="새로운 Todo..."
      />
      <button onClick={onSubmit}>추가</button>
    </div>
  );
};

export default Editor;
