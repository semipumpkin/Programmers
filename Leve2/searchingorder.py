def solution(info, query):
    answer = []

    # info 원소들을 ' '로 붙여서 리스트로 만듦
    # query 원소들을 ' and '로 붙여서 리스트로 만듦
    # query를 돌며 info의 모든 원소들을 하나하나씩 비교 하고
    # 해당하는 info의 원소가 있으면 숫자를 저장.
    for i in range(len(info)):
        info[i] = list(info[i].split())
    query = [list(q.split(' and ')) for q in query ]
    for q in query:
        # query를 돌며 info의 원소들을 하나씩 비교
        cnt = 0
        for i in info:

            # 첫 4개의 원소를 비교
            for k in range(4):
                if q[k] == i[k] or q[k] == '_':
                    continue
                else:
                    break
            else:
                if i[-1] >= q[-1]:
                    cnt += 1
                else:
                    break
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
