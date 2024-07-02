## [리액트][Udemy React 완벽가이드 2024] 리액트 핵심 심화 단계 (79강~81강)
> 오늘 github를 clone 받으면서 해당 내용을 맥북에서만 push, pull 해서 모르고 있었으나 window에서는 파일 명에 :가 들어가면 오류가 난다는 것을 알게 됐다.
리액트 정리한 내용을 md 파일로 github에 올리고 있어서 이번에 알게 돼서 기록으로 남긴다.

### 불변 State(상태)로 업데이트하기
```
import { useState } from "react"

const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null],
]

export default function GameBoard() {
    // 직접적으로 원본 배열을 수정하는 것을 지양해야함, 자바스크립트에서 원본 배열, 
    // 객체를 수정하는 경우 메모리에 참조된 내용을 변경하는 것인데 이 경우 순서가 원하는 대로 되지 않고 리액트가 실행하는 예정된 상태보다 먼저 업데이트가 됨
    const [gameBoard, setGameBoard] = useState(initialGameBoard)

    function handleSelectSquare(rowIndex, colIndex){
        setGameBoard((prevGameBoard)=>{
            // 이렇게 하면 이전에 가지고 있던 정보를 그대로 가지고 있지만 새로운 배열이 됨, 상태를 변경 불가능하게 업데이트하게 됨
            const updatedBoard = [...prevGameBoard.map((innerArray)=>[...innerArray])]
            updatedBoard[rowIndex][colIndex] = 'X'
            return updatedBoard
        })
    }

    return (
        <ol id="game-board">
            {gameBoard.map((row, rowIndex) => (
                <li key={rowIndex}>
                    <ol>
                        {row.map((playerSymbol, colIndex) => (
                            <li key={colIndex}>
                                <button onClick={()=>handleSelectSquare(rowIndex, colIndex)}>{playerSymbol}</button>
                            </li>
                        ))}
                    </ol>
                </li>
            ))}
        </ol>
    )
}
```
내용이 점점 어려워진다... 이 부분은 이해하기 더 어려웠다.
- 위 코드는 3*3 배열에서 클릭된 부분만 우선 X 표시를 하게 만드는 코드이다
- 주의점
  1. 버튼을 클릭했을 때 실행되는 함수에서 row, col index를 알아야 하기 때문에 익명함수로 작성하여 인자를 가질 수 있게 한다
  2. 버튼 클릭 시 gameBoard의 상태를 변경해줄 수 있도록 useState를 사용한다. 초기값은 initialGameBoard으로 지정한다.
  3. setGameBoard에 prevGameBoard를 매개변수로 갖게 되지만 새로운 GameBoard 변수를 만들고 여기에 스프레드 연산자를 활용하여 기존 배열의 정보를 가진 새로운 배열을 만들어준다.
    - 이렇게 하는 이유는 원본을 가지고 변경하는 경우 얕은 복사가 되어 원본이 변경될 수 있기 때문이다.

- ```setGameBoard((prevGameBoard)=>{어쩌구})``` 하는 구조가 어떻게 가능한가 싶었더니 useState에서 setState를 콜백함수로 사용할 때 쓸 수 있는 구조였다. 매개변수에 자동으로 과거 값이 들어가고 이를 기반으로 새로운 값을 return 하여 사용할 수 있나보다.
  - 참고 자료 : https://velog.io/@my_suwan/useState%EC%97%90%EC%84%9C-setState%EC%9D%98-%EC%BD%9C%EB%B0%B1%ED%95%A8%EC%88%98


### State(상태) 끌어올리기
> - 변경된 내용이 많고 코드 없이 설명이 안 될 것 같아서 코드에 주석을 달아서 설명을 적었다.
- Lifting State Up(상태 끌어올리기)에 대해 배웠다.
  - 상태 끌어올리기란 : 여러 컴포넌트에서 동일한 상태를 알고 있어야 하는 경우 가장 부모가 되는 컴포넌트에서 상태를 변경해주고 이에 대한 정보를 props로 내려주는 것이다.

1. App.jsx

```
function App() {
  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  const [activePlayer, setActivePlayer] = useState('X')

  function handleSelectSquare(){
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')
  }

  return (
    <main>
      <div id="game-container">
        {/* highlight-player라는 클래스를 추가하여 해당 class가 isActive 클래스를 가지고 있을 때 하이라이팅 될 수 있도록 설정 */}
        <ol id="players" className="highlight-player ">
          {/* 현재 symbol에 맞게 isActive를 true 또는 false로 보냄 */}
          <Player initialName="Player 1" symbol="X" isActive={activePlayer==='X'}/>
          <Player initialName="Player 2" symbol="O" isActive={activePlayer==='O'}/>
        </ol>
        {/* GameBoard 컴포넌트에서도 현재 활성화된 player의 symbol을 props로 넘겨줌 */}
        <GameBoard onSelectSquare={handleSelectSquare} activePlayerSymbol={activePlayer}/>
      </div>
      LOG
    </main>
  )
}

export default App

```

2. Player.jsx
```
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
```

3. GameBoard.jsx
```
import { useState } from "react"

const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null],
]

// activePlayerSymbol을 매개변수로 받아서 현재 활성화된 symbol의 정보를 가져옴
export default function GameBoard({onSelectSquare, activePlayerSymbol }) {
    // 직접적으로 원본 배열을 수정하는 것을 지양해야함, 자바스크립트에서 원본 배열, 
    // 객체를 수정하는 경우 메모리에 참조된 내용을 변경하는 것인데 이 경우 순서가 원하는 대로 되지 않고 리액트가 실행하는 예정된 상태보다 먼저 업데이트가 됨
    const [gameBoard, setGameBoard] = useState(initialGameBoard)

    function handleSelectSquare(rowIndex, colIndex){
        setGameBoard((prevGameBoard)=>{
            // 이렇게 하면 이전에 가지고 있던 정보를 그대로 가지고 있지만 새로운 배열이 됨, 상태를 변경 불가능하게 업데이트하게 됨
            const updatedBoard = [...prevGameBoard.map((innerArray)=>[...innerArray])]
            // 현재 활성화된 symbol을 클릭된 보드 영역에 입력함
            updatedBoard[rowIndex][colIndex] = activePlayerSymbol 
            return updatedBoard
        })
        onSelectSquare()
    }

    return (
        <ol id="game-board">
            {gameBoard.map((row, rowIndex) => (
                <li key={rowIndex}>
                    <ol>
                        {row.map((playerSymbol, colIndex) => (
                            <li key={colIndex}>
                                <button onClick={()=>handleSelectSquare(rowIndex, colIndex)}>{playerSymbol}</button>
                            </li>
                        ))}
                    </ol>
                </li>
            ))}
        </ol>
    )
}
```
