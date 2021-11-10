from itertools import permutations

def find(cur, path):
    cnt = 0
    for dungeon in path:
        if cur < dungeon[0]:
            return cnt
        else:
            cur = cur - dungeon[1]
            cnt += 1
    return cnt
    
def solution(k, dungeons):
    max_cnt = 0
    paths = permutations(dungeons, len(dungeons))
    for path in paths:
        max_cnt = max(max_cnt, find(k, path))
    return max_cnt
  
  # 던전 최대 개수가 8개이므로 permutations를 이용해서 완전 탐색
