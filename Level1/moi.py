def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 답의 길이만큼 답안지의 길이를 늘림
    man = [first, second, third]
    for nums in man:
        while len(nums) < len(answers):
            nums += nums
    # 답이 맞다면 count를 1씩늘리고,
    count = [0] * 3  
    for i in range(len(answers)):
        if answers[i] == first[i]:
            count[0] += 1
        if answers[i] == second[i]:
            count[1] += 1
        if answers[i] == third[i]:
            count[2] += 1
    # 가장 많이 맞춘사람을 리스트에 저장하고 return 시킴
    answer = []
    for i in range(len(count)):
        if count[i] == max(count):
            answer += [i + 1]
    return answer
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

