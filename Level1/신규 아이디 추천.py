import re

def solution(id):
    #1단계
    id = id.lower()
    #2단계
    new_id = ''
    for w in id:
        if w.isalnum() or w in '-_.':
            new_id += w
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    #4단계
    if new_id[0]=='.' and len(new_id)>1:
        new_id = new_id[1:]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    #5단계
    if new_id=='':
        new_id = 'a'
    #6단계
    if len(new_id)>15:
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    #7단계
    if len(new_id)<3:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    return new_id