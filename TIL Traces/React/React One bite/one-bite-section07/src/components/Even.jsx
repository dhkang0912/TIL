import { useEffect } from "react"

const Even = ()=>{
    useEffect(()=>{
        // useEffect가 반환하는 함수를 클린업, 정리함수라고 함
        // useEffect가 끝날 때 실행됨
        // deps를 빈 배열로 주면 mount 됐을 때 useEffect가 실행되고 mount가 끝날 때 return 되는 클린업, 정리함수가 실행됨
        return ()=>{
            console.log("unmount")
        }
    },[])

    return <div>짝수입니다.</div>
}

export default Even