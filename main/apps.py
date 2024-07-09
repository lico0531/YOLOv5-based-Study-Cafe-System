from django.apps import AppConfig
from pymongo import MongoClient

class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

# class KioskConfig(AppConfig):
#     name = 'kiosk'

#     def ready(self):
#         # MongoDB 초기화 코드
#         MONGO_URI = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/userdata?retryWrites=true&w=majority&appName=KIOSK"
#         client = MongoClient(MONGO_URI)
#         db = client['userdata']
#         collection = db['study']
#         example_data = {"id": "id", "pw": 0, "seat": 0}
#         collection.insert_one(example_data)
#         print("MongoDB에 연결되었습니다.")
