function solution(left, right) {
    let sum = 0;
    for (let n = left; n <= right; n++) {
        if (Number.isInteger(Math.sqrt(n))) {
            sum -= n;
        } else {
            sum += n;
        }
    }
    return sum;
}

//제곱근이 정수면 약수의 개수가 홀수이다.
