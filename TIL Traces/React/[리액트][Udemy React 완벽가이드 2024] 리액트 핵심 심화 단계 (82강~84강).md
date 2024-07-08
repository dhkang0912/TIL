## [리액트][Udemy React 완벽가이드 2024] 리액트 핵심 심화 단계 (82강~84강)
### 목차
- [\[리액트\]\[Udemy React 완벽가이드 2024\] 리액트 핵심 심화 단계 (82강~84강)](#리액트udemy-react-완벽가이드-2024-리액트-핵심-심화-단계-82강84강)
  - [목차](#목차)
  - [Props에서 State 파생하기](#props에서-state-파생하기)

### Props에서 State 파생하기
- App.jsx
```
import Player from "./components/Player"
import GameBoard from "./components/GameBoard"
import { useState } from "react"
import Log  from "./components/Log"

function App() {
  // Game turn과 현재 Player symbol을 저장하기 위해 사용
  const [gameTurns, SetGameTurns] = useState([])

  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  const [activePlayer, setActivePlayer] = useState('X')

  function handleSelectSquare(rowIndex, colIndex ){
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')
    // Game turn과 현재 Player symbol을 상태 변경해주기
    SetGameTurns((prevTurns)=>{
      // 기본적으로 현재 player의 symbol을 X로 설정, 초기값
      let currentPlayer = 'X'
      // 만약 prevTurns가 있고, 이전 턴의 player symbol이 X면 현재 player symbol을 O로 변경
      if (prevTurns.length > 0 && prevTurns[0].player === 'X') {
        currentPlayer = 'O'
      }
      // 내용 업데이트 해주고 반환하기
      const updatedTurns = [{square : {row : rowIndex, col : colIndex}, player : activePlayer},...prevTurns]

      return updatedTurns
    })
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
        <GameBoard onSelectSquare={handleSelectSquare} turns={gameTurns}/>
      </div>
      <Log/>
    </main>
  )
}

export default App

```

- GameBoard.jsx
```
const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null],
]

// activePlayerSymbol을 매개변수로 받아서 현재 활성화된 symbol의 정보를 가져옴
export default function GameBoard({onSelectSquare, turns }) {
    let gameBoard = initialGameBoard

    // 초기값일 때는 array를 만들지 않고 값이 있을 때만 만들기 위해 반복문을 씀
    // 만약 비어있다면 반복할 게 없어서 해당 for문이 돌지 않을 것
    for (const turn of turns){
        // 중첩 객체 {{}, {}, {}} <= 이런 형식이기 때문에 한 객체씩 반복되어 풀어서 사용할 수 있도록 반복문 사용
        const {square, player} = turn
        const {row, col} = square 
        // 현재 선택된 row, col 위치에 player symbol 보여주기
        // gameTurns의 상태를 기반으로 계산해서 파생시킨 파생 상태
        gameBoard[row][col] = player
    }

    return (
        <ol id="game-board">
            {/* map method는 배열을 반복하여 풀어주며, 인덱스를 함께 반환할 수 있다 (반복하여 풀린 요소, 인덱스) */}
            {gameBoard.map((row, rowIndex) => (
                <li key={rowIndex}>
                    <ol>
                        {row.map((playerSymbol, colIndex) => (
                            <li key={colIndex}>
                                <button onClick={()=>{onSelectSquare(rowIndex, colIndex)}}>{playerSymbol}</button>
                            </li>
                        ))}
                    </ol>
                </li>
            ))}
        </ol>
    )
}
```
- GameBoard는 gameTurns의 상태를 기반으로 계산해서 나오는 파생 상태