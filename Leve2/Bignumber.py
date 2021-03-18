# max_number = 0
# def solution(number, k):
#
#     sel = [0] * len(number)
#     t = len(number) - k
#
#     def partof(idx):
#         global max_number
#         N = len(number)
#         if idx == N:
#             if sel.count(1) == t:
#                 temp = ''
#                 for i in range(N):
#                     temp += number[i] * sel[i]
#                 if int(temp) > max_number:
#                     max_number = int(temp)
#             return
#         sel[idx] = 1
#         partof(idx + 1)
#         sel[idx] = 0
#         partof(idx + 1)
#
#     partof(0)
#     return str(max_number)


def solution(number, k):
    picks = len(number) - k
    result = ''
    # picks의 개수만큼 문자를 뽑는데

    # 그 합이 가장 큰것

    # 첫번째로 가장 큰 문자 = 문자열에서 picks - 1의 개수를 제외한 숫자중에 가장 큰 수
    # 두번째로 가장 큰 문자 = 첫번째로 가장 큰 문자에서 picks -2의 개수를 제외한 숫자중에 가장 큰 수
    # .... picks가 0이 될때까지 반복

    index = 0
    while picks:
        # 슬라이싱을 하면 개느리다
        # target = number[index:len(number) - picks + 1]
        target = ''
        for k in range(index, len(number) - picks + 1):
            target += number[k]

            # 만약 이 조건이 없다면 시간초과가 남.
            # 예외처리의 중요성
            if number[k] == '9':
                break
        max_num = "0"
        index2 = 0
        for i in range(len(target)):
            if target[i]> max_num:
                max_num = target[i]
                index2 = i

                # 만약 이 조건이 없다면 시간초과가 남.
                # 예외처리의 중요성
                if max_num == "9":
                    break
        # 인덱스 초기화
        index += index2 + 1

        result += max_num
        picks -= 1
    return result
# print(solution("1924", 2)) # 94
# print(solution("1231234", 3)) # 3234
print(solution("4177252841", 4)) # 775841
'''
target   index
41772     2 + 1 3
725       0 + 1 1
252       1 + 1 2
28        1 + 1 2
41        0 + 1 1
1         0 + 1 1
'''