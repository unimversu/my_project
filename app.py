from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

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
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    #result = list(db.brand_db.find({}, {'_id': False})),
    # 2. articles라는 키 값으로 articles 정보 보내주기

    name_receive = request.form['name_give']
    target_brand = db.brand_db.find.one(['brand : name_receive'])

    return jsonify({'result': 'success', 'brand_db': target_brand})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
