def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        order = ""
        for s in skill_tree:
            if s in skill: #선행 스킬에 포함된 것만 걸러내기
                order += s
        if skill.startswith(order): #선행 스킬 맨 앞부터 순서대로 스킬을 배웠으면 cnt 증가
            cnt += 1
    return cnt
