from pymongo import MongoClient

mongo_connect = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/?retryWrites=true&w=majority&appName=KIOSK"
client = MongoClient(mongo_connect)
db = client.temp

client = MongoClient(mongo_connect)
db = client.temp

doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기(조건 추가)
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기
db.users.delete_one({'name':'bobby'})