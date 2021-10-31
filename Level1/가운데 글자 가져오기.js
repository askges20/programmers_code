function solution(s) {
    return s.substr(Math.ceil(s.length/2) - 1, s.length % 2 === 0 ? 2 : 1);
}

// substr로 시작 인덱스, 길이 지정 가능
