def solution(w,h):
    x, y = max(w, h), min(w, h)
    while(y): #최대공약수 x
        x, y = y, x % y
    return w * h - (w + h - x)
