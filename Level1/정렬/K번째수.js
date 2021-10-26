function solution(array, commands) {
    return commands.map(c => {
        return array.slice(c[0] - 1, c[1]).sort((x, y) => x - y)[c[2] - 1];
    });
}

// sort - 문자열의 유니코드 포인트를 따라서 정렬한다.
// 따라서 sort 안에 조건이 없으면 문자열로 비교하게 되고 원하는 결과가 나오지 않는다.
