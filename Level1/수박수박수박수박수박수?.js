function solution(n) {
    return "수박".repeat(n/2) + (n % 2 === 0 ? "" : "수");
}

// repeat를 이용해서 문자열 반복 출력하기
