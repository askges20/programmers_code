function solution(board, moves) {
    let basket = [];
    let answer = 0;
    moves.forEach((n) => {
        for (let i = 0; i < board.length; i++) {
            if (board[i][n - 1] != 0) {
                basket.push(board[i][n - 1]);
                board[i][n - 1] = 0;
                break;
            }
        }
        if (basket.length >= 2) {
            if (basket.slice(-2)[0] == basket.slice(-1)[0]) {
                answer += 2;
                basket = basket.slice(0, basket.length - 2);
            }
        }
    })
    return answer;
}

// 배열에 값 추가할 때 - push 이용
// 파이썬 인덱싱, 슬라이싱 - slice 이용 (ex. 파이썬 basket[-2] -> 자바스크립트 basket.slice(-2)[0])
