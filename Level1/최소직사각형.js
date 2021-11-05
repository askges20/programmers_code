function solution(sizes) {
    let big = [], small = [];
    for (let s of sizes) {
        big.push(Math.max(...s));
        small.push(Math.min(...s));
    }
    return Math.max(...big) * Math.max(...small);
}
