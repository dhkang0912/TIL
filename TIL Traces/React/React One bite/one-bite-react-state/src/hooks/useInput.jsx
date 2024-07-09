import { useState } from "react"

// 커스텀 훅으로 변경하는 방법 : 함수 이름 앞에 use 접두사 사용
function useInput(){
  // 리액트 컴포넌트나 커스텀 훅 내부에서만 사용 가능함
  const [input, setInput] = useState("")

  const onChange = (e)=>{
    setInput(e.target.value)}
  
  return [input, onChange]
}

export default useInput
