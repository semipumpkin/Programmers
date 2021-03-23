def binarysearch(numbers, target):
    N = len(numbers)
    mid = int(N/2)

    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        pass
    else:
        pass
def solution(people, limit):
    N = len(people)
    people = sorted(people)
    count_people = [0] * N
    answer = 0
    for i in range(N):
        if count_people[i] == 0:
            # 한명을 일단 태움
            boat = people[i]
            count_people[i] = 1
            # 그리고 그 뒤에서 한명을 더 태워야 하는데
            max_num = 0
            max_weight = limit - boat
            index = 0
            mid = (N - 1 + i) / 2
            mid_weight = people[int(mid)]


            '''
            for j in range(N-1, i, -1):
                if count_people[j] == 0:
                # 한명 일단 태우고 나머지 사람은 보트가 허용하는 한 가장 높은 몸무게의 사람을 태워야 많이 태움
                    if max_num <= people[j] < max_weight:
                        max_num = people[j]
                        index = j
                    elif people[j] == max_weight:
                        index = j
                        # count_people[j] = 1
                        break
            count_people[index] = 1
            answer += 1
            '''
    # 한번에 최대 2 명
    # 구명보트 최대한 적게 사용
    return answer
# 인덱스로 움직이는건 while로 푸는게 좋다

# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))

