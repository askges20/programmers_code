def solution(n, m): #유클리드 호제법
    x, y = n, m
    while(y): #최대공약수 x
        x, y = y, x % y
    gcd = (n * m) // x #최소공배수 gcd
    return [x, gcd]
