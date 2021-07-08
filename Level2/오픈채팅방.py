def solution(record):
    result = []
    id_nick = {}
    
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            result.append(r[1] + "/님이 들어왔습니다.")
            id_nick[r[1]] = r[2]
        elif r[0] == "Leave":
            result.append(r[1] + "/님이 나갔습니다.")
        else: #Change
            id_nick[r[1]] = r[2]
            
    for i in range(len(result)):
        r = result[i]
        result[i] = id_nick[r.split("/")[0]] + r.split("/")[1]
    return result
