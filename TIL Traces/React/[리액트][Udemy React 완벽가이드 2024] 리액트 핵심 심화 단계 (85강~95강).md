## 1. [리액트][Udemy React 완벽가이드 2024] 리액트 핵심 심화 단계 (85강~95강)
- [1. \[리액트\]\[Udemy React 완벽가이드 2024\] 리액트 핵심 심화 단계 (85강~95강)](#1-리액트udemy-react-완벽가이드-2024-리액트-핵심-심화-단계-85강95강)
  - [1.1. State 관리 간소화와 불필요한 State 분별](#11-state-관리-간소화와-불필요한-state-분별)
  - [1.2. Tic-Tac-Toe 게임 프로그래밍 코드 정리](#12-tic-tac-toe-게임-프로그래밍-코드-정리)
    - [1.2.1. 코드별 해석 주석 완료](#121-코드별-해석-주석-완료)

### 1.1. State 관리 간소화와 불필요한 State 분별
```
import Player from "./components/Player"
import GameBoard from "./components/GameBoard"
import { useState } from "react"
import Log from "./components/Log"

// helper function, 데이터에 접근이 필요하지 않음, 상태가 변경될 때 변경되어야 하는 함수가 아님 
function deriveActivePlayer(gameTurns) {
  let currentPlayer = 'X'
  if (gameTurns.length > 0 && gameTurns[0].player === 'X') {
    currentPlayer = 'O'
  }

  return currentPlayer
}

function App() {
  const [gameTurns, SetGameTurns] = useState([])

  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  // const [activePlayer, setActivePlayer] = useState('X')
  const activePlayer = deriveActivePlayer(gameTurns)

  function handleSelectSquare(rowIndex, colIndex) {
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    // setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')
    SetGameTurns((prevTurns) => {
      const currentPlayer = deriveActivePlayer(prevTurns)
      const updatedTurns = [{ square: { row: rowIndex, col: colIndex }, player: currentPlayer }, ...prevTurns]

      return updatedTurns
    })
  }

  return (
    <main>
      <div id="game-container">
        {/* highlight-player라는 클래스를 추가하여 해당 class가 isActive 클래스를 가지고 있을 때 하이라이팅 될 수 있도록 설정 */}
        <ol id="players" className="highlight-player ">
          {/* 현재 symbol에 맞게 isActive를 true 또는 false로 보냄 */}
          <Player initialName="Player 1" symbol="X" isActive={activePlayer === 'X'} />
          <Player initialName="Player 2" symbol="O" isActive={activePlayer === 'O'} />
        </ol>
        {/* GameBoard 컴포넌트에서도 현재 활성화된 player의 symbol을 props로 넘겨줌 */}
        <GameBoard onSelectSquare={handleSelectSquare} turns={gameTurns} />
      </div>
      <Log turns={gameTurns} />
    </main>
  )
}

export default App

```
- activePlayer의 상태를 변경해주는 useState를 삭제하고 gameTurns의 기능을 통해 컨트롤하기 위해 helper function의 기능을 App 컴포넌트 밖에 작성했다.
- helper function은 데이터에 접근이 필요하지 않고 상태가 변경될 때 변경되어야 하는 함수가 아니기 때문에 App 컴포넌트 밖에 작성한다고 한다.
  - 이 함수는 gameTurns에 저장된 로그의 직전 player의 symbol을 기반으로 현재 player의 symbol을 알 수 있게 해주는 함수이다.

- activePlayer와 currentPlayer의 인자가 다르게 들어가야 하는 것이 이해가 되지 않아 한참 고민하고 gpt의 도움을 받았다.
  - activePlayer의 경우 렌더링될 때 gameTurns의 정보를 기반으로 현재 활성화된 player의 정보를 저장한다.
  - currentPlayer는 버튼을 눌렀을 때 버튼을 누르기 전 정보를 기반으로 버튼을 누르고 업데이트 되어야 하는 player 정보를 저장시킨다.
  => 결국 버튼을 누르면 currentPlayer의 정보를 기반으로 updatedTurns가 저장되고 다시 렌더링될 때 이 정보를 기반으로 activePlayer가 렌더링되는 것이다.
  => 이렇게 구분되어 작성되는 이유는 비동기적으로 상태가 업데이트되기 때문에 항상 최신 상태를 보장하기 위해서이다.

<br>

### 1.2. Tic-Tac-Toe 게임 프로그래밍 코드 정리
#### 1.2.1. 코드별 해석 주석 완료 

- app.jsx
```
import Player from "./components/Player"
import GameBoard from "./components/GameBoard"
import { useState } from "react"
import Log from "./components/Log"
import { WINNING_COMBINATIONS } from "./winning-combination"
import GameOver from "./components/GameOver"

// 해당 상수의 이름을 대문자로 해주는 것은 문법적으로 필수는 아니지만 일반적인 패턴
const PLAYERS =
{
  X: 'Player 1',
  O: 'Player 2'
}

// 하드코딩이 아닌 상수 변수에 할당하여 컴포넌트에서 사용할 수 있도록 해주는 것이 더 좋음
const INITIALGAMEBOARD = [
  [null, null, null],
  [null, null, null],
  [null, null, null],
]

// helper function, 데이터에 접근이 필요하지 않음, 상태가 변경될 때 변경되어야 하는 함수가 아님 
// symbol을 변경해주는 파생함수를 컴포넌트 밖에서 정의해주면서 컴포넌트 내부에서 다양한 방식으로 활용될 수 있음
function deriveActivePlayer(gameTurns) {
  let currentPlayer = 'X'
  // 직전 gameTurns의 정보가 있고 그 player의 symol을 기준으로 현재 player의 symbol을 판단함
  if (gameTurns.length > 0 && gameTurns[0].player === 'X') {
    currentPlayer = 'O'
  }

  // 매개변수를 기반으로 현재 player symbol을 반환해줌
  return currentPlayer
}

function deriveGameBoard(gameTurns) {
  // 깊은 복사를 해서 메모리 주소가 아닌 값이 복사되게 하기
  // 얕은 복사를 해서 gameBoard에 symbol을 할당하는 경우 초기화를 해도 이미 해당 메모리 주소의 내용을 변경했기 때문에 정보가 남아있게 된다.
  // 깊은 복사를 해서 메모리 주소가 아닌 값을 복사한 후 할당하기
  let gameBoard = [...INITIALGAMEBOARD.map(array => [...array])]

  // 초기값일 때는 array를 만들지 않고 값이 있을 때만 만들기 위해 반복문을 씀
  // 만약 비어있다면 반복할 게 없어서 해당 for문이 돌지 않을 것
  for (const turn of gameTurns) {
    // 중첩 객체 {{}, {}, {}} <= 이런 형식이기 때문에 한 객체씩 반복되어 풀어서 사용할 수 있도록 반복문 사용
    const { square, player } = turn
    const { row, col } = square
    // 현재 선택된 row, col 위치에 player symbol 보여주기
    gameBoard[row][col] = player
  }
  return gameBoard
}

// 현재 gameBoard의 symbol 할당 상태가 winning combiantion과 동일한지 확인하는 함수
// 매번 틱택토를 둘 때마다 확인하게 되고 기본값이 null이라 승자가 없으면 null이 나오게 됨
function deriveWinner(gameBoard, players) {
  let winner = null

  // 외부 파일인 winning-combination.js 파일에서 WINNING_COMBINATION이라는 자료를 아웃소싱해서 가져오고 있음
  for (const combination of WINNING_COMBINATIONS) {
    const firstSquareSymbol = gameBoard[combination[0].row][combination[0].column]
    const secondSquareSymbol = gameBoard[combination[1].row][combination[1].column]
    const thirdSquareSymbol = gameBoard[combination[2].row][combination[2].column]

    if (firstSquareSymbol &&
      firstSquareSymbol === secondSquareSymbol &&
      firstSquareSymbol === thirdSquareSymbol
    ) {
      winner = players[firstSquareSymbol]
    }
  }

  return winner
}

function App() {
  // player의 이름을 비동기적으로 업데이트 해줌
  const [players, setPlayers] = useState({ PLAYERS })

  // 활성화된 player의 symbol을 기록으로 남김, 가장 최신 정보가 index 0번에 항상 쌓임
  const [gameTurns, SetGameTurns] = useState([])

  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  // const [activePlayer, setActivePlayer] = useState('X')

  // 현재 player 정보를 렌더링 해줌
  const activePlayer = deriveActivePlayer(gameTurns)
  // 파생함수에 현재까지 gameTurns의 정보를 인자로 넘겨줌
  // 이때 함수에서 initial board의 초기값을 깊은 복사해와서 동일한 새로운 board를 만들어주고 저장되어있는 로그를 for문으로 돌면서 해당 로그의 정보를 board에 나타내줌
  const gameBoard = deriveGameBoard(gameTurns)

  // winner가 있는지 매번 확인하기
  const winner = deriveWinner(gameBoard, players)
  // 무승부인지 확인하기 => 9개 배열이 모두 다 차있지만, winner가 없으면 무승부
  const hasDraw = gameTurns.length === 9 && !winner

  function handleSelectSquare(rowIndex, colIndex) {
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    // setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')

    // 버튼 클릭 시 과거의 gameTurns를 기반으로 변경될 gameTurns의 내용들로 업데이트를 해줌
    SetGameTurns((prevTurns) => {
      const currentPlayer = deriveActivePlayer(prevTurns)
      const updatedTurns = [{ square: { row: rowIndex, col: colIndex }, player: currentPlayer }, ...prevTurns]
      console.log(updatedTurns)
      return updatedTurns
    })
  }

  // Rematch 버튼 클릭 시 gameTurns의 정보를 빈 배열로 초기화해줌
  function handleRestart() {
    SetGameTurns([])
  }

  // player의 이름을 변경해주는 기능
  function handlePlayerNameChange(symbol, newName) {
    setPlayers((prevPlayers) => {
      return {
        ...prevPlayers,
        // 동적인 자바스크립트 변수명 사용하기
        [symbol]: newName
      }
    })
  }

  return (
    <main>
      <div id="game-container">
        {/* highlight-player라는 클래스를 추가하여 해당 class가 isActive 클래스를 가지고 있을 때 하이라이팅 될 수 있도록 설정 */}
        <ol id="players" className="highlight-player ">
          {/* 현재 symbol에 맞게 isActive를 true 또는 false로 보냄 */}
          <Player initialName={PLAYERS.X} symbol="X" isActive={activePlayer === 'X'} onChangeName={handlePlayerNameChange} />
          <Player initialName={PLAYERS.O} symbol="O" isActive={activePlayer === 'O'} onChangeName={handlePlayerNameChange} />
        </ol>
        {/* winner가 있거나, Draw가 되면 winner와 restart 함수를 props로 넘겨주기 */}
        {(winner || hasDraw) && <GameOver winner={winner} onRestart={handleRestart} />}
        {/* GameBoard 컴포넌트에서도 현재 활성화된 player의 symbol을 props로 넘겨줌 */}
        <GameBoard onSelectSquare={handleSelectSquare} board={gameBoard} />
      </div>
      <Log turns={gameTurns} />
    </main>
  )
}

export default App

```

- Player.jsx
```
import { useState } from "react"

// isActive 클래스를 true, false로 받음
export default function Player({ initialName, symbol, isActive, onChangeName }) {
    // 초기값을 매개변수로 받고, 그 이후는 useState를 통해서 변경된 값과, 변경 값을 적용할 함수를 지정
    const [playerName, setPlayerName] = useState(initialName)
    const [isEditing, setIsEditing] = useState(false)
    function handleEditClick (){
        // 삼항연산자를 통해서 isEditing이 true면 false로 바꾸고, false면 true로 바꿈
        // setIsEditing(isEditing ? false : true)
        // !을 통해 값을 반대로 반전함

        setIsEditing((editing)=>!editing)
        // 현재 수정 중이라면 
        if (isEditing) {
            // 입력 받은 playerName을 통해 playername 변경
            onChangeName(symbol, playerName )
        }
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

