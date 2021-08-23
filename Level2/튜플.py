def solution(s):
    s = s[1:-1] + ','
    sorted_s = list(map(lambda x:x[1:], s.split('},')[:-1])) #괄호 없애고 리스트로
    sorted_s.sort(key = len) #길이순 정렬
    result = [sorted_s[0]] #튜플 첫번째 원소
    
    for i in range(len(sorted_s)):
        tmp = sorted_s[i].split(',') #집합 {a1,a2} 요소를 , 를 기준으로 분리
        for j in range(len(tmp)):
            if tmp[j] not in result:
                result.append(tmp[j])
                break
    
    return list(map(int, result))
