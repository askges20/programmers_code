def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        if word == '':
            answer += ' '
            continue
        w = word.lower()
        answer = answer + w[0].upper() + w[1:] + ' ' if w[0].isalpha() else answer + w + ' '
    return answer[:-1]
