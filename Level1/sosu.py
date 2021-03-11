def solution(n):
    count = [0] + [1] * n
    for i in range(2, n + 1):
        if n % i == 0:
            count[i] = 0
    return count.count(1)
print(solution(10))
print(solution(5))