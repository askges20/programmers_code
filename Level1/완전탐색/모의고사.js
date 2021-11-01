function solution(answers) {
    let one = [1,2,3,4,5];
    let two = [2,1,2,3,2,4,2,5];
    let three = [3,3,1,1,2,2,4,4,5,5];
    let scores = [0,0,0];
    let answer = [];
    
    scores[0] = answers.filter((value, idx) => value === one[idx%one.length]).length;
    scores[1] = answers.filter((value, idx) => value === two[idx%two.length]).length;
    scores[2] = answers.filter((value, idx) => value === three[idx%three.length]).length;
    
    let max_score = Math.max.apply(null, scores);
    for (let i = 0; i < 3; i++) {
        if (scores[i] === max_score) {
            answer.push(i + 1);
        }
    }
    
    return answer;
}
