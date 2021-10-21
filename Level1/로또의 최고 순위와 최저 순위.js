// 기존에 python으로 풀었던 문제 js로 풀어보기

function solution(lottos, win_nums) {
    var cnt_zero = lottos.filter(e => e === 0).length
    var cnt_match = 0
    lottos.forEach((value, index, array) => {
        if (win_nums.includes(value)) {
            cnt_match += 1
        }
    })
    return [Math.min(6, 7 - (cnt_match + cnt_zero)), Math.min(6, 7 - cnt_match)]
}

//1. count 대신 filter과 length
//2. for-in 대신 forEach
//3. in 대신 includes
//4. min은 Math.min으로
