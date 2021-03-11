def solution(participant, completion):
    # count의 리스트를 만들고 참가자의 이름만 있는 names 리스트 만듦
    cnt = [0] * len(set(participant))
    names = list(set(participant))
    
    # participant를 돌며, names에 이름이 있다면 count를 추가
    for i in range(len(participant)):
        if participant[i] in names:
            cnt[i] += 1
    
    # completion을 돌며, names에 이름이 있다면 count를 감소
    for j in range(len(completion)):
        if completion[j] in names:
            cnt[j] -= 1
    # count를 돌며 count가 1인 인덱스의 names 요소 return
    for k in range(len(cnt)):
        if cnt[k] == 1:
            return names[k]
             

print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
