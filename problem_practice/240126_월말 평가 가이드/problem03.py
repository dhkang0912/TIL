############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count() 를 사용시 감점
def menu_count(restorant_dict):
    cnt = 0
    for menu in restorant_dict['menus'] :
        cnt +=1
    # count = len(restorant_dict['menus'])

    return cnt

    # for menu in restorant_dict.get()
    #     cnt += 1
    # return cnt
    
    # 여기에 코드를 작성합니다.
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
restorant1 = {
    "id": 11,
    "user_rating": 5.5,
    "name": "김밥나라",
    "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
    "location": "서울특별시 강남구 역삼동 123-123"
}
print(menu_count(restorant1)) # 4
#####################################################