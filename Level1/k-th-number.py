
def solution(array, commands):
    answer = []
    for i in range(0, len(commands)): 
        cut = sorted(array[commands[i][0] - 1 : commands[i][1]])
        answer += [cut[commands[i][2] - 1]]
    return answer
if


h = [1, 5, 2, 6, 3, 7, 4]
r = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(h, r))
#[5, 6, 3]
print(h[0 : 3])
# index 에러 잘 극복하기!
