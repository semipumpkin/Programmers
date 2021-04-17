def solution(m, musicinfos):
    result = []
    # 문자 하나당 1분
    strings = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        hour = abs(int(musicinfos[i][0][:2]) - int(musicinfos[i][1][:2]))
        play_time_total = abs(int(musicinfos[i][0][3:]) - int(musicinfos[i][1][3:])) + 60 * hour
        music_name = musicinfos[i][2]
        melody = musicinfos[i][3]

        play_time = len(melody) - melody.count('#')

        # 총 멜로디는 멜로디 타임 내에 멜로디가 쭉 반복
        # 총 재생시간 // 멜로디 재생시간을 나누고
        # 나머지 시간만큼 멜로디를 짤라서 이어붙임
        melodies = ''
        repeat = (play_time_total // play_time)
        melodies += repeat * melody

        rest_length = play_time_total - len(melody) * repeat
        for i in range(0, rest_length):
            if melody[i] != '#':
                if melody[i+1] == '#':
                    melodies += melody[i] + '#'
                else:
                    melodies += melody[i]

        # print(melodies)

        # m을 멜로디 안에서 탐색
        # m이 #로 끝나지 않을때, m뒤에 #이 붙은 경우 answer에 더하지 않도록 조건 추가
        for k in range(len(melodies) - len(m)):
           if melodies[k: k+len(m)] == m and melodies[k+len(m)] != '#':
               result.append([play_time, music_name])

               break
    # print(result)
    answer = ''
    if len(result) == 0:
        answer += '(None)'
    else:
        answer += max(result)[1]

    # answer = result[0]
    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "WORLD"
    # 시작시간 # 끝난시간 # 곡제목 # 악보정보
T = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# T.split(',')
for string in T:
    string.split(',')

