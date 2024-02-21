# 어려우면 무조건 더 쪼개서 생각하기
# 차근 차근 대입해보면서 컴퓨터처럼 돌아가며 생각해보기


# 과제 1 : 2217. 대여 불가 도서 구분하기
# 보유 중인 도서
# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]

# # 대여 중인 도서
# rental_list = [
#     '장생전',
#     '원생몽유록',
#     '이생규장전',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]

    
        
# rental_list 요소를 반복함
# 보유 중인 포함되지 않은 요소가 발견되면
    # {}는 보유하고 있지 않습니다 프린트
# 포함되지 않은 요소가 없으면
    # {}는 보유하고 있지 않습니다 프린트
# 결국 rental_list의 요소 한개와 list_of_book의 요소들 각각을 비교하는 과정이 반복하여 필요함
# 문구 출력 후 반복문 종료

# 만약 모든 도서를 보유하고 있으면 도서가 대여 가능한 상태입니다 출력

# check = True
# for rental_list_element in rental_list :
#     if rental_list_element not in list_of_book :
#         check = False
#         print(f'{rental_list_element} 은/는 보유하고 있지 않습니다.')
#         break

# if check : 
#     print('모든 도서가 대여 가능한 상태입니다.')




# 과제 2 : 2218. 대여 불가 도서 관리하기
# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]

# rental_book = [
#     '장생전',
#     '위대한 개츠비',
#     '원생몽유록',
#     '이생규장전',
#     '데미안',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]

# 1. rental_list과 list_of_book의 요소를 비교한다.
    # 1). for문을 활용하여 rental_list_element에다가 rental_book 리스트 요소를 순서대로 담는다.
        #1-1). 만약 도서를 보유하지 않고 있다면, rental_list_element가 list_of_book에 없다면 (not in)
            #1-1-1. rental_list_element를 missing_book 리스트에 담는다
        #1-2). 만약 도서를 보유하고 있다면 '모든 도서가 대여 가능한 상태입니다.'를 출력한다.
# 3. 모든 도서를 보유하고 있다면 모든 도서가 대여 가능한 상태입니다.를 출력한다.
# 4. for문을 이용하여 missing_book_element에 missing_book를 길이만큼 반복하여
    #{도서명}을 보충하여야 합니다.를 출력한다.

# check = False
# missing_book = [missing_book_element for missing_book_element in rental_book if missing_book_element not in list_of_book]
# for print_missing_book in missing_book :
#     check = False
    # print(f'{print_missing_book} 을/를 보충하여야 합니다.')

# for rental_book_element in rental_book :
#     if rental_book_element in list_of_book :
#         check 
#         print('모든 도서가 대여 가능한 상태입니다.')
#     break

# missing_book = []
# for rental_book_element in rental_book :
#     if rental_book_element not in list_of_book :
#         missing_book.append(rental_book_element)

# print(missing_book)


#---
# check = True
# missing_book = [book for book in rental_book if book not in list_of_book]
# for missing_book_element in missing_book :
#     check = False
#     print(f'{missing_book_element} 을/를 보충하여야 합니다.')

# if check :
#     print('모든 도서가 대여 가능한 상태입니다.')
#---

#---
# list_of_book = []
# rental_book = []
# missing_book = [book for book in rental_book if book not in list_of_book]

# if missing_book:
#     for missing in missing_book :
#         print(f'{missing}을/를 보충하여야 합니다')
# else : 
#     print('모든 도서가 대여 가능한 상태입니다.')
#---




# 실습 1 : 1687. 도서관 사용자 관리 서비스 - 사전 준비 서비스
# import requests
# from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])

# print(parsed_data['company']['name'])



# 실습 2 : 2991. 모듈 연습
# from conf import settings
# from utils import create_url

# print(create_url.create_url(settings.NAME, settings.MAIN_URL))



# 실습 3 : 1688. 도서관 사용자 관리 서비스 - 데이터 수집
# import requests
# from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# # parsed_data = response.json()

# # 응답 데이터 출력
# # print(parsed_data)

# # 총 10명의 데이터를 요청한다
# dummy_data = []
# for i in range(1, 11) :
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
#     response = requests.get(API_URL)
#     user_data = response.json()
#     dummy_data.append(user_data['name'])

# print(dummy_data)



# 실습 4 : 2993. 함수와 제어문 연습



# 실습 5 : 1689. 도서관 사용자 관리 서비스 - 데이터 처리
# import requests
# from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# # parsed_data = response.json()

# # 응답 데이터 출력
# # print(parsed_data)

# 총 10명의 데이터를 요청한다
# dummy_data = []
# for i in range(1, 11) :
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
#     response = requests.get(API_URL)
#     user_data = response.json()
#     # dummy_data.append(user_data['name'])

#     # print(user_data)
#     name = user_data['name']
#     lat = user_data['address']['geo']['lat']
#     lng = user_data['address']['geo']['lng']
#     company_name = user_data['company']['name']

#     info ={'name' : name, 'lat' : lat, 'lng' : lng, 'company_name' : company_name}
#     # print(name, lat, lng, company_name )
#     if -80 < float(lat) < 80 and -80 < float(lng) < 80 :
#         dummy_data.append(info)

# print(dummy_data)


# 실습 6 : 2994. 중첩 리스트 순회 연습
matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

matrix_len = 0
for _ in matrix :
    # print(number)
    matrix_len += 1
print(matrix_len)

# for i in range(matrix_len) :
#     print(matrix[i])

for number in matrix :
    print(number)
    temporary_len = 0
    for _ in number :
        temporary_len += 1
    # print(number, temporary_len)
    if temporary_len <= 4 :
        print(f'{number}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for x in range(len(matrix)) :
    for y in range(len(matrix[x])) :
        print(f'matrix의 {x} {y}번째 요소의 값은 {matrix[x][y]} 입니다.')
