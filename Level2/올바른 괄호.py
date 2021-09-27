def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
    return len(stack) == 0
