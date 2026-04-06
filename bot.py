import telebot
from telebot import types
import sqlite3
import random
import time

# 1. BOT SOZLAMALARI
TOKEN = "7980218532:AAHCx_g2hdVFyaQgLsaqMRoU_0mhW7vi964"
bot = telebot.TeleBot(TOKEN)

# 2. SO'ZLAR BAZASI (Topik 1 va Topik 2 uchun 30 tadan namuna)
data = {
    "topik1": {
        "1": {
            "사과": "olma", "나무": "daraxt", "학교": "maktab", "책": "kitob", "선생님": "o'qituvchi",
            "학생": "o'quvchi", "의자": "stul", "책상": "parta", "문": "eshik", "안경": "ko'zoynak",
            "시계": "soat", "휴대폰": "telefon", "방": "xona", "거실": "mehmonxona", "주방": "oshxona",
            "옷장": "shkaf", "거울": "ko'zgu", "라디오": "radio", "가방": "sumka", "공책": "daftar",
            "연필": "qalam", "볼펜": "ruchka", "지우개": "o'chirg'ich", "지도": "xarita", "침대": "karovot",
            "창문": "deraza", "컵": "stakan", "식당": "oshxona/restoran", "병원": "shifoxona", "은행": "bank"
        }
"2": {
    "물": "suv", "불": "olov", "공기": "havo", "하늘": "osmon", "땅": "yer",
    "산": "tog'", "강": "daryo", "바다": "dengiz", "비": "yomg'ir", "눈": "qor",
    "바람": "shamol", "날씨": "ob-havo", "여름": "yoz", "겨울": "qish", "봄": "bahor",
    "가을": "kuz", "오늘": "bugun", "내일": "ertaga", "어제": "kecha", "시간": "vaqt",
    "아침": "ertalab", "점심": "tushlik", "저녁": "kechki ovqat", "밤": "tun", "낮": "kunduz",
    "지금": "hozir", "항상": "har doim", "자주": "tez-tez", "가끔": "ba'zan", "절대": "hech qachon"
},

"3": {
    "사람": "odam", "남자": "erkak", "여자": "ayol", "아이": "bola", "친구": "do'st",
    "가족": "oila", "아버지": "ota", "어머니": "ona", "형": "aka", "누나": "opa",
    "동생": "uka/singil", "할아버지": "bobo", "할머니": "buvi", "이름": "ism", "나이": "yosh",
    "직업": "kasb", "회사": "kompaniya", "직원": "xodim", "사장": "direktor", "손님": "mehmon",
    "경찰": "politsiya", "의사": "shifokor", "간호사": "hamshira", "선수": "sportchi", "가수": "qo'shiqchi",
    "배우": "aktyor", "학생증": "talaba guvohnomasi", "주소": "manzil", "번호": "raqam", "국적": "millat"
},

"4": {
    "먹다": "yemoq", "마시다": "ichmoq", "가다": "bormoq", "오다": "kelmoq", "보다": "ko'rmoq",
    "듣다": "eshitmoq", "읽다": "o'qimoq", "쓰다": "yozmoq", "말하다": "gapirmoq", "배우다": "o'rganmoq",
    "가르치다": "o'rgatmoq", "일하다": "ishlamoq", "쉬다": "dam olmoq", "자다": "uxlamoq", "일어나다": "turmoq",
    "앉다": "o'tirmoq", "서다": "turmoq", "걷다": "yurmoq", "뛰다": "yugurmoq", "타다": "minmoq",
    "내리다": "tushmoq", "사다": "sotib olmoq", "팔다": "sotmoq", "만나다": "uchrashmoq", "전화하다": "telefon qilmoq",
    "기다리다": "kutmoq", "열다": "ochmoq", "닫다": "yopmoq", "좋아하다": "yoqtirmoq", "싫어하다": "yoqtirmaslik"
}
"5": {
    "과일": "meva", "채소": "sabzavot", "고기": "go'sht", "생선": "baliq", "빵": "non",
    "우유": "sut", "치즈": "pishloq", "계란": "tuxum", "밥": "guruch/ovqat", "국": "sho'rva",
    "커피": "qahva", "차": "choy", "주스": "sharbat", "설탕": "shakar", "소금": "tuz",
    "후추": "murch", "기름": "yog'", "냉장고": "muzlatgich", "전자레인지": "mikroto'lqinli pech", "가스레인지": "gaz plita",
    "접시": "tarelka", "숟가락": "qoshiq", "젓가락": "cho'p", "포크": "vilka", "칼": "pichoq",
    "냄비": "qozon", "프라이팬": "tava", "식탁": "ovqat stoli", "메뉴": "menyu", "주문": "buyurtma"
},

"6": {
    "버스": "avtobus", "지하철": "metro", "택시": "taksi", "기차": "poyezd", "비행기": "samolyot",
    "자전거": "velosiped", "오토바이": "mototsikl", "길": "yo'l", "도로": "katta yo'l", "신호등": "svetofor",
    "횡단보도": "piyodalar yo'lagi", "정류장": "bekat", "표": "chipta", "여권": "pasport", "비자": "viza",
    "여행": "sayohat", "지도책": "atlas", "출발": "jo'nash", "도착": "yetib kelish", "예약": "bron qilish",
    "호텔": "mehmonxona", "열쇠": "kalit", "짐": "yuk", "가이드": "gid", "관광객": "sayyoh",
    "사진기": "kamera", "사진": "rasm", "기념품": "suvenir", "환전": "valyuta almashtirish", "공항": "aeroport"
},

"7": {
    "운동": "sport", "축구": "futbol", "농구": "basketbol", "배구": "voleybol", "테니스": "tennis",
    "수영": "suzish", "달리기": "yugurish", "체육관": "sport zal", "선수단": "jamoa", "경기": "musobaqa",
    "승리": "g'alaba", "패배": "mag'lubiyat", "점수": "hisob", "연습": "mashq", "코치": "murabbiy",
    "심판": "hakam", "공": "to'p", "골": "gol", "유니폼": "forma", "운동화": "krossovka",
    "체력": "jismoniy kuch", "속도": "tezlik", "힘": "kuch", "균형": "muvozanat", "기술": "texnika",
    "대회": "turnir", "참가": "qatnashish", "응원": "qo'llab-quvvatlash", "관중": "tomoshabin", "기록": "rekord"
}
"8": {
    "색깔": "rang", "빨간색": "qizil", "파란색": "ko'k", "노란색": "sariq", "초록색": "yashil",
    "검은색": "qora", "흰색": "oq", "회색": "kulrang", "갈색": "jigarrang", "분홍색": "pushti",
    "보라색": "binafsha", "주황색": "to'q sariq", "밝다": "yorug'", "어둡다": "qorong'i", "크다": "katta",
    "작다": "kichik", "길다": "uzun", "짧다": "qisqa", "높다": "baland", "낮다": "past",
    "넓다": "keng", "좁다": "tor", "두껍다": "qalin", "얇다": "yupqa", "무겁다": "og'ir",
    "가볍다": "yengil", "빠르다": "tez", "느리다": "sekin", "깨끗하다": "toza", "더럽다": "iflos"
},

"9": {
    "감정": "his-tuyg'u", "기쁘다": "xursand bo'lmoq", "슬프다": "xafa bo'lmoq", "화나다": "jahli chiqmoq", "놀라다": "hayron bo'lmoq",
    "무섭다": "qo'rqinchli", "재미있다": "qiziqarli", "재미없다": "zerikarli", "행복하다": "baxtli", "외롭다": "yolg'iz",
    "피곤하다": "charchagan", "졸리다": "uyqusi kelmoq", "배고프다": "och bo'lmoq", "배부르다": "to'q bo'lmoq", "아프다": "og'rimoq",
    "건강하다": "sog'lom", "사랑": "sevgi", "미워하다": "yomon ko'rmoq", "웃다": "kulmoq", "울다": "yig'lamoq",
    "걱정": "tashvish", "스트레스": "stress", "긴장": "hayajon", "편안하다": "xotirjam", "만족": "qoniqish",
    "불만": "norozilik", "희망": "umid", "절망": "umidsizlik", "자신감": "ishonch", "부끄럽다": "uyalmoq"
},

"10": {
    "컴퓨터": "kompyuter", "노트북": "noutbuk", "키보드": "klaviatura", "마우스": "sichqoncha", "모니터": "monitor",
    "인터넷": "internet", "와이파이": "wifi", "웹사이트": "veb-sayt", "비밀번호": "parol", "아이디": "login",
    "다운로드": "yuklab olish", "업로드": "yuklash", "파일": "fayl", "폴더": "papka", "프로그램": "dastur",
    "앱": "ilova", "설치": "o'rnatish", "삭제": "o'chirish", "복사": "nusxa olish", "붙여넣기": "joylash",
    "저장": "saqlash", "열기": "ochish", "닫기버튼": "yopish tugmasi", "검색": "qidirish", "링크": "havola",
    "화면": "ekran", "터치": "sensor bosish", "배터리": "batareya", "충전": "quvvatlash", "전원": "quvvat"
}
"11": {
    "요일": "hafta kuni", "월요일": "dushanba", "화요일": "seshanba", "수요일": "chorshanba", "목요일": "payshanba",
    "금요일": "juma", "토요일": "shanba", "일요일": "yakshanba", "주": "hafta", "달": "oy",
    "년": "yil", "달력": "kalendar", "기간": "muddat", "순서": "tartib", "처음": "birinchi",
    "마지막": "oxirgi", "이전": "oldin", "이후": "keyin", "동안": "davomida", "매일": "har kuni",
    "매주": "har hafta", "매년": "har yil", "일찍": "erta", "늦게": "kech", "곧": "tez orada",
    "방금": "hozirgina", "이미": "allaqachon", "아직": "hali", "계속": "davom etib", "중간": "o‘rtada"
},
    },
    "topik2": {
        "1": {
            "환경": "atrof-muhit", "영향": "ta'sir", "경제": "iqtisodiyot", "발전": "rivojlanish", "과학": "fan",
            "기술": "texnologiya", "사회": "jamiyat", "정부": "hukumat", "문제": "muammo", "해결": "yechim",
            "현상": "hodisa", "원인": "sabab", "결과": "natija", "중요성": "muhimlik", "기능": "vazifa/funksiya",
            "구조": "tuzilish", "과정": "jarayon", "목표": "maqsad", "변화": "o'zgarish", "추세": "tendensiya",
            "연구": "tadqiqot", "분석": "tahlil", "통계": "statistika", "증가": "o'sish", "감소": "kamayish",
            "가능성": "ehtimollik", "경험": "tajriba", "차이": "farq", "관계": "munosabat", "제도": "tizim/tartib"
        }
"2": {
    "정책": "siyosat", "법률": "qonun", "권리": "huquq", "의무": "majburiyat", "민주주의": "demokratiya",
    "선거": "saylov", "투표": "ovoz berish", "정부기관": "davlat organi", "국회": "parlament", "행정": "ma'muriyat",
    "재정": "moliya", "세금": "soliq", "투자": "investitsiya", "시장": "bozor", "무역": "savdo",
    "산업": "sanoat", "노동": "mehnat", "기업": "korxona", "생산": "ishlab chiqarish", "소비": "iste'mol",
    "경쟁": "raqobat", "효율": "samaradorlik", "자원": "resurs", "환경보호": "atrof-muhitni himoya qilish", "지속가능성": "barqarorlik",
    "혁신": "innovatsiya", "전략": "strategiya", "협력": "hamkorlik", "갈등": "mojarо", "위험": "xavf"
},

"3": {
    "교육": "ta'lim", "학습": "o‘rganish", "지식": "bilim", "능력": "qobiliyat", "경험치": "tajriba darajasi",
    "연구개발": "R&D", "논문": "ilmiy maqola", "참여": "ishtirok", "토론": "munozara", "발표": "taqdimot",
    "문헌": "manba", "자료": "ma'lumot", "이론": "nazariya", "실험": "tajriba", "관찰": "kuzatish",
    "분석력": "tahlil qobiliyati", "창의력": "ijodkorlik", "문제해결": "muammoni hal qilish", "능동적": "faol", "비판적": "tanqidiy",
    "집중력": "diqqat", "협동": "hamkorlik qilish", "지도력": "yetakchilik", "자기주도": "o‘zini boshqarish", "평가": "baholash",
    "시험": "imtihon", "성과": "natija", "성장": "o‘sish", "도전": "chaqiriq", "목표달성": "maqsadga erishish"
},

"4": {
    "문화": "madaniyat", "전통": "an'ana", "역사": "tarix", "사회구조": "jamiyat tuzilishi", "가치관": "qiymat tizimi",
    "예술": "san'at", "문학": "adabiyot", "음악": "musiqa", "미술": "tasviriy san'at", "건축": "arxitektura",
    "종교": "din", "철학": "falsafa", "관습": "odat", "축제": "festival", "공연": "konsert/namoyish",
    "영향력": "ta'sir kuchi", "교류": "almashuv", "통합": "integratsiya", "다양성": "turfa", "창조성": "ijodiylik",
    "사회적책임": "ijtimoiy mas'uliyat", "정체성": "shaxsiyat", "시대": "davr", "변천": "o‘zgarish jarayoni", "기념": "xotira",
    "보존": "saqlash", "전파": "tarqatish", "연대": "birlik", "참여": "ishtirok", "학습": "o‘rganish"
},

"5": {
    "과학기술": "fan va texnologiya", "연구원": "tadqiqotchi", "실험실": "laboratoriya", "발명": "ixtiro", "특허": "patent",
    "데이터": "ma'lumotlar", "정보": "informatsiya", "분석도구": "tahlil vositasi", "모형": "model", "설계": "loyiha",
    "자동화": "avtomatlashtirish", "로봇": "robot", "인공지능": "sun'iy intellekt", "컴퓨터시스템": "kompyuter tizimi", "알고리즘": "algoritm",
    "응용": "amaliyot", "실용화": "amaliy qo‘llanish", "혁신기술": "innovatsion texnologiya", "첨단": "zamonaviy", "효율화": "samaradorlashtirish",
    "문제해결능력": "muammoni hal qilish qobiliyati", "팀워크": "jamoaviy ish", "프로젝트": "loyiha", "성과관리": "natijalarni boshqarish", "자원관리": "resurslarni boshqarish",
    "연구개발비": "R&D xarajatlari", "기술발전": "texnologik rivojlanish", "시장분석": "bozor tahlili", "경쟁력": "raqobatbardoshlik", "창업": "startap"
},

"6": {
    "정치": "siyosat", "국제관계": "xalqaro munosabatlar", "외교": "diplomatiya", "안보": "xavfsizlik", "협상": "muzokara",
    "조약": "shartnoma", "연합": "ittifoq", "동맹": "alyans", "분쟁": "mojarо", "전쟁": "urush",
    "평화": "tinchlik", "중재": "vositachilik", "군사력": "harbiy kuch", "경제제재": "iqtisodiy sanksiya", "인권": "inson huquqlari",
    "난민": "qochqin", "이주": "ko‘chish", "난제": "murakkab masala", "국경": "chegara", "자원분쟁": "resurs mojarosi",
    "정책결정": "siyosiy qaror qabul qilish", "의사결정": "qaror qabul qilish", "권력": "hokimiyat", "리더십": "yetakchilik", "책임": "mas'uliyat",
    "참여민주주의": "ishtirokchilik demokratiyasi", "사회운동": "ijtimoiy harakat", "시민권": "fuqarolik huquqi", "법치": "huquqiy davlat", "투명성": "oshkoralik"
},

"7": {
    "경제학": "iqtisodiyotshunoslik", "금융": "moliyaviy tizim", "주식시장": "aksiyalar bozori", "투자전략": "investitsiya strategiyasi", "위험관리": "xavfni boshqarish",
    "회계": "buxgalteriya", "예산": "byudjet", "재무분석": "moliyaviy tahlil", "자본": "kapital", "수익": "daromad",
    "손실": "zarar", "인플레이션": "inflyatsiya", "디플레이션": "deflyatsiya", "시장경제": "bozor iqtisodiyoti", "경기변동": "iqtisodiy sikl",
    "무역정책": "savdo siyosati", "관세": "boj", "환율변동": "valyuta kursi o‘zgarishi", "금리": "foiz stavkasi", "부동산": "ko‘chmas mulk",
    "자산": "aktivlar", "부채": "qarz", "경제성장": "iqtisodiy o‘sish", "고용": "bandlik", "실업": "ishsizlik",
    "물가": "narxlar darajasi", "생산성": "mehnat unumdorligi", "경쟁력강화": "raqobatbardoshlikni kuchaytirish", "혁신경제": "innovatsion iqtisodiyot", "사회복지": "ijtimoiy himoya"
},

"8": {
    "과학": "fan", "생명과학": "biologiya", "물리학": "fizika", "화학": "kimyo", "지구과학": "geografiya",
    "천문학": "astronomiya", "생태학": "ekologiya", "유전학": "genetika", "진화": "evolyutsiya", "세포": "hujayra",
    "분자": "molekula", "원자": "atom", "에너지": "energiya", "힘": "kuch", "운동": "harakat",
    "속도": "tezlik", "가속": "tezlanish", "중력": "og‘irlik kuchi", "압력": "bosim", "온도": "harorat",
    "화학반응": "kimyoviy reaksiya", "실험방법": "tajriba usuli", "관찰결과": "kuzatuv natijasi", "측정": "o‘lchash", "이론검증": "nazariyani tekshirish",
    "모델링": "modellash", "시뮬레이션": "simulyatsiya", "데이터분석": "ma'lumotlarni tahlil qilish", "결과해석": "natijani tahlil qilish", "논리적사고": "mantiqiy fikrlash"
},

"9": {
    "사회문제": "ijtimoiy muammo", "빈곤": "qashshoqlik", "실업문제": "ishsizlik muammosi", "범죄": "jinoyat", "교육격차": "ta'limdagi farq",
    "환경오염": "atrof-muhit ifloslanishi", "기후변화": "iqlim o‘zgarishi", "자원고갈": "resurs tugashi", "질병": "kasallik", "노인문제": "qariyalar masalasi",
    "청소년문제": "yoshlar muammosi", "이주문제": "ko‘chish muammosi", "인권침해": "inson huquqlari buzilishi", "사회복지정책": "ijtimoiy himoya siyosati", "주거문제": "uy-joy masalasi",
    "교통문제": "transport muammosi", "도시문제": "shahar muammosi", "정보격차": "informatsiya farqi", "빈집문제": "bo‘sh uy masalasi", "재난대응": "falokatga tayyorgarlik",
    "범죄예방": "jinoyatni oldini olish", "사회통합": "ijtimoiy integratsiya", "복지제도": "ijtimoiy tizim", "지역격차": "hududiy farq", "경제불균형": "iqtisodiy nomutanosiblik",
    "민주화": "demokratlashuv", "투명성강화": "oshkoralikni kuchaytirish", "참여확대": "ishtirokni kengaytirish", "정책평가": "siyosat baholash", "공공서비스": "jamoat xizmatlari"
},

"10": {
    "철학": "falsafa", "논리": "mantiq", "윤리": "axloq", "가치": "qiymat", "사상": "fikr",
    "인간관계": "insoniy munosabatlar", "자아": "o‘zlik", "존재": "mavjudlik", "인식": "idrok", "지혜": "donolik",
    "사례분석": "holat tahlili", "비판적사고": "tanqidiy fikrlash", "창의적사고": "ijodiy fikrlash", "논쟁": "bahs", "주장": "da'vo",
    "설득": "ishontirish", "토론기법": "munozara texnikasi", "문제인식": "muammoni anglash", "합리적결정": "mantiqiy qaror", "사회비판": "jamiyatni tanqid",
    "정의": "adolat", "자유": "erkinlik", "책임": "mas'uliyat", "권리보장": "huquqni himoya qilish", "공정성": "adolatlilik",
    "참여적사고": "ishtirokchi fikrlash", "인류발전": "insoniyat rivoji", "지식확장": "bilimni kengaytirish", "문화이해": "madaniyatni tushunish", "사회문제해결": "ijtimoiy muammoni hal qilish"
}
    }
}

# 3. MA'LUMOTLAR BAZASI (SQLite)
def init_db():
    conn = sqlite3.connect('korean_bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, t1_day INTEGER DEFAULT 1, t2_day INTEGER DEFAULT 1)''')
    conn.commit()
    conn.close()

def get_user_days(user_id):
    conn = sqlite3.connect('korean_bot.db')
    c = conn.cursor()
    c.execute("SELECT t1_day, t2_day FROM users WHERE id=?", (user_id,))
    res = c.fetchone()
    conn.close()
    return res if res else (1, 1)

def set_user_day(user_id, topic, day):
    conn = sqlite3.connect('korean_bot.db')
    c = conn.cursor()
    t1, t2 = get_user_days(user_id)
    if topic == "topik1":
        c.execute("INSERT OR REPLACE INTO users (id, t1_day, t2_day) VALUES (?, ?, ?)", (user_id, day, t2))
    else:
        c.execute("INSERT OR REPLACE INTO users (id, t1_day, t2_day) VALUES (?, ?, ?)", (user_id, t1, day))
    conn.commit()
    conn.close()

user_test = {}

# 4. BOT BUYRUKLARI
@bot.message_handler(commands=['start'])
def start(message):
    init_db()
    t1_day, t2_day = get_user_days(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(f"📚 TOPIK 1 ({t1_day}-kun)"))
    markup.add(types.KeyboardButton(f"🎓 TOPIK 2 ({t2_day}-kun)"))
    bot.send_message(message.chat.id, "Salom! Koreys tili darajangizni tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda m: "TOPIK" in m.text)
def show_lesson(message):
    topic = "topik1" if "TOPIK 1" in message.text else "topik2"
    t1_day, t2_day = get_user_days(message.chat.id)
    day_num = t1_day if topic == "topik1" else t2_day
    day_str = str(day_num)

    if day_str not in data[topic]:
        bot.send_message(message.chat.id, "Hozircha keyingi kunlar yuklanmagan.")
        return

    words_text = f"📅 {topic.upper()} | {day_num}-kun so'zlari:\n\n"
    for kor, uzb in data[topic][day_str].items():
        words_text += f"🔹 {kor} - {uzb}\n"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📝 Testni boshlash", callback_data=f"start_test_{topic}_{day_num}"))
    bot.send_message(message.chat.id, words_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("start_test_"))
def start_test(call):
    parts = call.data.split("_")
    topic = parts[2]
    day_num = int(parts[3])
    day_words = list(data[topic][str(day_num)].items())
    random.shuffle(day_words)

    user_test[call.message.chat.id] = {
        "topic": topic, "day": day_num, "score": 0, "current_q_idx": 0, "words": day_words
    }
    bot.delete_message(call.message.chat.id, call.message.message_id)
    send_question(call.message.chat.id)

def send_question(chat_id):
    test_data = user_test[chat_id]
    idx = test_data["current_q_idx"]
    
    if idx < len(test_data["words"]):
        kor_word, correct_ans = test_data["words"][idx]
        
        # Xato variantlar
        topic = test_data["topic"]
        all_uzb = [v for d in data[topic].values() for v in d.values()]
        wrong_options = random.sample([w for w in all_uzb if w != correct_ans], 3)
        
        options = [correct_ans] + wrong_options
        random.shuffle(options)

        markup = types.InlineKeyboardMarkup()
        for opt in options:
            cb_data = "ans_correct" if opt == correct_ans else "ans_wrong"
            markup.add(types.InlineKeyboardButton(opt, callback_data=cb_data))

        bot.send_message(chat_id, f"❓ {idx+1}/{len(test_data['words'])}\n\n**{kor_word}** so'zining tarjimasi nima?", 
                         reply_markup=markup, parse_mode="Markdown")
    else:
        finish_test(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("ans_"))
def handle_answer(call):
    chat_id = call.message.chat.id
    if call.data == "ans_correct":
        user_test[chat_id]["score"] += 1
    
    user_test[chat_id]["current_q_idx"] += 1
    bot.delete_message(chat_id, call.message.message_id)
    send_question(chat_id)

def finish_test(chat_id):
    test_data = user_test[chat_id]
    score = test_data["score"]
    total = len(test_data["words"])
    percent = (score / total) * 100
    topic = test_data["topic"]
    day_num = test_data["day"]

    if percent >= 70:
        new_day = day_num + 1
        set_user_day(chat_id, topic, new_day)
        msg = f"✅ Natija: {percent:.0f}%\nTabriklaymiz! {new_day}-kun ochildi."
    else:
        msg = f"❌ Natija: {percent:.0f}%\nO'tish uchun 70% kerak. Yana urinib ko'ring."

    t1, t2 = get_user_days(chat_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(f"📚 TOPIK 1 ({t1}-kun)"))
    markup.add(types.KeyboardButton(f"🎓 TOPIK 2 ({t2}-kun)"))
    bot.send_message(chat_id, msg, reply_markup=markup)

if __name__ == '__main__':
    print("Bot ishlamoqda...")
    init_db()
    bot.infinity_polling()
