def solution(s):
    answer = ""
    isEven = True
    for i in range(len(s)):
        answer += s[i].upper() if isEven else s[i].lower()
        isEven = True if s[i] == ' ' else not isEven
    return answer
