import useInput from "../hooks/useInput"

// 3가지 hook 관련된 팁
// 1. 함수 컴포넌트, 커스텀 훅 내부에서만 호출 가능
// 2. 조건부로 호출될 수는 없다. => 호출 순서가 꼬이면서 내부적인 순서가 엉망이 될 수 있음, 컨퍼런스 함수 안에서만 사용 가능
// 3. 나만의 훅(Custom Hook)을 직접 만들 수 있다.


const HookExam = ()=>{
  const [input, onChange] = useInput()
  const [input2, onChange2] = useInput()

  return (
  <div>
    <input value={input} type="text" onChange={onChange} />
    <input value={input2} type="text" onChange={onChange2} />
    {input}
    {input2}
  </div>

  )}

export default HookExam