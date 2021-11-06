function solution(record) {
    let result = [];
    let id_nick = {};
    for (let r of record) {
        let r_split = r.split(' ');
        if (r_split[0] === 'Enter') {
            result.push(r_split[1] + '/님이 들어왔습니다.');
            id_nick[r_split[1]] = r_split[2];
        } else if (r_split[0] === 'Leave') {
            result.push(r_split[1] + '/님이 나갔습니다.');
        } else {
            id_nick[r_split[1]] = r_split[2];
        }
    }
    for (let i = 0; i < result.length; i++) {
        let cur = result[i];
        result[i] = id_nick[cur.split('/')[0]] + cur.split('/')[1]
    }
    return result;
}
