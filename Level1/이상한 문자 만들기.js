function solution(s) {
    let isEven = false;
    let answer = "";
    for (let w of s) {
        if (w === " ") {
            answer += " ";
            isEven = false;
        }
        else if (isEven) {
            answer += w.toLowerCase();
            isEven = false;
        } else {
            answer += w.toUpperCase();
            isEven = true;
        }
    }
    return answer;
}
