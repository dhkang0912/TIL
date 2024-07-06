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

const INITIALGAMEBOARD = [
  [null, null, null],
  [null, null, null],
  [null, null, null],
]

// helper function, 데이터에 접근이 필요하지 않음, 상태가 변경될 때 변경되어야 하는 함수가 아님 
function deriveActivePlayer(gameTurns) {
  let currentPlayer = 'X'
  if (gameTurns.length > 0 && gameTurns[0].player === 'X') {
    currentPlayer = 'O'
  }

  return currentPlayer
}

function deriveGameBoard(gameTurns) {
  // 깊은 복사를 해서 메모리 주소가 아닌 값이 복사되게 하기
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

function deriveWinner(gameBoard, players) {
  let winner = null

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
  const [players, setPlayers] = useState({ PLAYERS })

  const [gameTurns, SetGameTurns] = useState([])

  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  // const [activePlayer, setActivePlayer] = useState('X')
  const activePlayer = deriveActivePlayer(gameTurns)
  const gameBoard = deriveGameBoard(gameTurns)
  const winner = deriveWinner(gameBoard, players)
  const hasDraw = gameTurns.length === 9 && !winner

  function handleSelectSquare(rowIndex, colIndex) {
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    // setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')
    SetGameTurns((prevTurns) => {
      const currentPlayer = deriveActivePlayer(prevTurns)
      const updatedTurns = [{ square: { row: rowIndex, col: colIndex }, player: currentPlayer }, ...prevTurns]
      console.log(updatedTurns)
      return updatedTurns
    })
  }

  function handleRestart() {
    SetGameTurns([])
  }

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
        {(winner || hasDraw) && <GameOver winner={winner} onRestart={handleRestart} />}
        {/* GameBoard 컴포넌트에서도 현재 활성화된 player의 symbol을 props로 넘겨줌 */}
        <GameBoard onSelectSquare={handleSelectSquare} board={gameBoard} />
      </div>
      <Log turns={gameTurns} />
    </main>
  )
}

export default App
