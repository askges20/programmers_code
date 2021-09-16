def get_new(str):
    new_str = []
    for i in range(len(str) - 1):
        cur = str[i:i+2]
        if not cur.isalpha():
            continue
        new_str.append(cur)
    return new_str

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    str1_new, str2_new = get_new(str1), get_new(str2)
    
    inter = list(set(str1_new) & set(str2_new))
    union = list(set(str1_new) | set(str2_new))
    
    total, alike = 0, 0
    
    for a in range(len(union)):
        cnt_list = []
        total += max(str1_new.count(union[a]), str2_new.count(union[a]))
    if total == 0:
        return 65536
    
    for b in range(len(inter)):
        alike += min(str1_new.count(inter[b]), str2_new.count(inter[b]))
    
    return int((alike/total) * 65536)
