def solution(orders, course):
    # 코스 배열 = 메뉴의 개수
    # 코스 배열을 돌면서 중복된 메뉴의 개수를 찾자.
    answer = []
    for num in course:
        # 각 메뉴의 개수를 돌며,
        result = []
        result_count = []
        for order in orders:
            N = len(order)
            sel = [0] * N
            def menu(index):
                if index == N:
                    if sel.count(1) == num:
                        # print(sel)
                        temp = ''
                        for i in range(N):
                            temp += order[i] * sel[i]
                        temp = sorted(temp)
                        temp = ''.join(temp)

                        if temp not in result:
                            # print(temp)
                            result.append(temp)
                            result_count.append(1)
                        else:
                            for i in range(len(result)):
                                if result[i] == temp:
                                    result_count[i] += 1

                    return
                sel[index] = 1
                menu(index+1)
                sel[index] = 0
                menu(index+1)
            menu(0)
        # print(result)
        # print(result_count)
        M = len(result_count)
        if M > 2:
            max_num = max(result_count)
            for i in range(M):
                if result_count[i] == max_num and result_count[i] >= 2:
                    answer.append(result[i])

        # answer.append(result)
    return sorted(answer)
# course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
# course 배열에는 같은 값이 중복해서 들어있지 않습니다.
'''
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
'''

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print((solution(["XYZ", "XWY", "WXA"], [2,3,4])))
# 	["WX", "XY"]