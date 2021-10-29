function solution(arr)
{
    return arr.filter((n, i) => arr[i + 1] != n);
}
