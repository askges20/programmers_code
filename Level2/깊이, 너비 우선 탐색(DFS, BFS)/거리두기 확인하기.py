def bfs(p, idx): #bfs를 이용한 풀이
    visited = [[False] * 5 for _ in range(5)]
    queue = [idx]
    dir = [[-1,0], [1,0], [0,-1], [0,1]] #방향
    
    while queue:
        x, y, d = queue.pop()
        visited[x][y] = True #방문
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            nd = d + 1
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]: #범위 내에 있고 방문하지 않은 경우
                visited[nx][ny] = True
                
                if p[nx][ny] == 'P': #응시자가 있는 자리
                    if nd <= 2: #맨해튼 거리가 2이하이면
                        return False #거리두기 지키지 않음
                elif p[nx][ny] == 'O': #빈 테이블
                    if nd == 1:
                        queue.append([nx, ny, nd]) #현재 자리 기준 거리 1인 자리 더 확인
    return True #모든 지원자와 거리두기 지킴

def solution(places):
    answer = []
    for p in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P': #지원자가 있는 자리
                    result = bfs(p, [i, j, 0]) #bfs로 거리두기 확인
                    if not result:
                        flag = 0
        answer.append(flag)
    return answer
