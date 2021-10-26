function isPrime(sum) {
    if (sum < 2)
        return false;
    for (let cur = 2; cur < sum; cur++) {
        if (sum % cur === 0)
            return false;
    }
    return true;
}

function solution(nums) {
    let cnt = 0;
    for (let i = 0; i < nums.length; i++) {
        let a = nums[i];
        for (let j = i + 1; j < nums.length; j++) {
            let b = nums[j];
            for (let k = j + 1; k < nums.length; k++) {
                let c = nums[k];
                if (isPrime(a + b + c))
                    cnt += 1;
            }
        }
    }
    return cnt;
}

// 파이썬에서는 combinations가 있는데 js에는 없어서 3중 for문 돌림...
