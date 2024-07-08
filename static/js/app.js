const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const session = require('express-session');
const MongoStore = require('connect-mongo');
const cors = require('cors');
const authRoutes = require('../../../../server/routes/auth');
const seatRoutes = require('../../../../server/routes/seat');
const { MongoClient, ServerApiVersion } = require('mongodb');

const app = express();
const PORT = process.env.PORT || 3000;

const uri = "mongodb+srv://shlico0531:kiosk@kiosk.edi8kfi.mongodb.net/userdata?retryWrites=true&w=majority&appName=KIOSK"; // 이 부분을 세션 설정 전에 위치시킵니다.

app.use(bodyParser.json());
app.use(express.static('public'));

// CORS 설정
app.use(cors({
    origin: true, // 모든 출처 허용
    credentials: true
}));

// 세션 설정 (MongoDB를 세션 저장소로 사용)
app.use(session({
    secret: 'webKids123!',
    resave: false,
    saveUninitialized: false,
    store: MongoStore.create({ mongoUrl: uri }),
    cookie: {
        secure: false, // 로컬 환경에서는 false로 설정
        sameSite: 'lax' // or 'strict' depending on your setup
    }
}));

// MongoDB 연결 설정
const client = new MongoClient(uri, {
    serverApi: {
        version: ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});

async function run() {
    try {
        await client.connect();
        await client.db("admin").command({ ping: 1 });
        console.log("Pinged your deployment. You successfully connected to MongoDB!");
    } catch (error) {
        console.error('MongoDB connection error:', error);
    }
}
run().catch(console.dir);

// Mongoose 연결 설정
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Mongoose connected'))
    .catch(err => console.log(err));

// 라우터 설정
app.use('/auth', authRoutes);
app.use('/seat', seatRoutes);

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
