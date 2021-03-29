def searching(y, x, board, N, M):
    if N > M:
        N = M
    T = 1
    while y + T < N or x + T < N:
        for i in range(y, y + T + 1):
            for j in range(x, x + T + 1):
                if not board[y+T][x]:
                    return T
            if not board[y][x+T]:
                return T
        T += 1
    return T
#
# max_width = 0
#
def solution(board):
    global max_width
    y = 0
    x = 0
    N = len(board)
    M = len(board[0])
    while True:
        while True:
            if board[y][x]:
                pass
            x += 1
        y += 1

    return max_width
#
# def solution(board):
#     answer = 0
#     H = len(board)
#     W = len(board[0])
#     if H == 1 or W == 1:
#         return 1
#     for r in range(1, H):
#         for c in range(1, W):
#             if board[r][c] == 1:
#                 board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1
#             answer = max(board[r][c] , answer)
#     return answer**2
tc1 = [[0,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [0,0,1,0]]

tc2 = [[0,0,1,1],
       [1,1,1,1]]

tc3 = [[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]]
tc4 = [[1, 1, 1],
       [1, 1, 0],
       [1, 0, 0]]
# print(searching(0, 0, tc3, 3, 3))
# print(searching(0, 0, tc4, 3, 3))
# print(searching(0, 2, tc2, 2, 4))
print(solution(tc1))
# print(solution(tc2))
# print(solution(tc3))
