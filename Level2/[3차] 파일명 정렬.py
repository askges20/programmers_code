def solution(files):
    re_files = []
    for file in files:
        head, number, tail = "", "", ""
        for i in range(len(file)):
            if file[i].isnumeric(): #number 부분
                number += file[i]
            else:
                if number == "": #head 부분
                    head += file[i]
                else:
                    re_files.append([head.lower(), int(number), file])
                    break
        if i == len(file) - 1: #tail이 빈문자열
            re_files.append([head.lower(), int(number), file])
        re_files.sort(key = lambda x : (x[0], x[1])) #정렬
    return list(map(lambda x : x[-1], re_files))
