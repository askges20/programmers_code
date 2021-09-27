#sort 정렬 -> 하나의 리스트에 비교 기준 순서대로 값을 넣어놓고 sort 할때 순서대로 비교
def solution(weights, head2head):
    num_boxers = len(weights) #선수 수
    record = [[] for _ in range(num_boxers)] #승률, 무거운 사람, 자기 몸무게, 번호(음수)
    
    for i in range(num_boxers):
        if head2head[i].count('N') == num_boxers: #경기x 복서 승률 0
            record[i].append(0)
        else:
            cnt_win = head2head[i].count('W') #이긴 횟수
            record[i].append(cnt_win / (cnt_win + head2head[i].count('L'))) #승률 구하기
        cnt_heavy = 0
        for j in range(num_boxers):
            if weights[j] > weights[i] and head2head[i][j] == 'W': #무거운 사람 이긴 횟수
                cnt_heavy += 1
        record[i].extend([cnt_heavy, weights[i], -(i + 1)])
    record.sort(reverse = True)
    result = []
    for i in range(num_boxers):
        result.append(-record[i][-1])
    return result


  
#lambda 정렬 -> 각 비교 기준을 다른 리스트에 저장하고 key로 비교
def solution(weights, head2head):
    num_boxers = len(weights) #선수 수
    nums = [] #선수 번호
    rate = [] #승률
    win_heavy = [] #자신보다 무거운 사람을 이긴 횟수
    
    for i in range(num_boxers):
        nums.append(i + 1) #번호
        if head2head[i].count('N') == num_boxers: #경기x 복서 승률 0
            rate.append(0)
        else:
            cnt_win = head2head[i].count('W') #이긴 횟수
            rate.append(cnt_win / (cnt_win + head2head[i].count('L'))) #승률 구하기
        cnt_heavy = 0
        for j in range(num_boxers):
            if weights[j] > weights[i] and head2head[i][j] == 'W': #무거운 사람 이긴 횟수
                cnt_heavy += 1
        win_heavy.append(cnt_heavy)
    result = sorted(nums, key = lambda x : (-rate[x - 1], -win_heavy[x - 1], -weights[x - 1], x)) #람다 이용해서 정렬하기
    return result
