# 1. n을 3진법으로 바꾼다
def samjin(n):
    nums = ''
    if n < 3:
        nums += str(n)
    else:
        nums += str(samjin(n % 3))
        return samjin(n // 3) + samjin(n%3)
    return nums

# 2. 3진법으로 바꾼 수를 앞뒤로 순서를 바꾼다. 
def solution(n):
    reverse = ''
    sam = samjin(n)
    for i in range(1, len(sam) + 1):
        reverse += sam[-i]
# 3. 이를 다시 10진법으로 바꾼다. 
    num = 0
    for j in range(1, len(reverse) + 1):
        num += int(reverse[-j]) * 3 ** (j - 1)
    return num 
    

print(solution(45))
print(solution(125))

