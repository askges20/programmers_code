def change_note(note): # 멜로디와 악보에서 #이 붙은 음을 소문자로 치환
    new_note = []
    for n in note:
        if n == '#':
            new_note[-1] = new_note[-1].lower()
        else:
            new_note.append(n)
    return new_note

def solution(m, musicinfos):
    m = change_note(m)
    result = []
    
    for i in range(len(musicinfos)):
        start, end, name, note = musicinfos[i].split(",")
        new_note = change_note(note)
        
        start = start.split(":")
        end = end.split(":")
        playtime = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1])) #재생 시간 계산
        
        if len(new_note) > playtime: #플레이시간이 음악 길이보다 짧으면
            new_note = new_note[:playtime]
        else: #플레이시간이 음악 길이보다 길면 (반복 재생)
            new_note = new_note * (playtime // len(new_note)) + new_note[:(playtime % len(new_note))]
        
        m = "".join(m)
        played_note = "".join(new_note)
        if m in played_note:
            result.append([-playtime, i, name]) #재생 시간, 순서, 이름 저장
        result.sort() #정렬
    
    return result[0][-1] if len(result) > 0 else "(None)"
