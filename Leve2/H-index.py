# def solution(citations):
#     answer = 0
#     N = len(citations)
#     citations.sort(reverse=True)
#     # 6, 5, 3, 1, 0
#     # 6, 5, 4, 1, 0
#     for i in range(N):
#         h = N - i
#         if citations[i] <= h:
#             cnt = i + 1
#             for j in range(i+1, N):
#                 if citations[j] == citations[i]:
#                     cnt += 1
#                 else:
#                     break
#             if N - cnt <= citations[i] <= cnt:
#                 answer = h
#                 break
def solution(citations):
    answer = 0

    return answer

print(solution([3, 0, 6, 1, 5])) # 3
print(solution([4, 0, 6, 1, 5])) # 3
# print(solution([5, 5, 5, 5, 5])) # 3
# print(solution([5, 4, , 5, 5])) # 3
