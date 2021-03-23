

answer = 0
def solution(numbers, target):
    N = len(numbers)
    sel = [0] * N
    def powerset(idx):
        global answer
        if idx == N:
            total = 0
            for i in range(N):
                total += sel[i] * numbers[i]
            if total == target:
                answer += 1
            return
        sel[idx] = -1
        powerset(idx+1)
        sel[idx] = 1
        powerset(idx+1)
    powerset(0)


    return answer
print(solution([1, 1, 1, 1, 1], 3))