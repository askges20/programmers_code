def solution(n, words):
    last = words[0]
    history = set([last])
    for i in range(1, len(words)):
        if (words[i] in history) or (words[i][0] != last[-1]):
            return [i % n + 1, i // n + 1]
        history.add(words[i])
        last = words[i]
    return [0,0]
