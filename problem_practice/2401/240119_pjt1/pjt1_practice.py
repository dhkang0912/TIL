# 라이브러리 : 남들이 만들어놓은 코드를 가져다가 쓰자!
# 데이터를 가져오는 python 라이브러리 : requests
# 파이썬 패키지 관리 (가져온 피키지를 관리해줌) : pip 
    # 설치 : pip install <패키지 이름>
    # 목록 확인 : pip list
    # import 모듈

# 파이썬은 원래 내 파일에 있는 것을 먼저 검색하고, 내장모듈을 검색함
# 그러나 설치한 패키지는 위와 같이 검색이 안됨 -> import를 해야함


import requests

url = 'https://fakestoreapi.com/carts'
# data = requests.get(url)
data = requests.get(url).json()

# 모듈에서 만들어진 기능을 가져와서 쓰는 것이 .을 붙이는 것, 
    # requests 모듈에서 무언가를 가져와라, 해당 데이터로 부터 주소를 가져와라
    # .json()은 보기 좋게 하기 위해 json 타입으로 가져와라

print(data)

