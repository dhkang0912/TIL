import { useState } from "react";
// 간단한 회원가입 폼
// 1. 이름
// 2. 생년 월일
// 3. 국적
// 4. 자기소개

const Register = () => {
  const [input, setInput] = useState({
    name: "",
    birth: "",
    country: "",
    bio: "",
  });

  const onChange = (e)=>{
    setInput({
      ...input,
      [e.target.name] : e.target.value
    })
  }

  const onChangeName = (event) => {
    setInput({
      ...input,
      name: event.target.value,
    });
  };

  const onChangBirth = (event) => {
    setInput({
      ...input,
      birth: event.target.value,
    });
  };

  const onChangeCountry = (event) => {
    setInput({
      ...input,
      country: event.target.value,
    });
  };

  const onChangeBio = (event) => {
    setInput({
      ...input,
      bio: event.target.value,
    });
  };

  return (
    <div>
      <div>
        <input
          value={input.name}
          onChange={onChangeName}
          placeholder={"이름"}
          type="text"
        />
        {input.name}
      </div>

      <div>
        <input value={input.birth} onChange={onChangBirth} type="date" />
        {input.birth}
      </div>

      <div>
        <select value={input.country} onChange={onChangeCountry}>
          <option></option>
          <option value="kr">한국</option>
          <option value="us">미국</option>
          <option value="uk">영국</option>
        </select>
        {input.country}
      </div>

      <div>
        <textarea value={input.bio} onChange={onChangeBio} />
        {input.bio}
      </div>
    </div>
  );
};

export default Register;
