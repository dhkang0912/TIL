import { useState, useRef } from "react";
// 간단한 회원가입 폼
// 1. 이름
// 2. 생년 월일
// 3. 국적
// 4. 자기소개

const Register = () => {
  // 비슷한 유형의 state가 있을 때는 하나의 state로 통합해서 만들면 편함
  const [input, setInput] = useState({
    name: "",
    birth: "",
    country: "",
    bio: "",
  });

  // 자바스크립트 문법 let이 아니라 useRef를 사용하는 이유
  // 버튼을 클릭하면 컴포넌트인 Register 함수가 리렌더링됨, let의 경우 리렌더링될 때마다 계속 리셋이 됨
  // 아무리 수정을 해도 수정횟수로 세지지가 않음
  // useRef로 만든 경우 컴포넌트가 리렌더링되어도 다시 초기화되지 않음, 이전 값을 기억하고 감 
  const countRef = useRef(0);
  const inputRef = useRef();

  // let count = 0

  // 비슷한 유형의 상태 변경 함수가 있을 경우 통합시켜서 관리하면 편함
  const onChange = (e) => {
    countRef.current++;
    // count++
    console.log(countRef);
    // console.log(count)
    setInput({
      // 스프레드 연산자로 기존 값 나열
      ...input,
      // 자바스크립트 프로퍼티 key를 변수 이름으로 동적으로 사용
      [e.target.name]: e.target.value,
    });
    // console.log(e.target)
  };

  const onSubmit = () => {
    if (input.name === "") {
      // 이름을 입력하는 DOM 요소에 포커스(선택된 상태로 만들기)
      // console.log(inputRef.current)
      // DOM 요소에 접근해서 focus 메소드로 비어있는 경우 선택된 상태로 만들기
      inputRef.current.focus()
    }
  };

  return (
    <div>
      {/* <button
      // useRef를 사용했기 때문에 버튼을 눌러도 리렌더링되진 않음
        onClick={() => {
          refObj.current++;
          console.log(refObj.current);
        }}
      >
        ref + 1
      </button> */}

      <div>
        <input
        // ref 속성에 DOM 요소가 저장됨
          ref={inputRef}
          name="name"
          value={input.name}
          onChange={onChange}
          placeholder={"이름"}
          type="text"
        />
        {input.name}
      </div>

      <div>
        <input
          name="birth"
          value={input.birth}
          onChange={onChange}
          type="date"
        />
        {input.birth}
      </div>

      <div>
        <select name="country" value={input.country} onChange={onChange}>
          <option></option>
          <option value="kr">한국</option>
          <option value="us">미국</option>
          <option value="uk">영국</option>
        </select>
        {input.country}
      </div>

      <div>
        <textarea name="bio" value={input.bio} onChange={onChange} />
        {input.bio}
      </div>

      <button onClick={onSubmit}>제출</button>
    </div>
  );
};

export default Register;
