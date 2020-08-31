from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.myproject

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/click', methods=['GET'])
def click_brand():
    brand_receive = request.args.get('brand_give')
    url = db.brand_db.find_one({'brand': brand_receive}, {'_id': False, 'site': False})['url'],

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')
    og_image = soup.select_one('meta[property="og:image"]')

    doc = {
        'url': url,
        'title': og_title['content'],
        'desc': og_description['content'],
        'image': og_image['content']
    }


    return jsonify({'result': 'success', 'brand_db': doc})


    #name_receive = request.form['AECAWHITE']
    #target_brand = db.brand_db.find(['brand : AECA WHITE'])

    #return jsonify({'result': 'success', 'brand_db': target_brand})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
