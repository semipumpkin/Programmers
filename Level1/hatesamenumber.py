def solution(arr):
    answer = [arr[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer += [arr[i]]
        
    return answer

a = [1,1,3,3,0,1,1]
b = [4,4,4,3,3]
print(solution(a))
print(solution(b))