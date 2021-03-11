def solution(bridge_length, weight, truck_weights):
    q = [truck_weights.pop(0)]
    time_list = [1]
    time = 1

    while q:
        if time_list and time_list[0] == bridge_length:
            q.pop(0)
            time_list.pop(0)
        if truck_weights and sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights.pop(0))
            time_list.append(0)

        time += 1
        for i in range(len(time_list)):
            time_list[i] += 1
    # 최대로 다리에 트럭을 집어넣은 상태

    # 시간을
    return time
'''
1 [] [7] [4, 5, 6]
스택이 빌때까지 반복

'''

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))