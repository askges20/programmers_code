def solution(N, road, K):
    answer = 0
    times = [[500000 for _ in range(N + 1)] for _ in range(N + 1)]
    for v1, v2, t in road: #인접 행렬
        times[v1][v2] = min(times[v1][v2], t)
        times[v2][v1] = min(times[v2][v1], t)
    
    #다익스트라 알고리즘
    min_time = [500000 for _ in range(N + 1)]
    queue = [1]
    while queue:
        cur_node = queue.pop(0)
        for i in range(2, N + 1):
            next_node, t = i, times[cur_node][i]
            if min_time[cur_node] == 500000:
                tmp_min = times[cur_node][next_node]
            else:
                tmp_min = min_time[cur_node] + t
            if min_time[next_node] > tmp_min:
                min_time[next_node] = tmp_min
                queue.append(next_node)
                
    return len(list(filter(lambda t: t <= K, min_time))) + 1
