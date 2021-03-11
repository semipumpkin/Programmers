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
    num = len(number) - k

    pass

print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234
print(solution("4177252841", 4)) # 775841
# pt = [0]*4
# at = []
# partof(0, "1924", at, pt)
# print(max(at))