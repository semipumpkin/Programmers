def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

print(solution('pPoooyY'))
print(solution('pyY'))