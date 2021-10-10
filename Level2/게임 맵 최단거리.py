def solution(maps):
    m, n = len(maps), len(maps[0])
    cnt_maps = [[-1 for _ in range(n)] for _ in range(m)]
    cnt_maps[0][0] = 1
    
    dir = [[1,0], [0,1], [0,-1], [-1,0]] #방향
    queue = [[0, 0]]
    while queue:
        cur = queue.pop(0)
        x, y = cur[0], cur[1]
        for d in dir:
            new_x, new_y = x + d[0], y + d[1]
            if 0 <= new_x < m and 0 <= new_y < n and maps[new_x][new_y] == 1:
                if cnt_maps[new_x][new_y] == -1:
                    cnt_maps[new_x][new_y] = cnt_maps[x][y] + 1
                    queue.append([new_x, new_y])
    return cnt_maps[-1][-1]
