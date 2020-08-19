import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://8division.com/brands.html',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기, 여기안에 50개가 들어가 있음(네이버 영화가 50개라고 하면), 적당히 중간에 있는 걸 찾아서, a(최종)를 이용해서 찾아보기
brands = soup.select('#contents')
#contents > div > div > div.brands-box.brands-A > a:nth-child(1)
#contents > div > div > div.brands-box.brands-D > a:nth-child(2)
#contents > div.shop-category > ul:nth-child(6) > li.shop-191 > a
#contents > div.brands > ul:nth-child(8) > li:nth-child(1) > p > a
#contents > div.brands > ul:nth-child(14) > li:nth-child(2) > p > a

# movies (tr들) 의 반복문을 돌리기
for brand in brands:
    # movie 안에 a 가 있으면,
    a_tag = brand.select_one('div.brands')
    if a_tag is not None:

        print(a_tag.text)

