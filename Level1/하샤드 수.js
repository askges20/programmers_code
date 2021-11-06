function solution(x) {
    return !(x % (x + '').split('').reduce((a, b) => +a + +b));
}
