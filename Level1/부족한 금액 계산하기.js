function solution(price, money, count) {
    let cnt_sum = 0;
    for (var i = 1; i < count + 1; i++) {
        cnt_sum += i;
    }
    return price * cnt_sum < money ? 0 : price * cnt_sum - money;
}
