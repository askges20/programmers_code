def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1
    start, end = 0, 0
    while True:
        end += 1
        if end == len(msg):
            answer.append(dic[msg[start:end]])
            break
        if msg[start:end+1] not in dic.keys():
            answer.append(dic[msg[start:end]])
            dic[msg[start:end+1]] = len(dic) + 1
            start = end
    return answer
