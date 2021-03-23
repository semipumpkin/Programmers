import itertools
# from itertools import combinations



# def solution(clothes):
#     clothes_dict = {}
#     for cloth in clothes:
#         if cloth[1] not in clothes_dict.keys():
#             clothes_dict[cloth[1]] = 1
#         else:
#             clothes_dict[cloth[1]] += 1
#
#     answer = 0
#     value_list = list(clothes_dict.values())
#     N = len(value_list)
#     visited = [0] * N
#     def johab(index, sel):
#         global answer, value_list
#         if index == N:
#             result = 1
#             for i in range(N):
#                 if sel[i]:
#                     result *= sel[i] * value_list[i]
#             answer += result
#
#             return
#
#
#         sel[index] = 1
#         johab(index+1, sel)
#         sel[index] = 0
#         johab(index+1, sel)
#     johab(0, visited)
#     return answer
final = 0
def solution(clothes):
    # 각 종류마다 딕셔너리 만들고, 같은 종류의 다른 아이템일경우 + 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict.keys():
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1

    # 각각 종류마다 숫자의 리스트를 만들어줌
    value_list = list(clothes_dict.values())
    N = len(value_list)
    visited = [0] * N

    # 가지고 있는 옷의 종류가 모두 다르면 2^n - 1이니까 바로 return
    if value_list.count(1) == len(value_list):
        return 2**len(value_list) - 1

    # 아닐 경우 powerset을 이용
    else:
        def johab(index, sel, values):
            global final
            if index == N:

                result = 1
                for i in range(N):
                    if sel[i]:
                        result *= sel[i] * values[i]
                # print(sel, result)
                final += result

                return

            sel[index] = 1
            johab(index + 1, sel, values)
            sel[index] = 0
            johab(index + 1, sel, values)

        johab(0, visited, value_list)
        # -1 을 해주는 경우는 아무것도 입지 않았을 경우 이므로 1을 빼줌
        return final - 1

    # return clothes_dict
# 2 1 1 => 숫자 다 더해줌. 4 + 숫자 2개씩 뽑아서 곱한담에 더해줌. 5 + 숫자 3개씩 뽑아서 다 곱한담에 더해줌 2

# 3 2 4 5 => 14C1 +
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict.keys():
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1

    for val in clothes_dict.values():
        answer *= (val + 1)

    return answer - 1

'''
2 1 
3 + 2
'''
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "a"]])) # 11
box = []
for i in range(30):
    box.append([i, -i])
# print(box)
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])) # 3
print(solution(box))
# print(combinations(4, 2))