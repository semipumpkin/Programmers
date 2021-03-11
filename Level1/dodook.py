def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for num in _reserve:
        ab = num - 1
        back = num + 1
        if ab in _lost:
            _lost.remove(ab)
        elif back in _lost:
            _lost.remove(back)
    return n - len(_lost)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [2])) # 3
print(solution(3, [3, 2], [2])) # 2