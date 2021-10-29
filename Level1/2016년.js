function solution(a, b) {
    let max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    if (a === 1)
        return days[b % 7]
    else {
        return days[(max_day.slice(0, a - 1).reduce((x, y) => x + y) + b) % 7]
    }
}
