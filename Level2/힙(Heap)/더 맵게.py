def solution(scoville, K):
    import heapq
    cnt = 0
    heapq.heapify(scoville) #리스트를 힙으로
    
    while scoville[0] < K:  #스코빌 지수가 K이상이 아닌 음식 존재
        cnt += 1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f + s * 2) #두 개의 음식 섞기
        if len(scoville) == 1 and scoville[0] < K:  #더이상 섞지 못할 때
            return -1
    return cnt

'''
import heapq
heapq.heapify(list) #리스트를 오름차순 heapq로 변환
heapq.heappop(list) #리스트의 가장 작은 값을 pop(return, 삭제)
heapq.heappush(list, value) #리스트에 value 삽입 및 자동 정렬
'''
