def dec_to_124(n):
    answer = ''
    strange_dict = {1: '1', 2: '2', 0: '4'}
    while n >= 1:
        answer = strange_dict[n%3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
    return answer

for i in range(1, 11):
    print(dec_to_124(i))

'''
1        1
2        2 
3        4
4        11
5        12
6        14
7        21
8        22
9        24
10       41
'''