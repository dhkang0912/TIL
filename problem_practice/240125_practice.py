# 과제 1 : 1466. 음수 양수 0 예외 처리

# 아래 함수를 수정하시오.
# def check_number():
#     try : 
#         num = int(input('숫자를 입력하세요 : '))
#         if num > 0 :
#             print('양수입니다.')
#         elif num < 0 :
#             print('음수입니다.')
#         elif num == 0 :
#             print('0입니다.')
#     except ValueError :
#         print('잘못된 입력입니다.')


# check_number()


# 과제 2 : 1467. 사용자 정보 클래스 예외 처리
# 아래 클래스를 수정하시오.
# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

#     def get_user_info(self):
#         self.user_data['name'] = input('이름을 입력하세요 : ')
#         try :
#             self.user_data['age'] = int(input('나이를 입력하세요 : '))
#         except ValueError :
#             print('나이는 숫자로 입력해야 합니다.')
#         # name = input('이름을 입력하세요 : ')
#         # try :
#         #     age = int(input('나이를 입력하세요 : '))
#         #     self.user_data = {'이름' : name, '나이' : age}
#         # except ValueError :
#         #     print('나이는 숫자로 입력해야 합니다.')

#     def display_user_info(self):
#         if self.user_data['name'] == '' or 'age' not in self.user_d:
#             print('사용자 정보가 입력되지 않았습니다.')
#         else:
#             print(f'사용자 정보: \n이름 : {self.user_data["name"]} \n나이 : {self.user_data["age"]}')

# user = UserInfo()
# user.get_user_info()
# user.display_user_info()



# 실습 1 : 1461.Animal 클래스 정의
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0



# class Dog(Animal):
#     def __init__(self):
#         Animal.num_of_animal += 1


# class Cat(Animal):
#     def __init__(self):
#         Animal.num_of_animal += 1
        


# class Pet(Animal):
#     def __init__(self):
#         self.access_num_of_animal = 0
#         super().__init__() 
    
#     @classmethod
#     def access_num_of_animal(cls) :
#         return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'
        


# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())



# 실습 2 : 1461.Animal 클래스 정의
# data = {'name': '홍길동'}
# # if not data['age']:
# #     print(data['age'])
# # else:
# #     print('data에는 age라는 키가 없습니다.')
# #     data['age'] = 30
# #     print(data)
# # 아래에 코드를 작성하시오.
# try :
#     print(data['age'])
# except KeyError :
#     print('data에는 age라는 키가 없습니다.')
#     data.update({'age' : 16})
#     print(data)


# # arr = ['반갑', '하세요', '안녕']
# # for i in range(4):
# #     print(arr.pop())
# # print(arr)

# # 아래에 코드를 작성하시오.
# arr = ['반갑', '하세요', '안녕']
# try : 
#     for i in range(4):
#         print(arr.pop())
#     print(arr)
# except IndexError :
#     print('더 이상 pop 할 수 없습니다.')



# # word = '3.15'
# # print(int(word))
# # 아래에 코드를 작성하시오.

# try :
#     word = '3.15'
#     print(int(word))
# except ValueError :
#     print('정수로 변환 가능한 값을 입력해주세요')



# 실습 3 : 1462. Animal 클래스 상속 Dog 클래스
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0

# class Dog(Animal):
#     def bark(self) :
#         print('멍멍!')


# dog1 = Dog()
# dog1.bark()



# 실습 4. 3005. 상속의 이해
# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         self.author = author
#         super().__init__(data_type, title, content, created_at, updated_at)
    
# class Other(BaseModel):
#     TYPE = 'Other Model'
#     # def __init__(self, data_type, title, content, created_at, updated_at):
#     #     super().__init__( data_type, title, content, created_at, updated_at)
#     #     self.TYPE = 'Other Model'
    
#     def save(self) :
#         print('데이터를 다른 장소에 저장합니다.')
    


# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)



# 실습 4 : 1463. Animal 클래스 상속 Cat 클래스
# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0


# class Cat(Animal):
#     def __init__(self, sound) :
#         self.sound = sound
    
#     def meow(self) :
#         print(f'self.sound!')

# cat1 = Cat("야옹")
# cat1.meow()




# 실습 5. 3006. 상속의 이해
class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        self.author = author
        super().__init__(data_type, title, content, created_at, updated_at)
    
class Other(BaseModel):
    TYPE = 'Other Model'
    # def __init__(self, data_type, title, content, created_at, updated_at):
    #     super().__init__( data_type, title, content, created_at, updated_at)
    #     self.TYPE = 'Other Model'
    
    def save(self) :
        print('데이터를 다른 장소에 저장합니다.')

class ExtendModel (Novel, Other) :
    # TYPE = 'extended_type'
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type
        

    def display_info (self) :
        print(f'PK : {self.PK}, TYPE : {self.TYPE}, Extended Type : {self.extended_type}')    

    
    def save(self) :
        print('데이터를 확장하여 저장합니다.')


# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)
        

#새로운 모델 인스턴스 생성
extended_instance = ExtendModel('확장', '확장 모델', '모델 내용', 2022, 2024, '확장 작가', 'Extended Type')

# 새로운 모델의 메서드 호출
print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
extended_instance.display_info()
extended_instance.save()
