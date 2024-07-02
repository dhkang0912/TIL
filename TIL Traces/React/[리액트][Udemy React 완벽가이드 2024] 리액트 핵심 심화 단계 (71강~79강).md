## [리액트][Udemy React 완벽가이드 2024] - 리액트 핵심 심화 단계 (71강~79강)
### 개념복습 : state 활용법
```
import { useState } from "react"

export default function Player({ name, symbol }) {
    const [isEditing, setIsEditing] = useState(false)
    function handleEditClick (){
        setIsEditing(true)
    }

    let playerName = <span className="player-name">{name}</span>

    if (isEditing) {
        playerName = <input type="text" required/>
    }

    return (
            <li>
                <span id="player">
                    {playerName}
                    <span className="player-symbol">{symbol}</span>
                </span>
                <button onClick={handleEditClick}>Edit</button>
            </li>
        )
}
```

- edit 버튼을 누르면 수정할 내용을 입력할 수 있는 입력 칸이 나와야 함, 그 전까지는 기존 가지고 있는 player name이 보여져야 함
  - useState를 통해서 새로고침없이 수정 시 변화를 감지하여 해당 내용이 렌더링되게 할 수 있음
  - useState는 값과 변경하는 함수를 담은 배열을 반환함
  - button 태그에 onClick 이벤트 시 활성화될 함수를 작성해주고 이 함수에는 setIsEditing 함수의 값을 true로 넣어주면서 isEditing 값을 변경할 수 있게 해줌

- jsx 코드를 변수화할 수 있기 때문에 playerName으로 변수화하여 isEditing 상태에 따라(if문 활용) player name을 보여줄지, input 창을 보여줄지 작성
  - 처음엔 Player1이라는 문구를 보여주지만 Edit을 클릭 시 input 창을 보여줌
  

### 컴포넌트 인스턴스의 분리된 동작법
- 동일한 컴포넌트에 다른 내용이 있는 경우, 사용된 컴포넌트는 동일하지만 각각 다른 인스턴스를 생성하고 서로 영향을 미치지 않음

### 조건적 컨텐츠, State 업데이트를 위한 차선책
```
import { useState } from "react"

export default function Player({ name, symbol }) {
    const [isEditing, setIsEditing] = useState(false)
    function handleEditClick (){
        // 삼항연산자를 통해서 isEditing이 true면 false로 바꾸고, false면 true로 바꿈
        // setIsEditing(isEditing ? false : true)
        // !을 통해 값을 반대로 반전함
        setIsEditing(!isEditing)
    }

    let playerName = <span className="player-name">{name}</span>
    // let btnCaption = "Edit"

    if (isEditing) {
        playerName = <input type="text" required value={name}/>
        // btnCaption="Save"
    }

    return (
            <li>
                <span id="player">
                    {playerName}
                    <span className="player-symbol">{symbol}</span>
                </span>
                {/* <button onClick={handleEditClick}>{btnCaption}</button> */}
                <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
            </li>
        )
}
```
- Edit, Save 글씨를 상태에 맞게 표현하기 위해 isEditing State를 통해서 삼항연산자로 표현
- handleEditClick 함수를 통해 클릭 시 isEditing 상태를 반전시켜 각 상태에 맞게 버튼의 글씨를 보여줌

### 옛 State 기반으로 올바르게 업데이트하기
```
import { useState } from "react"

export default function Player({ name, symbol }) {
    const [isEditing, setIsEditing] = useState(false)
    function handleEditClick (){
        // 삼항연산자를 통해서 isEditing이 true면 false로 바꾸고, false면 true로 바꿈
        // setIsEditing(isEditing ? false : true)
        // !을 통해 값을 반대로 반전함
        setIsEditing((editing)=>!editing)
    }

    let playerName = <span className="player-name">{name}</span>
    // let btnCaption = "Edit"

    if (isEditing) {
        playerName = <input type="text" required value={name}/>
        // btnCaption="Save"
    }

    return (
            <li>
                <span id="player">
                    {playerName}
                    <span className="player-symbol">{symbol}</span>
                </span>
                {/* <button onClick={handleEditClick}>{btnCaption}</button> */}
                <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
            </li>
        )
}
```
- 위의 코드처럼 ```setIsEditing(!isEditing)```을 통해 업데이트하는 것을 리액트는 권장하지 않음, 이렇게 업데이트 하는 경우 처음 자바스크립트가 렌더링된 기본값을 기준으로 업데이트가 됨
  - 추가적으로 ```setIsEditing(!isEditing)```로 업데이트를 하는 경우 동시에 한번 더 ```setIsEditing(!isEditing) setIsEditing(!isEditing)``` 처리를 시켰을 때 정상적으로 작동되지 않음
  => 왜 그런가? : 첫번째 setIsEditing(!isEditing)를 처리하는데 시간이 약간 지연됨, 이 지연되는 시간동안 두번째 setIsEditing(!isEditing)가 처리됨 
  => 결론적으로 원하는 결과가 나오지 않음
  

- 이 경우에 정상적으로 처리를 하기 위해서는 함수로 받아서 처리해야 가장 최신 내용을 받아올 수 있음 ```setIsEditing(editing=>!editing)```로 작성해야함
- 함수를 사용하여 변경하면 매개변수가 항상 가장 최신 상태 <= 리액트가 보장함

### 사용자 입력과 양방향 바인딩
```
import { useState } from "react"

export default function Player({ initialName, symbol }) {
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
            <li>
                <span id="player">
                    {editablePlayerName}
                    <span className="player-symbol">{symbol}</span>
                </span>
                {/* <button onClick={handleEditClick}>{btnCaption}</button> */}
                <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
            </li>
        )
}
```
- 리액트에서 input을 통해 양방향 바인딩을 설정하는 방법
  - 변경이 일어나는 곳에 이벤트 핸들러인 onChange를 설정해주고, 변경될 때마다 실행할 함수를 할당
  - 함수에는 useState를 통해서 변경된 값을 실시간으로 반영될 수 있도록 매개변수와 함수를 지정
  - input에서 이벤트 발생 시 event.target.value에 해당 값을 저장함
  - 이 값을 useState의 값 변경 함수의 인자로 들어가게 넣어줌
  - 변경이 일어날 때마다 playerName은 상태값이 변경될 것이고 이를 화면에 보여주도록 렌더링함
  
### 다차원 리스트 렌더링
```
const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null],
]

export default function GameBoard() {
    return (
        <ol id="game-board">
            {initialGameBoard.map((row, rowIndex) => (
                <li key={rowIndex}>
                    <ol>
                        {row.map((playerSymbol, colIndex) => (
                            <li key={colIndex}>
                                <button>{playerSymbol}</button>
                            </li>
                        ))}
                    </ol>
                </li>
            ))}
        </ol>
    )
}
```
- 2차원 배열을 통해 3*3 좌표를 생성
  - 안의 요소들은 map을 통해서 처음엔 row를 표현하고, row를 또 map으로 표현하여 col을 접근함