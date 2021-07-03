def solution(n, arr1, arr2):
    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = bin(arr1[i] | arr2[i])[2:]
        arr[i] = "0" * (n-len(arr[i])) + arr[i]
        arr[i] = arr[i].replace('1','#')
        arr[i] = arr[i].replace('0',' ')
    return arr
