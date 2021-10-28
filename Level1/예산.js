function solution(d, budget) {
    d.sort((a, b) => a - b);
    let sum = d.reduce((a, b) => a + b, 0);
    while (sum > budget)
        sum -= d.pop();
    return d.length;
}

// 숫자끼리 비교할땐 sort 안에 조건 필수
// reduce 쓸때 초깃값 줄 수 있음
// 배열 맨 마지막 값 꺼낼 때는 pop 이용, 첫번째 값 꺼낼 때는 shift 이용
