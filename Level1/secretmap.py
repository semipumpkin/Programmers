# 이진수 변환 함수
def dec_to_bin(n):
    nums = ''
    if n < 2:
        nums += str(n)
    else:
        nums += str(dec_to_bin(n%2))
        return dec_to_bin(n//2) + dec_to_bin(n%2)
    return nums

def solution(n, arr1, arr2):
    # 첫번째 지도
    answer = []

    # 두번째 지도
    answer2 = []
    for i in range(len(arr1)):

        # 그냥 1이 나올때 #, 0이 나올때 공백을 추가하면 자리수가 부족할때가 있다.
        if len(dec_to_bin(arr1[i])) < n:

            # 따라서 자리수가 부족할때는 곧 앞에 0이 부족한거이므로 앞에다 부족한 자리수의 개수만큼
            # '0'을 더해줌
            answer.append('0'*(n - len(dec_to_bin(arr1[i]))) + dec_to_bin(arr1[i]))
        else:
            answer.append(dec_to_bin(arr1[i]))
        # 위와 동일
    for i in range(len(arr2)):
        if len(dec_to_bin(arr2[i])) < n:
            answer2.append('0'*(n - len(dec_to_bin(arr2[i]))) + dec_to_bin(arr2[i]))
        else:
            answer2.append(dec_to_bin(arr2[i]))
    # n * n행렬을 만들때 각 자리의 지도에 1이 하나라도 있으면 '#', 둘다 없으면 공백 ' ' 추가
    result = []
    for y in range(n):
        strings = ''
        for x in range(n):
            if answer[y][x] == '1' or answer2[y][x] == '1':
                strings += '#'
            else:
                strings += ' '
        result.append(strings)
    return result
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27, 56, 19, 14, 14, 10]))
# print(dec_to_bin(8))
