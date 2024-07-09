#몽고 db 페이지

from pymongo import MongoClient

# settings.py에 설정된 MongoDB URI
MONGO_URI = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/userdata?retryWrites=true&w=majority&appName=KIOSK"

# MongoDB 클라이언트 생성
client = MongoClient(MONGO_URI)

# 데이터베이스 선택
db = client['userdata']

# 예시 컬렉션 접근
collection = db['study']

# 데이터 삽입 예시
example_data = {"id": "seungheon", "pw": 1234, "seat": 12}
collection.insert_one(example_data)

print("MongoDB에 연결되었습니다.")