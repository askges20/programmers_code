def solution(n, computers):
    answer=0
    visited=[] #탐색한 컴퓨터
    for c in range(n):
        if c not in visited:
            bfs(n, computers, c, visited)
            answer+=1
    return answer

def bfs(n, computers, c, visited):
    queue=[c]
    while queue:
        c=queue.pop(0)
        visited.append(c) #탐색 표시
        for link in range(n):
            if link!=c and computers[c][link] and (link not in visited): #탐색하지 않은 다른 컴퓨터와 연결되어있는 경우
                queue.append(link)
