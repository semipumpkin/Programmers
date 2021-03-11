def solution(strings, n):
    nth = ''
    # n번째 문자 정렬
    for word in strings:
        nth += word[n]
    ordered = sorted(nth)
    sorted_strings = sorted(strings)
    # strings의 문자열들을 미리 정렬해서 n번째 문자가 같더라도 사전순으로 배치되도록 함
    # ordered의 문자를 하나씩 돌면서 sorted_strings중에 n번째 문자가 같으면 answer에 추가
    answer = []
    for i in range(len(ordered)):
        for j in range(len(sorted_strings)):
            if ordered[i] == sorted_strings[j][n] and sorted_strings[j] not in answer:
                answer += [sorted_strings[j]]
        
    return answer
print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))