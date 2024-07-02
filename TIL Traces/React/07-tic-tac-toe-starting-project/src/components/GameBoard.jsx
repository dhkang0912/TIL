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