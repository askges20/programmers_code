def solution(s):
    if len(s) == 1:
        return 1
    
    lens = []
    for c in range(1, len(s)//2 + 1):
        result = ''
        cnt = 1
        cur = s[:c]
        
        for i in range(c, len(s), c):
            if s[i:i+c] == cur:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + cur
                cnt = 1
                cur = s[i:i+c]
                
        if cnt == 1:
            cnt = ''
        result += str(cnt) + cur
        lens.append(len(result))
        
    return min(lens)
