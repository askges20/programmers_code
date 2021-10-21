function solution(numbers, hand) {
    let left = [1,4,7,10]
    let right = [3,6,9,12]
    let cur_left = 10
    let cur_right = 12
    let result = ''
    
    numbers.forEach((value, index, array) => {
        if (left.includes(value)) {
            result += 'L'
            cur_left = value
        } else if (right.includes(value)) {
            result += 'R'
            cur_right = value
        } else {
            if (value === 0) {
                value = 11
            }
            
            let left_dist = Math.floor(Math.abs(value - cur_left) / 3) + Math.floor(Math.abs(value - cur_left) % 3)
            let right_dist = Math.floor(Math.abs(value - cur_right) / 3) + Math.floor(Math.abs(value - cur_right) % 3)
            
            if (left_dist > right_dist) {
                result += 'R'
                cur_right = value
            } else if (left_dist < right_dist) {
                result += 'L'
                cur_left = value
            } else {
                if (hand === 'left') {
                    result += 'L'
                    cur_left = value
                } else {
                    result += 'R'
                    cur_right = value
                }
            }
        }
    })
    return result
}

//JS에서 //는 주석이므로 Math.abs와 Math.floor을 이용해서 구함
