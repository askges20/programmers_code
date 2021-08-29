def get_grade(avg):
    grade = ""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def solution(scores):
    n = len(scores) #학생 수
    grade = ""
    for i in range(n):
        student = []
        n = len(scores)
        for j in range(n):
            student.append(scores[j][i]) #점수들
        self_score = student[i] #자기 점수
        if (self_score == max(student) or self_score == min(student)) and student.count(self_score) == 1: #자기 점수가 유일한 최대 or 최소 값일 때
            student[i] = 0 #평균 계산에서 제외
            n -= 1
        avg = sum(student)/n #평균
        grade += get_grade(avg) #학점 구하기
    return grade
