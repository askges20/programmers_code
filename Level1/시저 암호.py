def solution(s, n):
    result = ''
    for i in range(len(s)):
        if s[i].isupper(): #대문자
            result += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower(): #소문자
            result += chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        else:
            result += ' '
    return result
  
  #isupper, islower : 대소문자 확인
  #ord, chr : 아스키코드 변환
