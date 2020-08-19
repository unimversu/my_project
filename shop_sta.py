import requests  # requests 라이브러리 설치 필요

# requests 를 사용해 요청(Request)하기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response_data = requests.get('http://stable.kr/exec/front/Product/SubCategory',headers=headers)
# 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
brand_list = response_data.json()


for brand in brand_list:
    if brand['parent_cate_no'] == 209:
        print(brand['name'], brand['param'])

#pont color red는 강조하는 문법
#처음에는 서울시 미세먼지 api하는 것처럼 가져왔지만, 막혔었음! -> header(크롤링 막는 걸 속이는 방법)을 사용하니깐 뚫렸다~
