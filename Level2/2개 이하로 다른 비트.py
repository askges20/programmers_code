def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            bits = list('0' + bin(n)[2:])
            idx = ''.join(bits).rfind('0')
            bits[idx] = '1'
            bits[idx + 1] = '0'
            answer.append(int(''.join(bits), 2))    
    return answer
