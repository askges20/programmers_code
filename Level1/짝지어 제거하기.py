def solution(s):
    stack = [] #스택 이용
    for c in s:
        stack.append(c)
        if len(stack)>=2:
            if stack[-2]==stack[-1]:
                stack.pop(-1)
                stack.pop(-1)
    return 1 if len(stack)==0 else 0
