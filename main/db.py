from pymongo import MongoClient

MONGO_URI = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/userdata?retryWrites=true&w=majority&appName=KIOSK"
client = MongoClient(MONGO_URI)
db = client['userdata']
collection = db['study']