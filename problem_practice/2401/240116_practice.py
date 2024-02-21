# 2213. 간단한 형 변환 -> 과제 1
# book = '1'
# book = int(book)

# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(book * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# rental = int(rental)
# print(changes)
# print(total - rental)


# 2214. 중복 작가 제거하기 -> 과제 2
# authors = [
#     '작자 미상',
#     '이항복',
#     '임제',
#     '임제',
#     '조성기',
#     '조성기',
#     '조성기',
#     '임제',
#     '허균',
#     '허균',
#     '허균',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '박지원',
#     '이항복',
#     '남영로',
#     '남영로',
#     '남영로',
#     '이항복',
#     '임제',
#     '임제',
# ]
# authors = list(set(authors))
# print(authors)


# 1673. escape sequence 낙화 
# '''
# 다음은 이형기 시인의 "낙화"의 한 구절이다.
# - 1연
# 	가야할 때 언제인가를
# 	분명히 알고 가는 이의
# 	뒷모습은 얼마나 아름다운가.

# 나는 이 시를 보며 '나는 내가 가야할 때가 언제일까?' 를 생각해 보았다.
# '''

# print('다음은 이형기 시인의 \"낙화\"의 한 구절이다.\n\
# - 1연 \n\
#       가야할 때 언제인가를 \n\
#       분명히 알고 가는 이의 \n\
#       뒷모습은 얼마나 아름다운가\n\
#       \n\
# 나는 이 시를 보며 \'나는 가야할 때가 언제일까?\'를 생각해보았다')


# 2985. 리스트 활용하기
# zero_list = [0]
# print(zero_list)
# many_zero_list = zero_list*250000
# print(len(many_zero_list))
# numbers = list(range(1,11))
# print(numbers)
# print(numbers[3:])


# 1674. 책 제목과 작성자 함께 출력하기
# 책 한 권당 print문을 한 번씩만 사용한다.
# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고, \n{author_2}은 {book_2}를 집필하였다')

# 2986. 딕셔너리 활용하기
# title = '딕셔너리 활용하기'
# data = {'과목': 'python', '구분' : '실습', '단계' : '2', '문제번호' : '3251', '이름' : None, '일차' : 22 }
# print(data)
# data['단계'] = str(data['단계']) + '단계'
# data['이름'] = title
# data['일차'] -= 20
# print(data)


# 1675. 도서 목록 정리하기
# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(f'{authors[1]} : {books[3]} \n{authors[3]} : {books[1]} \n{authors[0]} : {books[2]} \n{authors[2]} : {books[0]} \n{authors[-1]} : {books[-1]} ')


# 2987. 복잡한 자료구조

# 1677. 깊은 복사와 indexing 접근
catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

backup_catalog = catalog

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print(catalog == backup_catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)

