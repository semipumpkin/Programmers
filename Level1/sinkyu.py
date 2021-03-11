def solution(new_id):
    # answer = ''
# 1. 소문자 치환
    new_id = new_id.lower()
# 2. 필요없는 문자 제거
    special = '~!@#$%^&*()=+[{]}:?,<>/'
    removed = ''
    # count = 0
    for i in range(len(new_id)):
        if new_id[i] not in special:
            removed += new_id[i]

# 3. 마침표 두번 연속은 하나의 마침표 치환
    while '..' in removed: 
        removed = removed.replace('..', '.')
# 4. 마침표 처음 끝 제거

    if removed[0] == '.':
        # removed = removed.replace('.', '', 1)
        # 슬라이싱은 매우 위험한 발상이 될 수 있다. 
        removed = removed[1:]
    elif removed[-1] == '.':
        removed = removed[:-1]

            
# 5. 비어있다면 a 대입
    if len(removed) == 0:
        removed = 'a'
            
# 6. 길이 16이상이면 첫 15개의 문자남기고 다 제거 마침표가 끝에 위치하면 마침표 제거
    if len(removed) >= 16:
        removed = removed[:15]
    if removed[-1] == '.':
        removed = removed[0:-1]
        # 왜 이게 -1이여야 될까?
        # removed = removed[0:14]
    
# 7. 마침표 길이가 2이하라면 마지막문자를 3될때까지 반복
    while len(removed) <= 2:
        removed += removed[-1]
        

    return removed






print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))