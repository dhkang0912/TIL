############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    end_char = user['id'][-1]
    try :
        if 0 <= int(end_char) <= 9 :
            result = True
        else :
            result = False
    except ValueError:
        # try - except는 사실 시험 범위에 안 들어가는데, 
        # 이걸 안 쓰고 푸는 방법이 있을텐데 뭐가 있을까?
        result = False

    
    return result
        
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################