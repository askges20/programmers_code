#완전탐색
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    best = []
    
    for i in range(len(answers)):
        scores[0] = scores[0] + (answers[i] == one[(i+1)%len(one)-1])
        scores[1] = scores[1] + (answers[i] == two[(i+1)%len(two)-1])
        scores[2] = scores[2] + (answers[i] == three[(i+1)%len(three)-1])
    
    for j in range(len(scores)):
        if max(scores) == scores[j]:
            best.append(j+1)
            
    return best
