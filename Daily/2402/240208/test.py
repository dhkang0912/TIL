lines = [
    "AABCDD",
    "afzz",
    "09121",
    "a8EWg6",
    "P5h3kx"
]

# 각 줄에서 최대 길이 구하기
max_length = max(len(line) for line in lines)

# 각 줄을 최대 길이로 맞추기
padded_lines = [line.ljust(max_length) for line in lines]
print(padded_lines)

# 각 열을 순회하며 문자열 조합
result = ""
for i in range(max_length):
    for line in padded_lines:
        result += line[i]

# 결과 출력
print(result)
