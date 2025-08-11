############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def turn(temperature_list):
    # 여기에 코드를 작성합니다.
    maximum_list = []
    minimum_list = []
    for max_num in temperature_list :
        maximum_list.append(max_num[0])
    
    for min_num in temperature_list :
        minimum_list.append(min_num[1])
    
    all_list = {}
    all_list.update({'maximum' : maximum_list, 'minimum' : minimum_list})
    # 다 잘 짜놓고 어째서 변수를 정확하게 안 적어줘서 다른 결과값이 나오게 하는거야...
    # 그렇게 짜더라도 값이 이상하면 차근차근 뇌디버깅해서 에러 알아내야하는데 그게 아직도 잘 안된다

    return all_list


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
temperatures1 = [
    #최대온도, 최소온도
    [9, 3],
    [9, 0],
    [11, -3],
    [11, 1],
    [8, -3],
    [7, -3],
    [-4, -12]
]
print(turn(temperatures1)) 
# {'maximum': [9, 9, 11, 11, 8, 7, -4], 'minimum': [3, 0, -3, 1, -3, -3, -12]}
#####################################################