function solution(n) {
    return parseInt(n.toString(3).split("").reverse().join(""), 3);
}

// toString을 이용하여 10진수를 다른 진수로 변환하기
// split -> reverse -> join을 거쳐서 문자열 뒤집기
// parseInt를 이용하여 10진수로 변환하기 ( parseInt(변환할 수, 현재 진수) )
