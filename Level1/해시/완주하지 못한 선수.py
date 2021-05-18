def solution(participant, completion):
    pdic = {}
    for p in participant: #pdic에 참여자 이름과 인원 저장
        if p not in pdic.keys():
            pdic[p] = 1
        else:
            pdic[p] = pdic[p] + 1
            
    for c in completion: #완주자 인원만큼 value값 감소
        pdic[c] = pdic[c] - 1
    
    for p in participant:
        if pdic[p] == 1 : #pdic에서 value가 1인 사람 리턴
            return p
