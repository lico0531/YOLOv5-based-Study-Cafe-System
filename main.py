from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from pymongo import MongoClient

#db 연동---------------------------------------------
mongo_connect = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/?retryWrites=true&w=majority&appName=KIOSK"
client = MongoClient(mongo_connect)
db = client.temp

client = MongoClient(mongo_connect)
db = client.temp

# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# # 한 개 찾기(조건 추가)
# user = db.users.find_one({'name':'bobby'})

# # 여러개 찾기( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))

# # 바꾸기
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# # 지우기
# db.users.delete_one({'name':'bobby'})
#db 연동---------------------------------------------

app = Flask(__name__)
app.secret_key = 'secret'

# 회원가입
@app.route('/signup', methods=['POST'])
def signup():
    data = request.form
    existing_user = db.users.find_one({'name': data['new_username']})
    if existing_user:
        return redirect(url_for('home', msg="이미 있는 ID입니다."))
    else:
        new_user = {'name': data['new_username'], 'password': data['new_password'], 'seat': None}
        db.users.insert_one(new_user)
        return redirect(url_for('home', msg="회원가입이 성공적으로 되었습니다."))
    
# 로그인
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    user = db.users.find_one({'name': data['username'], 'password': data['password']})
    if user:
        session['username'] = user['name']  # 사용자 정보 세션에 저장
        return redirect(url_for('seat', msg="로그인 성공!"))
    else:
        return redirect(url_for('home', msg="로그인 실패!"))
    
# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)  # 세션에서 사용자 정보 제거
    return redirect(url_for('home'))

# 퇴실하기
@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    username = session.get('username')
    if username:
        db.users.update_one({'name': username}, {'$set': {'seat': None}})
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "사용자 정보를 찾을 수 없습니다."})

@app.route('/')
def home():
    msg = request.args.get('msg')
    return render_template('index.html', msg=msg)

@app.route('/seat')
def seat():
    return render_template('seat.html')

# 좌석 선택
@app.route('/select_seat', methods=['POST'])
def select_seat():
    data = request.json
    selected_seat = data['seat']
    username = session.get('username')  # 세션에서 사용자 정보 가져오기
    if username:
        db.users.update_one({'name': username}, {'$set': {'seat': selected_seat}})
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "사용자 정보를 찾을 수 없습니다."})
    
# 좌석 정보 가져오기
@app.route('/fetch_seat_info', methods=['GET'])
def fetch_seat_info():
    all_users = list(db.users.find({}, {'_id': False, 'name': True, 'seat': True}))
    seat_data = [{"seat": user['seat']} for user in all_users if 'seat' in user]
    return jsonify({"success": True, "seats": seat_data})



@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    return jsonify({"msg":"완료!"})
    
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
   return jsonify({'msg': "완료!"})
   
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)