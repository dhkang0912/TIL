// export default function TabButton ({label}){
//     return <li><button>{label}</button></li>
// }

// export default function TabButton ({children}){
//     function handleClick(){
//         console.log("Hello World")
//     }
//     // 이벤트를 추가할 때도 prop을 넣어줌
//     // on~은 prop을 추가하는 것으로 함수로 작성해야함
//     // 함수 값을 넣고 싶기 때문에 소괄호를 넣으면 안되고 함수 이름만 작성해야함 
//     return <li><button onClick={handleClick}>{children}</button></li>
// }

export default function TabButton({ children, isSelected, ...props }) {

    // 이벤트를 추가할 때도 prop을 넣어줌
    // on~은 prop을 추가하는 것으로 함수로 작성해야함
    // 함수 값을 넣고 싶기 때문에 소괄호를 넣으면 안되고 함수 이름만 작성해야함 
    // jsx에서 class를 넣을 때는 className 속성을 통해 넣음
    // 삼항연산자를 통해 해당 요소가 선택됐을 때만 활성화할 수 있음
    return <li><button className={isSelected ? 'active' : undefined} {...props}>
            {children}
        </button></li>
}