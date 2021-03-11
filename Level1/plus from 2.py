def solution(numbers):
    # 2 <= len(numbers) <= 100
    answer = []
    l = len(numbers)
    for i in range(l):
        for j in range(l):
            if i != j and numbers[i] + numbers[j] not in answer:
                answer += [numbers[i] + numbers[j]]
                
    return sorted(answer)

a = [2, 1, 3, 4, 1]
b = [5, 0, 2, 7]

print(solution(a))
print(solution(b))