# 과제 1 : 1452. List를 set으로 형 변환
# # 아래 함수를 수정하시오.
# def remove_duplicates_to_set(elements):
#     element_list = set()
#     for element in elements :
#         element_list.add(element)
    
#     return element_list


# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)



# 과제 2 : Dict.update()

# 아래 함수를 수정하시오.
# def add_item_to_dict(my_dict, region, new_region):
#     new_dict = my_dict.copy()
#     new_dict.update({region : new_region})

#     return new_dict


# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)



# 실습 1 : 1447. 합집합 Set, union()
# def union_sets(x, y):
#     result = x.union(y)
#     return result




# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)


# 실습 2 : 2998. 세트와 딕셔너리
# my_set = {'가', '나', (0, 0)}
# my_dict = {
#         '가': 1, 
#         (0, 0): '튜플도 키값으로 사용가능'
#     }

# # 아래에 코드를 작성하시오.
# for key in my_set :
#     print(my_dict.get(key))

# # for var in my_set :
# #     my_dict.setdefault((1,2,3,'A'), '변수로도 키 설정 가능')

# var = (1, 2, 3, 'A')
# my_dict.update({var:'변수로도 키 설정 가능'})


# print(my_dict)


# 실습 3 : 1448. Dict.get()
# 아래 함수를 수정하시오.
# def get_value_from_dict(my_dict, name_key):
#     return my_dict.get(name_key)


# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result)  # Alice



# 실습 4 : 2999. 딕셔너리 메서드1
# data = {
#     '이름': '키위',
#     '종류': '새',
#     '원산지': '호주' 
# }

# plus_data = {
#     '종류': '과일',
#     '가격': 30000
# }
# # 1. data가 가진 모든 키와 벨류 목록을 출력한다.
# print(data.items())
# # 2. data가 가진 벨류 목록들만 모아서 출력한다.
# print(data.values())
# # 3. data에서 'without' 키가 가진 value를 출력한다.
#     # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
# print(data.get('without', 'unknown'))
# # 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
# data.update(plus_data)
# # 5. 변경된 data를 출력한다.
# print(data)



# 실습 5 : 1449. 교집합 set.intersection()
# def intersection_sets(x , y):
#     result = x.intersection(y)
#     return result
    


# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result)


# 실습 6 : 3000. 딕셔너리 메서드2
# data = [
#     {
#         'name': 'galxy flip',
#         'company': 'samsung',
#         'is_collapsible': True,
#     },
#     {
#         'name': 'ipad',
#         'is_collapsible': False
#     },
#     {
#         'name': 'galxy fold',
#         'company': 'samsung',
#         'is_collapsible': True
#     },
#     {
#         'name': 'galxy note',
#         'company': 'samsung',
#         'is_collapsible': False
#     },
#     {
#         'name': 'optimus',
#         'is_collapsible': False
#     },
# ]

# key_list = ['name', 'company', 'is_collapsible']

# # 아래에 코드를 작성하시오.
# for data_dict in data :
#     for key in key_list :
#         if data_dict.get('company') == None :
#             data_dict.setdefault('company' , 'unknown')
#             print(f'{key}는 {data_dict.get(key)}')
#         elif data_dict.get('company') != None :
#             print(f'{key}는 {data_dict.get(key)}입니다.')
#     print()




# 실습 7 : 1450. Dict.keys()
# 아래 함수를 수정하시오.
# def get_keys_from_dict(my_dict):
#     my_dict_keys= my_dict.keys()
#     keys = []
#     for key in my_dict_keys :
#         keys.append(key)

#     return keys

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)  # ['name', 'age']



# 실습 7 : 1451. set.difference()
# 아래 함수를 수정하시오.
# def difference_sets(x, y):
#     result =  x.difference(y)
#     return result


# result = difference_sets({1, 2, 3}, {3, 4, 5})
# print(result)


