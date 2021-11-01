function solution(a, b) {
    return a.reduce((sum, cur, idx) => sum + cur * b[idx], 0);
}
