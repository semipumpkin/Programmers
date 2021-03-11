def solution(strings):
    min_length = 1000000000000

    # 글자 수만큼 같은 것을 탐색
    for i in range(1, len(strings) + 1):
        temp = ''

        # 글자수는 i
        index = i

        # tmp의 끝 인덱스부터 i까지의 단어가 같다면
        tmp = strings[:i]
        count = 1
        while index <= len(strings):

            # tmp와 같을때까지 계속 반복문을 돌림
            while strings[index: index + i] == tmp:
                # count를 올려주고
                count += 1
                # 탐색 인덱스 초기화
                index += i


            # count가 2 이상이면 temp에 count를 담아줌
            if count >= 2:
                temp += str(count)
            # 숫자를 담아주고 tmp 문자를 담아줌
            temp += tmp

            # 그리고 새로운 tmp를 초기화 후
            tmp = strings[index: index + i]

            # 탐색 인덱스, count 초기화
            index += i
            count = 1

            # tmp로 할당되지 않은 문자들을 다 더해주고 반복문 종료
            if index > len(strings):
                temp += strings[index - i: ]

        # min_length 보다 작다면 len(temp)를 계속 갱신
        if len(temp) < min_length:
            min_length = len(temp)

    return min_length



print(solution('aabbaccc')) # 2a2ba3c
print(solution('ababcdcdababcdcd')) # 2ababcdcd
print(solution('abcabcdede')) # 2abcdede
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))