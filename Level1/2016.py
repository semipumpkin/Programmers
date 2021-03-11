def solution(a, b):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    # 7로 나눴을때 나머지가 0이면 목요일이기 때문에 리스트의 첫번째 요소를 THU로 했습니다.
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    for i in range(1, a + 1):
        days = sum(months[: i]) + b
    return day[(days % 7)]
# print(solution(5, 24))
for i in range(5)
awef    
qwd