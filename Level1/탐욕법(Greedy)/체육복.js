function solution(n, lost, reserve) {
    lost = lost.sort();
    reserve = reserve.sort();
    lost = lost.filter(l => {
        if (reserve.includes(l)) {
            reserve.splice(reserve.indexOf(l), 1);
            return false;
        }
        return true;
    })
    return n - lost.filter(l => {
        if (reserve.includes(l - 1)) {
            reserve.splice(reserve.indexOf(l - 1), 1);
            return false;
        } else if (reserve.includes(l + 1)) {
            reserve.splice(reserve.indexOf(l + 1), 1);
            return false;
        } else {
            return true;
        }
    }).length;
}

// 파이썬에서는 set형을 이용했는데 js에는 없어서 filter로 걸러냈음
