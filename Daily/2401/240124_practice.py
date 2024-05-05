# 과제 1 : 1459. 반복 출력 메서드
# class StringRepeater:
#     def repeat_string(self, num, my_str) :
#         for _ in range(num) :
#             print(my_str)    

# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")



# 과제 2 : 1460. 자기소개 클래스
# 아래 클래스를 수정하시오.
# class Person:
#     number_of_people = 0
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
#         Person.number_of_people += 1
    
#     def introduce(self) :
#         print(f'제 이름은 {self.name}이고, 저는 {self.age}입니다.')

        

# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)



# 실습 6 : 3003. 자동차 클래스 정의하기
# 클래스를 만든다 = 타입을 만들다라고 생각하면 좀 쉬움
# 인스턴스는 그 객체 (타입의 객체)

# class Car:
#     wheels = 4 #클래스의 속성
#     # 아래에 코드를 작성하시오.
#     def __init__(self, engine, driving_system, sound) :
#         self.engine = engine
#         self.driving_system = driving_system
#         self.sound = sound
    
#     def __str__(self):
#         return self.engine
    
#     def drive(self) :
#         print(self.sound)
#         return self.engine
    
#     def introduce(self) :
#         print(f'제 차의 엔진은 {self.engine}방식이고, {self.driving_system} (으)로 동작합니다.')
    
#     @classmethod # 클래스의 속성을 가지고 액션하는 것, 클래스 속성이 영향을 받음
#     def increase_wheels(cls) :
#         cls.wheels += 1
#         print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1 증가하였습니다.')
    
#     @staticmethod # 클래스, 인스턴스 어디에도 영향 받지 않음, 그 외적으로 가지는 행동
#     def description() :
#         print('자동차(自動車, 영어: car, automobile)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.')




# car1 = Car('gasoline', '후륜구동', '부릉부릉')
# # 변수 = 클래스 이름인 경우 def에서 자기 자신을 먼저 불러옴
# car2 = Car('diesel', '전륜구동', '달달달달')
# car3 = Car('hybrid', '4wd', '슈웅')

# car1.drive()
# print(car2.drive())

# print('===')
# car1.introduce()
# car3.introduce()

# print('===')
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.increase_wheels()
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')



# 실습 1 : 1454. Shape 클래스
# main.py


# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height


# shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)



# 실습 2 : 3001. 클래스와 메서드 이해하기
# 아래에 코드를 작성하시오.
# my_list = [1, 2, 3]
# my_dict = {'A': 1, 'B': 2, 'C': 3}

# print(dir(my_list))
# print(dir(my_dict))

# help(my_list)
# help(my_dict)



# 실습 3 : 1455. Shape 클래스 넓이 메서드
# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height) :
#         self.width  = width
#         self.height = height 
    
#     def calculate_area(self) :
#         area = self.width * self.height
#         return area


# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)



# 실습 4 : 3002. 신화 클래스 정의하기
# class Myth :
#     type_of_myth = 0

#     def __init__(self, myth_name) :
#         self.name = myth_name
#         Myth.type_of_myth += 1
        
#     @staticmethod
#     def description() :
#         print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다')


# myth1 = Myth('dangun')
# myth2 = Myth('greek & rome')
# print(myth1.name)
# print(myth2.name)
# print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
# Myth.description()



# 실습 5 : 1456. Shape 클래스 둘레 메서드
# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
    
#     def calculate_perimeter(self) :
#         result = (self.width + self.height) * 2
#         return result

# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)



# 실습 6 : 1457. Shape 클래스 정보 출력 메서드
# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
        

#     def print_info(self):
#         Area = self.width * self.height
#         Perimeter = (self.width + self.height) * 2
#         print(f'Width : {self.width} \nHeight : {self.height} \nArea : {Area} \nPerimeter : {Perimeter}')
        


# shape1 = Shape(5, 3)
# shape1.print_info()



# 실습 7 : 1458. Shape 클래스 매직 메서드 __str__
# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height

#     def __str__(self) :
#         return f'Shape: width={self.width}, height={self.height}'


# shape1 = Shape(5, 3)
# print(shape1)
