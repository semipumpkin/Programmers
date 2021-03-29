count0 = 0
count1 = 0
def lookingfor(N, box):

    R = int(2/N)
    global count0, count1

    # 1사분면 탐색
    target1 = box[0][0]
    for y in range(R):
        for x in range(R):
            if

    return count, N**2 - count
    # 다 탐색하고나면



def solution(arr):
    # 재귀느낌?
    # arr = 2^n 개의 사각형
    # 일단 완탐으로 풀어보자
    # arr[0][0]의 숫자와 같지 않은걸 쭉 찾고,
    # 만약 같지 않은걸 찾는다면 쪼개자
    # 계속 같다면 그쪽의 사각형은 탐색 더이상 x


    answer = []
    return answer



tc1 = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
tc2 = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4, 9]
# print(solution(tc2)) # [10, 15]


print(lookingfor(len(tc1), tc1))