import { useState } from "react"

// isActive 클래스를 true, false로 받음
export default function Player({ initialName, symbol, isActive }) {
    // 초기값을 매개변수로 받고, 그 이후는 useState를 통해서 변경된 값과, 변경 값을 적용할 함수를 지정
    const [playerName, setPlayerName] = useState(initialName)
    const [isEditing, setIsEditing] = useState(false)
    function handleEditClick (){
        // 삼항연산자를 통해서 isEditing이 true면 false로 바꾸고, false면 true로 바꿈
        // setIsEditing(isEditing ? false : true)
        // !을 통해 값을 반대로 반전함
        setIsEditing((editing)=>!editing)
    }

    function handleChange(event){
        // 변경되는 이벤트가 있을 때마다 함수가 실행되고, 변경된 내용이 event.target.value에 저장됨
        // 해당 내용을 setPlayerName에 넣어서 상태를 변경해줌
        console.log(event)
        setPlayerName(event.target.value)
    }

    let editablePlayerName = <span className="player-name">{playerName}</span>
    // let btnCaption = "Edit"

    if (isEditing) {
        // input 창에서 value 값이 변경이 있을 때마다 handleChange란 함수를 실행
        editablePlayerName = <input type="text" required value={playerName} onChange={handleChange}/>
        // btnCaption="Save"
    }

    return (
        // 삼항연산자를 통해서 isActive가 true라면 해당 className을 active하고 그렇지 않다면 undefined를 통해 나타나지 않게 함
            <li className={isActive ? 'active' : undefined}>
                <span id="player">
                    {editablePlayerName}
                    <span className="player-symbol">{symbol}</span>
                </span>
                {/* <button onClick={handleEditClick}>{btnCaption}</button> */}
                <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
            </li>
        )
}