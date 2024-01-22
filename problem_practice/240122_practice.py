# 과제 1 : 1445. Str.count()
# 주어진 문자열에서 특정 문자의 개수를 세는 함수를 작성하시오.
# 문자열과 대상 문자를 인자로 받아 개수를 반환해야한다.
# def count_character(x, y):
#     num_char = x.count(y)
    
#     return num_char


# result = count_character("Hello, World!", "o")
# print(result)  



# 과제 2 : 1446. 최소 최대
# 아래 함수를 수정하시오.
# def find_min_max(num):
#     num.sort()
#     min = num[0]
#     max = num[-1]
#     return min, max
    
# def find_min_max(num):
#     find_min = min(num)
#     find_max = max(num)
#     return find_min, find_max

# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)



# 실습 1 : 1440. 메서드를 활용한 문자열 뒤집기
# 아래 함수를 수정하시오.
# def reverse_string(x):
#     reversed_join = ''.join(reversed(x))
#     return reversed_join


# result = reverse_string("Hello, World!")
# print(result)  # !dlroW ,olleH



# 실습 2 : 2995. 문자열과 리스트 메서드1
# N = 9
# data_1 = '123456789'
# arr_1 = []
# # 아래에 코드를 작성하시오.

# for i in range(N) :
#     arr_1.append(data_1[i])

# print(arr_1)


# M = 15
# data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# # 아래에 코드를 작성하시오.
# arr_2 = list(data_2.split())
# print(arr_2)

# for i in arr_2 :
#     if int(i) % 2 == 1 :
#         print(i)



# 실습 3 : 1468. 메서드를 활용한 중복 요소 제거
# 아래 함수를 수정하시오.
# def remove_duplicates(x):
#     new_list= [] 
#     for num in x :
#         if num not in new_list :
#             new_list.append(num)
#     return new_list


# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)



# 실습 4 : 2996. 문자열과 리스트 메서드2
# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# # 아래에 코드를 작성하시오.
# new_num = []
# for num in data_1 :
#     if num.isupper() == True or num == ' ' :
#         new_num.append(num)

# result = ''.join(new_num)
# print(result)

# # print()
# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# arr = []
# compared = ['내', '힘', '들', '다']
# for char in compared :
#     if char in data_2 :
#         arr.append(data_2.find(char))
#     elif char in data_2 :
#         arr.append(data_2.find(char))
#     elif char in data_2 :
#         arr.append(data_2.find(char))
#     elif char in data_2 :
#         arr.append(data_2.find(char))

# print(arr)

# # data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# # arr = []
# # compared = ['내', '힘', '들', '다']
# # for char in compared :
# #     if char in compared :
# #         arr.append(data_2[data_2.find(char)])      

# arr.sort()
# print(arr)
# for i in arr : 
#     print(data_2[i], end = '')



# 실습 5 : 1442. 튜플 요소 추가와 정렬 
# 아래 함수를 수정하시오.
# def sort_tuple(x):
#     new_tuple = sorted(x)
#     return new_tuple


# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)



# 실습 6 : 2997. 문자열과 리스트 메서드
#함수
# def restructure_word(word, arr) :
#     for word_element in word :
#         if word_element.isdecimal() == True : 
#             for i in range(int(word_element)) :
#                 arr.pop()
#         else :
#             arr.remove(word_element)
    
#     return arr
    
# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []
# arr.extend(original_word)
# print(arr)


# result = restructure_word(word, arr)
# full_sentence = ''.join(result)
# print(full_sentence)



# 실습 7 : 1443. Str.title()
# def capitalize_words(x):
#     new_words = x.title()
#     return new_words
    
# result = capitalize_words("hello, world!")
# print(result)



# 실습 8 : 1444. List.pop() List.extend()
# 리스트에서 홀수를 모두 제거하고, 짝수만 남긴 리스트를 반환하는 even_elements 함수 작성
# extend와 pop 활용
# def even_elements(my_list):
#     even = []
#     for my_list_element in my_list :
#         if my_list_element % 2 == 0 :
#             even.extend([my_list_element])
#     return even

# def even_elements(my_list):
#     even = []
#     while my_list : # my_list라는 변수를 넣는다는 것은 my_list라는 리스트의 요소가 존재할 때까지 돌린다는 의미
#         number = my_list.pop(0)
#         if number % 2 == 0 :
#             even.extend([number])
#     return even
 
            


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
