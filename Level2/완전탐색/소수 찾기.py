import math

primes = set([])
strList = []
madeNumList = set([])
    
def solution(numbers):
    for i in numbers:
        strList.append(i) #각 숫자를 하나씩 분리
        
    for j in strList:
        if j == "0":
            continue
        num = j
        madeNumList.add(num) #만들 수 있는 숫자 리스트에 넣음
        tmpList = list(strList)
        #recursion에서 tmpList에 있는 숫자들을 하나씩 붙여서 숫자를 만들어 볼 것
        tmpList.remove(num) #num은 이미 사용했기 때문에 tmpList에서 제거
        recursion(num, tmpList) #recursion으로 숫자들 만들기
        
    for k in madeNumList: #만들어진 숫자들의 소수 판별
        if isPrime(int(k)):
            primes.add(k)
            
    print(primes)
    return len(primes)        

def recursion(num, tmpList):
    for j in range(len(tmpList)):
        tmpNum = num + tmpList[j]
        madeNumList.add(tmpNum)
        
        tmpList2 = list(tmpList)
        tmpList2.remove(tmpList[j])
        
        recursion(tmpNum, tmpList2) #다시 recursion 호출해서 숫자 이어붙이기
        
    
def isPrime(num): #소수 판별
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True