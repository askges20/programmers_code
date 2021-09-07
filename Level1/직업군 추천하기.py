def solution(table, languages, preference):
    table_split = []
    for i in range(len(table)):
        table_tmp = table[i].split()
        table_tmp.reverse()
        table_split.append([table_tmp[-1]] + table_tmp[:-1])
    
    max_score = -1
    max_job = []
    for i in range(len(table_split)):
        score = 0
        for j in range(len(languages)):
            if languages[j] in table_split[i]:
                score += table_split[i].index(languages[j]) * preference[j]
        if max_score < score:
            max_score = score
            max_job = [table_split[i][0]]
        elif max_score == score:
            max_job.append(table_split[i][0])
            
    return sorted(max_job)[0]
