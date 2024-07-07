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
