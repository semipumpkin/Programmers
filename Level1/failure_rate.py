def solution(N, stages):
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

    # 전체 스테이지의 개수 N
    # 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호 배열
    # 사용자
    answer = []

    # 스테이지 못깬 사람의 수
    heojeob = 0

    # 사용자의 수
    n = len(stages)

    for i in range(1, N + 1):

        # 예외처리! 이거 안하면 런타임에러남
        if stages.count(i) == 0:

            # answer에 실패율과 스테이지를 리스트로 만들어서 저장해줌
            answer += [[0, i]]
        else:
            answer += [[stages.count(i) / (n - heojeob), i]]

            # 스테이지를 못넘어가고 실패한 사람은 heojeob에 수를 더해줌
            heojeob += stages.count(i)

    # answer를 정렬하고 reverse 시키면 실패율이 같을때, 내림차순이 되어버림
    failure = list(reversed(sorted(answer)))

    # 따라서, 실패율이 같을때, 오름차순으로 바꿔줘야함
    for i in range(len(failure)):
        for j in range(i, len(failure)):
            # 앞의 수가 같다면
            if failure[i][0] == failure[j][0]:
                failure[i], failure[j] = failure[j], failure[i]
    # 인덱스만 result에 저장해줌
    result = []
    for i in range(len(failure)):
        result.append(failure[i][1])

    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))