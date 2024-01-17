# 2215. 덧셈 함수
# def add_numbers(a , b):
#     return a + b



# # 수정한 add_numbers() 함수를 호출하시오.
# print(add_numbers(3, 5))


# 2216. 다양한 built in-function
# # 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
# negative = -3
# print(abs(negative))


# # 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
# empty_list = []
# print(bool(empty_list))


# # 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))


# # 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
# unsorted_list = ['하', '교', '캅', '의', '지', '가']
# print(sorted(unsorted_list))


# 1680. 신규 고객 증가
# 어떻게 만들 것인가?
    # 1. increase_user라는 함수 정의
        # 1-1. global number_of_people을 불러옴
        # 1-2. number_of_people은 1씩 증가
        # 1-3. print('현재 가입된 유저 수 :', number_of_people)

# number_of_people = 0


# def increase_user():
#     global number_of_people
#     number_of_people += 1

# increase_user()
# print('현재 가입된 유저 수 :', number_of_people)


# 2988. 함수 연습하기
# def my_multi(number_1, number_2):
#     result_1 = number_1 * number_2
#     return result_1

# print(my_multi(2, 3))
# # my_multi(2, 3) 결과 : 6
# # 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


# def is_negative(number):
#     if number <= 0 :
#         return True
#     else : 
#         return False

# result_2 = is_negative(3)

# print(result_2)

# # is_negative(3) 결과 : False
# # # 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


# def default_arg_func(default = '기본 값'):
#     return default

# result_3 = default_arg_func()
# result_4 = default_arg_func('다른 값')

# print(result_3)
# print(result_4)


# 1681. 신규 고객 등록과 환영 인사

# 1. increae_user 함수를 정의()
    # 1-1.현재 가입된 유저의 수를 +1하여 저장
    # 1-2. 저장된 최근 유저의 수를 프린트
    # 1-2. return 


# 2. create_user(name, age, address) 함수를 정의
    # 1-1. increase_user 함수를 호출
    # 1-2. user_info에 값을 할당
    # 1-3. 할당된 user_info를 딕셔너리로 반환
    # 1-4. print(f'{name}님 환영합니다!')


# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1
    
# def create_user(name, age, address) :
#     print('현재 가입된 유저 수 :', number_of_people)
#     increase_user()
#     print(f'{name}님 환영합니다!')
#     user_info = {'name' : name, 'age' : age, 'address': address}
#     print(user_info)
#     print('현재 가입된 유저 수 :', number_of_people)


# create_user('홍길동', 30, '서울')
# create_user('김민영', 27, '광주')


# 2989. 함수 활용하기
# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# def create_data(subject, day, title = None) :
#     global pro_num
#     pro_num += 1
#     data = {'과목' : subject, '일차' : day, '제목' : title, '문제 번호' : pro_num}
#     return data

# result_1 = create_data('python', 3)

# result_2 = create_data(subject='web', day=1, title='web 연습하기')

# result_3 = create_data(**global_data)

# print(result_1)
# print(result_2)
# print(result_3)


# 1682. 도서 대여 서비스
# number_of_book = 100

# def decrease_book(num):
#     global number_of_book
#     number_of_book -= num
#     print('남은 책의 수 :', number_of_book)
#     # return number_of_book

# def rental_book(name , num):
#     print(f'{name}님이 {num}권의 책을 대여하였습니다')
#     decrease_book(num)

# rental_book('홍길동', 3)
# rental_book('강두홍', 2)


# 1683. 대규모 신규 고객 등록
# def create_user(name, age, address) :
#     print(f'{name}님 환영합니다!')
#     user_info = {'name' : name, 'age' : age, 'address': address}
#     return user_info
#     # print(user_info)



# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# t = list(map(create_user, name, age, address))
# print(t)


# 1684. 대규모 도서 대여 서비스
# def create_user(name, age, address):
#     print(f'{name}님 환영합니다!')
#     user_info = {'name' : name, 'age' : age, 'address' : address}
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# many_user = list(map(create_user, name, age, address))
# info = list(map(lambda x: {'name':x['name'],  'age':x['age']}, many_user))

# print(info)
# def rental_book(info):
#     # info = {'name': name, 'age' : age}
#     number = info['age']//10
#     name = info['name']
#     decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')

# number_of_book = 100

# def decrease_book(number):
#     global number_of_book
#     number_of_book-=number
#     print('남은 책의 수 :', number_of_book)
#     return number_of_book

# rental = rental_book({'name': '홍길동', 'age' : 30})
# list(map(rental_book, info))


# 2990. 재귀 함수 만들기
# def recur_example(number):
#     '''
#         함수(2) 실행
#             number에 2 할당
#             if 2 == 1 조건문 만족하지 않음
#             else문 2 + 함수(2-1) 
#                 결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

#                 함수(2-1) 실행
#                     number에 1 할당
#                     if 1 == 1 조건문 만족하므로 1 반환
            
#             else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
#             2 + 1 반환
#         결과 : 3  
#     '''
#     if number == 1:
#         return 1
#     else:
#         return number + recur_example(number - 1)
# result_1 = recur_example(5)
# print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# # 거듭 제곱 재귀 함수
# # base = 밑, exponent = 지수
# # base의 exponent승 == 2의 3승
# def power(base, exponent):
#     '''
#         함수(2, 3) 실행
#             base에 2 할당, exponent에 3할당
#             지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

#             아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
#                 2 * 함수(2, 3-1)

#             모든 상황을 반복하는 과정
#             2 * (2 * (2 * 1))  
#             결과 : 8
#     '''
#     if exponent == 0 : 
#         return 1
#     else:
#         return base * power(base, exponent - 1)
#         # 헷갈렸던 부분 : 
#         # 첫번째 입력 값은 사실 상 else에 걸려서 else에서 재귀함수를 호출하고 있는 것!! 그렇기 때문에 안에서만 if가 다시 평가됨
#         # 내가 헷갈린 부분은 언제가는 exponent가 0이 되어서 return이 1이 되는 것인 줄 착각함 (그냥 단순 반복문 개념을 생각함)
#         # 그러나 재귀함수는 들여쓰기가 된 상태에서 깊이가 생겨 반복이 되기 때문에 안의 안의 안... 이런 식으로 반복이 되어 중복될 일이 없음, 특정 조건에 달하면 마지막 부분이 return되면서 그 값이 나올 뿐

# result_2 = power(2, 3)
# print(result_2) # 2 * 2 * 2 * 1 = 8

# # 모든 자릿수 더하기 함수
# def sum_of_digits(number):
#     '''
#         함수(321) 실행
#         number가 10 미만인 경우, number 반환

#         아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
#             number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
#             1 + (321 // 10)

#         모든 상황을 반복하는 과정
#         1 + 2 + 3
#         결과 : 6
#     '''
#     if number < 10:
#         return number
#     else:
#         return (number % 10) + (sum_of_digits(number // 10))
# result_3 = sum_of_digits(321)
# print(result_3) # 1 + 2 + 3 = 6

# https://dojang.io/mod/page/view.php?id=2352
# 재귀함수 이해를 위해 해당 설명을 확인함
# 재귀함수 = 재귀호출을 종료 시점을 정하여 그때까지 반복해서 해줌




# 어려웠던 부분 다시 문제 풀어보기!!!
# 1684. 대규모 도서 대여 서비스
# - 문제 
    # 실습 4에서 작성한 코드를 활용하여 many_user 변수에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당한다.
        # 1. create_user 함수를 활용해서 user_info를 값으로 반환 받는다
    # 실습 3에서 작성한 코드를 활용하여 decrease_book 함수를 작성한다.
    # rental_book 함수는 info 인자 하나만 할당 받을 수 있다.
        # info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리이다.
        # 신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용한다. (decrease_book 함수의 인자)
        # info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성한다.
            # 이 때, map에 사용될 함수는 lambda로 구현한다.
            #  그 결과를 rental_book 함수에 각각 전달하여 호출한다. 이 때 역시 map 함수를 사용한다.





def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user_info = {'name' : name, 'age' : age, 'address' : address}
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book-=number
    print('남은 책의 수 :', number_of_book)
    return number_of_book

# rental_book 함수는 info 인자 하나만 할당 받을 수 있다.
        # info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리이다.
        # 신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용한다. (decrease_book 함수의 인자)
        # info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성한다.
            # 이 때, map에 사용될 함수는 lambda로 구현한다.
            #  그 결과를 rental_book 함수에 각각 전달하여 호출한다. 이 때 역시 map 함수를 사용한다.

def rental_book(info) :
    decrease_book(info['age'] // 10) # 대여할 책의 수
    print(f'{info['name']}님이 {info['age'] // 10}권의 책을 대여하였습니다.')

user_info_list = list(map(lambda new_user_info : {'name' : new_user_info['name'], 'age' : new_user_info['age']}, many_user))
map(rental_book, user_info_list)



# def create_user(name, age, address):
#     print(f'{name}님 환영합니다!')
#     user_info = {'name' : name, 'age' : age, 'address' : address}
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# many_user = list(map(create_user, name, age, address))
# info = list(map(lambda x: {'name':x['name'],  'age':x['age']}, many_user))

# print(info)
# def rental_book(info):
#     # info = {'name': name, 'age' : age}
#     number = info['age']//10
#     name = info['name']
#     decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')

# number_of_book = 100

# def decrease_book(number):
#     global number_of_book
#     number_of_book-=number
#     print('남은 책의 수 :', number_of_book)
#     return number_of_book

# rental = rental_book({'name': '홍길동', 'age' : 30})
# list(map(rental_book, info))

