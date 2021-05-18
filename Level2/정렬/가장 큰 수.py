def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ""
    for n in numbers:
        answer = answer + str(n)
    return str(int(answer))