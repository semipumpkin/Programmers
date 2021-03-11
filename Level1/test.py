def solution(n):
    count = [0] + [0] * n
    for i in range(2, n + 1):
        if n % i == 0:
            count[i] == 1
    return count
print(solution(100))