############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_user_data_valid(user):
    # 여기에 코드를 작성합니다.
    if user['id'] == '' or user['password'] == '':
        # 데이터 구조를 먼저 잘 보고 하자, 자꾸 딕셔너리를 그냥 불러오면 되는데
        # 중첩 딕셔너리인 줄 알고 for문 써서 불러오려고 한다. 그럴 필요 없는 문제였음
        status = False
    else :
        status = True
    # 추가적인 조건이 있다면 여기에 추가할 수 있습니다.
    return status
    




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 

user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################