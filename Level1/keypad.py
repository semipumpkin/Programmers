def solution(numbers, hand):
    answer = ''
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    position_left = [3, 0]
    position_right = [3, 2]

    # 숫자가 1, 4, 7 일때 왼손, 숫자가 3, 6, 9 일때 오른손
    for num in numbers:
        if num in [1, 4, 7]:

            for i in range(3):
                if num == phone[i][0]:
                    answer += 'L'
                    position_left = [i, 0]
        elif num in [3, 6, 9]:
            for i in range(3):
                if num == phone[i][2]:
                    answer += 'R'
                    position_right = [i, 2]

        # 숫자가 2, 5, 8, 0 일때, 거리비교
        elif num in [2, 5, 8, 0]:

            for y in range(4):

                if num == phone[y][1]:
                    # 현재 위치와 누를 숫자의 위치의 인덱스의 차를 다 더해줘서 거리를 구함
                    DR = abs(y - position_right[0]) + abs(1 - position_right[1])
                    DL = abs(y - position_left[0]) + abs(1 - position_left[1])
                    if DR < DL:
                        answer += 'R'
                        position_right = [y, 1]
                    elif DR > DL:
                        answer += 'L'
                        position_left = [y, 1]
                    elif DR == DL:
                        answer += hand[0].upper()
                        if hand[0].upper() == 'R':
                            position_right = [y, 1]
                        elif hand[0].upper() == 'L':
                            position_left = [y, 1]
        # print(phone[position_left[0]][position_left[1]], phone[position_right[0]][position_right[1]])


    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))

