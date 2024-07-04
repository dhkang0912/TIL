import Player from "./components/Player"
import GameBoard from "./components/GameBoard"
import { useState } from "react"
import Log  from "./components/Log"

function App() {
  const [gameTurns, SetGameTurns] = useState([])

  // activePlayer의 symbol이 필요한 곳이 여러 컴포넌트여서 이게 필요한 가장 상위의 컴포넌트에서 변화를 감지하고 이를 props로 내려줌
  // 해당 변화의 가장 상단은 App.jsx
  const [activePlayer, setActivePlayer] = useState('X')

  function handleSelectSquare(rowIndex, colIndex ){
    // 기본적으로 플레이어의 symbol 초기값은 X로 만약 X가 아닌 경우 O로 바꿔주는 코드
    setActivePlayer((curActivePlayer)=>curActivePlayer==='X' ? 'O' : 'X')
    SetGameTurns((prevTurns)=>{
      let currentPlayer = 'X'
      if (prevTurns.length > 0 && prevTurns[0].player === 'X') {
        currentPlayer = 'O'
      }
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
