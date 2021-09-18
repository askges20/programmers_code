def is_correct(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif (stack[-1] == "(" and s[i] == ")") or (stack[-1] == "[" and s[i] == "]") or (stack[-1] == "{" and s[i] == "}"):
            stack = stack[:-1]
        else:
            stack.append(s[i])
    return len(stack) == 0

def solution(s):
    cnt = 0
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if is_correct(s):
            cnt += 1
    return cnt
