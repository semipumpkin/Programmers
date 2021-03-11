def solution(board, moves):
    # 뽑은 인형들을 stack에 저장
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                stack += [board[i][move - 1]]
                board[i][move - 1] = 0 
                break
    
    # 중복된 인형을 터뜨리는 과정
    count = 0
    while True:
        for i in range(len(stack)-1): 
            if stack[i] == stack[i + 1]:    
                stack.pop(i + 1)               
                stack.pop(i)             
                count += 2             
                break
        else:
            break
            
    return count

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]
print(solution(a,b))