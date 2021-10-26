// 자바스크립트 배열 숫자 더하는 방법 3가지

// 1. for문
function solution(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i]
    }
    return 45 - sum;
}

// 2. forEach문
function solution(numbers) {
    let sum = 0;
    numbers.forEach((item) => {
        sum += item
    })
    return 45 - sum;
}

// 3. reduce 이용
/*
배열.reduce((누적값, 현잿값, 인덱스, 원배열) => {
  return 결과
}, 초깃값);
*/
function solution(numbers) {
    return 45 - numbers.reduce((a,b) => a + b)
}

// 해당 문제에서는 1 3 2 순으로 빨랐음
