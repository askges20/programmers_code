function solution(n)
{
    return n < 10 ? n : ("" + n).split("").reduce((a, b) => parseInt(a) + parseInt(b));
}
