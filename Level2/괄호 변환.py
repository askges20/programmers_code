def is_correct(u): #올바른 괄호 문자열 판별
    stack = [u[0]] #스택 이용
    for i in range(1, len(u)):
        if stack[-1] == u[i]:
            stack.append(u[i])
        elif stack[-1] == "(" and u[i] == ")":
            stack = stack[:-1]
    return len(stack) == 0

def solution(p):
    answer = ""
    if p == "": #빈문자열 입력
        return ""
    for i in range(2, len(p) + 1, 2):
        print(p[0:i])
        if p[0:i].count("(") == p[0:i].count(")"):
            u = p[0:i]
            v = p[i:]
            break
    if is_correct(u): #u가 올바른 괄호 문자열
        answer += u + solution(v)
    else: #u가 올바른 괄호 문자열이 아님
        answer = "(" + solution(v) + ")" #4-1 ~ 4-3
        u = u[1:-1] #4-4
        tmp = ""
        for i in range(len(u)):
            if u[i] == "(":
                tmp += ")"
            else:
                tmp += "("
        answer += tmp
    return answer
