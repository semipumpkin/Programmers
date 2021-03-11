def solution(dartResult):
    # '*' = 해당 점수와 바로 전에 얻은 점수를 각 2배
    # '#' 해당 점수가 - 됨
    # '*' 첫번째에 스타상이나오면 첫번째 점수만 2배
    # '*'의 효과는 것과 중첩 가능
    # '#'와도 중첩가능
    # 라운드마다 둘중 하나만 존재


    answer = 0
    stack = []
    stack2 = []
    for i in range(len(dartResult) - 1):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit() == False:
            if dartResult[i] != '0':
                stack.append(int(dartResult[i]))
        elif dartResult[i].isdigit() and dartResult[i+1].isdigit():
            stack.append(int(dartResult[i] + dartResult[i+1]))
        else:
            stack2.append(dartResult[i])
    stack2.append(dartResult[-1])
    for i in range(len(stack2)):
        if stack2[i] == 'S':
            stack.append(stack.pop(0) ** 1)
        elif stack2[i] == 'D':
            stack.append(stack.pop(0) ** 2)
        elif stack2[i] == 'T':
            stack.append(stack.pop(0) ** 3)
        # print(stack)
        elif stack2[i] == '*':
            stack[-1] = stack[-1] * 2
            stack[-2] = stack[-2] * 2
        elif stack2[i] == '#':
            stack[-1] = stack[-1] * (-1)
    if dartResult[2] == '*':
        stack[2] = stack[2] / 2
    return int(sum(stack))


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))