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
def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user_info = {'name' : name, 'age' : age, 'address' : address}
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))
info = list(map(lambda x: {'name':x['name'],  'age':x['age']}, many_user))

print(info)
def rental_book(info):
    # info = {'name': name, 'age' : age}
    number = info['age']//10
    name = info['name']
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book-=number
    print('남은 책의 수 :', number_of_book)
    return number_of_book

rental = rental_book({'name': '홍길동', 'age' : 30})
list(map(rental_book, info))