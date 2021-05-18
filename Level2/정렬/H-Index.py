def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    length = len(citations)
    for i in range(length):
        if citations[length-i-1] >= length-i:
            return length - i
    return 0