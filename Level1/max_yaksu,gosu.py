def solution(n, m):
    # result1 약수 리스트
    result1 = []
    for i in range(1, m+1):
        if m % i == 0 and n % i == 0:
            result1 += [i]
    # 최대공약수
    ans1 = max(result1)

    # 최소공배수
    ans2 = (n//ans1) * (m//ans1) * ans1
    return [ans1, ans2]
print(solution(3, 12))
print(solution(2, 5))
print(solution(20, 2))
print(solution(6, 15))