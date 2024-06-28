import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import json
import instaloader
import time
from enum import Flag
import random
import requests
import threading
import re
from fake_useragent import UserAgent
import os
from pytube import YouTube
import hashlib
import base64

import xml.etree.ElementTree as ET
capthan='''مرحبا بك في بوت تيم الزعيم ☠️🔥

البوت لثغرات الانترنت المجاني 👑

         اختر القسم المطلوب : 👇'''
p = "Kiro"
ida=6552799655
authenticated_users = {}
photourl = "https://t.me/MM_5_1/2"
admin_chat_id = ida
user_data = {}
TOKEN = "6736219238:AAHV8PBd-8UNmyW6sKV_VwTE8i6NsyJsYKY"
token = TOKEN
admin = ida


ADMIN_ID = ida
CHANNELS = [ "@ElZAEM_Team","@KingsNet70","@passward_Amr"] 



linkpas="https://ouo.io/8Jllj"
we10="https://t.me/Legendseam_204/1800"
face="https://tme/Legends_Tam_224/1828"
yout="https://t.me/Legends_Team24/1829"
bot = telebot.TeleBot(TOKEN)
ascii_art = '''█▀▀▄ █▀▀ ▀█░█▀ █▀▀ 
█░░█ █▀▀ ░█▄█░ ▀▀█ 
▀▀▀░ ▀▀▀ ░░▀░░ ▀▀▀ 
'''
sent_to_admin = {}
password_required = False 
def append_user_id(user_id):
    with open('ids', 'a+') as file:
        file.seek(0)
        ids = file.read().splitlines()
        if str(user_id) not in ids:
            file.write(str(user_id) + '\n')

def check_subscription(user_id):
    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                return False
        except:
            return False
    return True

def is_admin(chat_id):
    return chat_id == admin_chat_id

@bot.message_handler(commands=['admin'])
def send_admin_commands(message):
    chat_id = message.chat.id
    if is_admin(chat_id):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton('تغيير كلمة المرور', callback_data='chg_password'),
            types.InlineKeyboardButton('تغيير الرابط ', callback_data='chg_link'),
            types.InlineKeyboardButton('تغيير الكابشن  ', callback_data='chg_c'),
            types.InlineKeyboardButton('تغيير الصوره  ', callback_data='chg_p'),

            types.InlineKeyboardButton('تحديث yout', callback_data='update_yout'),
            types.InlineKeyboardButton('تحديث facebook', callback_data='update_facebook'),
            types.InlineKeyboardButton('تحديث we', callback_data='upwe10'),
            types.InlineKeyboardButton('اذاعة ', callback_data='request_message_to_send'),
            types.InlineKeyboardButton(' عدد المستخدمين  ', callback_data='count_lines_in_ids'),
            types.InlineKeyboardButton(' وضع باسورد او لا   ', callback_data='toggle_password'),
            types.InlineKeyboardButton('إرسال ملف ids', callback_data='send_ids_file')
        )
        bot.send_message(chat_id, "أوامر الادمن", reply_markup=keyboard)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")


@bot.callback_query_handler(func=lambda call: call.data == 'send_ids_file')
def send_ids_file_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        try:
            with open('ids', 'rb') as file:
                bot.send_document(chat_id, file)
        except FileNotFoundError:
            bot.send_message(chat_id, "الملف 'ids' غير موجود.")
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

@bot.callback_query_handler(func=lambda call: call.data == 'toggle_password')
def toggle_password_callback(call):
    global password_required
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        password_required = not password_required
        status = "تم وضع طلب الباسورد" if password_required else "تم الغاء طلب الباسورد "
        bot.send_message(chat_id, f"  تم تغيير وضع كلمة المرور   : {status}")
        authenticated_users.clear()
        user_data.clear()
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

@bot.callback_query_handler(func=lambda call: call.data == 'update_yout')
def update_yout_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "يرجى إرسال الرابط الجديد لمتغير yout:")
        bot.register_next_step_handler(call.message, process_yout_update)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def process_yout_update(message):
    chat_id = message.chat.id
    new_yout_value = message.text.strip()
    global yout
    yout = new_yout_value
    bot.send_message(chat_id, f"تم تحديث قيمة متغير link إلى:\n{yout}")


@bot.callback_query_handler(func=lambda call: call.data == 'chg_p')
def update_yout_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "ارسل رابط الصورة الجديدة")
        bot.register_next_step_handler(call.message, ph)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def ph(message):
    chat_id = message.chat.id
    new_photo_value = message.text.strip()
    global photourl
    photourl = new_photo_value
    bot.send_message(chat_id, f"تم تحديث الي \n{photourl}")   

@bot.callback_query_handler(func=lambda call: call.data == 'chg_link')
def update_yout_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "يرجى إرسال الرابط الجديد لمتغير link:")
        bot.register_next_step_handler(call.message, link)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")
 
@bot.callback_query_handler(func=lambda call: call.data == 'chg_c')
def upc(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "اكتب الكابشن ")
        bot.register_next_step_handler(call.message, cvd)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def cvd(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    chat_id = message.chat.id
    qw = message.text.strip()
    global capthan
    capthan = qw
    bot.send_message(chat_id, f"تم تحديث الكابشن   إلى:\n{capthan}")

def link(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    chat_id = message.chat.id
    new_link_value = message.text.strip()
    global linkpas
    linkpas = new_link_value
    bot.send_message(chat_id, f"تم تحديث قيمة متغير yout إلى:\n{linkpas}")

@bot.callback_query_handler(func=lambda call: call.data == 'update_facebook')
def update_facebook_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "يرجى إرسال الرابط الجديد لمتغير facebook:")
        bot.register_next_step_handler(call.message, process_facebook_update)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def process_facebook_update(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    chat_id = message.chat.id
    new_facebook_value = message.text.strip()
    global face
    face = new_facebook_value
    bot.send_message(chat_id, f"تم تحديث قيمة متغير facebook إلى:\n{face}")
@bot.callback_query_handler(func=lambda call: call.data == 'upwe10')
def upwe10(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "يرجى إرسال الرابط الجديد لمتغير we:")
        bot.register_next_step_handler(call.message, porwe10)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def porwe10(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    chat_id = message.chat.id
    new_we_value = message.text.strip()
    global face
    we10 = new_we_value
    bot.send_message(chat_id, f"تم تحديث قيمة متغير facebook إلى:\n{we10}")

@bot.callback_query_handler(func=lambda call: call.data == 'chg_password')
def change_password_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "الرجاء إدخال كلمة المرور الحالية:")
        bot.register_next_step_handler(call.message, process_old_password)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def process_old_password(message):
    chat_id = message.chat.id
    if message.text == p:
        bot.send_message(chat_id, "الرجاء إدخال كلمة المرور الجديدة:")
        bot.register_next_step_handler(message, process_new_password)
    else:
        bot.send_message(chat_id, "كلمة المرور غير صحيحة.")

def process_new_password(message):
    global p
    p = message.text
    bot.send_message(message.chat.id, f"تم تغيير كلمة المرور بنجاح إلى: {p}")
    authenticated_users.clear()
    user_data.clear()


@bot.callback_query_handler(func=lambda call: call.data == 'request_message_to_send')
def request_message_to_send_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        bot.send_message(chat_id, "يرجى إرسال الرسالة التي ترغب في إرسالها للجميع.")
        bot.register_next_step_handler(call.message, send_message_to_all)
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")

def send_message_to_all(message):
    chat_id = message.chat.id
    if is_admin(chat_id):
        try:
            with open('ids', 'r') as file:
                ids = file.read().splitlines()
                for user_id in ids:
                    try:
                        bot.send_message(user_id, message.text)
                        time.sleep(5)
                    except Exception as e:
                        print(f"Error sending message to {user_id}: {e}")
            bot.send_message(chat_id, "تم إرسال الرسالة لجميع المستخدمين في ملف 'ids'.")
        except FileNotFoundError:
            bot.send_message(chat_id, "الملف 'ids' غير موجود.")
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")
@bot.callback_query_handler(func=lambda call: call.data == 'count_lines_in_ids')
def count_lines_in_ids_callback(call):
    chat_id = call.message.chat.id
    if is_admin(chat_id):
        try:
            with open('ids', 'r') as file:
                lines = len(file.readlines())
                bot.send_message(chat_id, f"عدد مستخدمين البوت{lines}")
        except FileNotFoundError:
            bot.send_message(chat_id, "الملف 'ids' غير موجود.")
    else:
        bot.send_message(chat_id, "غير مصرح لك باستخدام هذا الأمر.")



@bot.message_handler(commands=['start'])
def ask_for_authentication(message):
    if message.chat.type == 'private':
        chat_id = message.chat.id
        if chat_id in authenticated_users and authenticated_users[chat_id]:
            start(message)
        else:
            if check_subscription(chat_id):
                if password_required:
                    bot.send_message(chat_id, f"""اكتب باسورد البوت للدخول الي السكربتات
                    لو مش عارفه تقدر تجيبه من الربط دا 👇
                    {linkpas}""")
                    bot.register_next_step_handler(message, check_password)
                else:
                    authenticated_users[chat_id] = True
                    start(message)
            else:
                markup = types.InlineKeyboardMarkup()
                for channel in CHANNELS:
                    btn = types.InlineKeyboardButton(text=f"اشترك في {channel}", url=f"https://t.me/{channel[1:]}")
                    markup.add(btn)
                bot.reply_to(message, "من فضلك اشترك بكل القنوات", reply_markup=markup)

def check_password(message):
    chat_id = message.chat.id
    password = message.text
    if password == p:
        authenticated_users[chat_id] = True
        bot.send_message(chat_id, "تم التحقق من كلمة المرور بنجاح!")
        start(message)
    else:
        bot.send_message(chat_id, "كلمة المرور غير صحيحة. يرجى المحاولة مرة أخرى.")


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        if check_subscription(message.chat.id):
            global sent_to_admin
            user_id = message.chat.id

            if user_id not in sent_to_admin:
                user_info = extract_user_info(message)
                admin_message = f"مستخدم جديد:\n\n{user_info}"
                bot.send_message(ADMIN_ID, admin_message)
                sent_to_admin[user_id] = True
                append_user_id(user_id)

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                types.InlineKeyboardButton('قسم  اورنج', callback_data='open_menu'),
                types.InlineKeyboardButton('قسم اتصالات', callback_data='open_menu2'),
                types.InlineKeyboardButton('قسم فودفون', callback_data='open_menu3'),
                types.InlineKeyboardButton('قسم الرشق', callback_data='rash'),
                types.InlineKeyboardButton('قسم التحميل', callback_data='download')
            )


            bot.send_photo(message.chat.id, photourl,caption=capthan,  reply_markup=keyboard)
        else:
         markup = types.InlineKeyboardMarkup()
         for channel in CHANNELS:
            btn = types.InlineKeyboardButton(text=f"اشترك في    {channel}", url=f"https://t.me/{channel[1:]}")
            markup.add(btn)
         bot.reply_to(message, "من فضلك اشترك بكل القنوات", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.strip() == "/start")
def check_for_start_command(message):
    start(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)  
    except Exception as e:
        print(f"Error deleting message: {e}")

    if call.data == 'open_menu':
        menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
        menu_keyboard.add(
            types.InlineKeyboardButton('524 ميجا اورنج ', callback_data='buttonx'),
            types.InlineKeyboardButton(' تفعيل واتش ات ', callback_data='buttong'),
            types.InlineKeyboardButton(' عجلة الحظ   ', callback_data='spin'),

        )
        bot.send_message(call.message.chat.id, 'اختار القسم اللذي تريده:', reply_markup=menu_keyboard)
    elif call.data == 'open_menu2':
        menu_keyboard = types.InlineKeyboardMarkup()
        menu_keyboard.row(
            types.InlineKeyboardButton(' ساعتين سوشيال  ', callback_data='2hour'),
        )
        bot.send_message(call.message.chat.id, 'اختار القسم اللذي تريده:', reply_markup=menu_keyboard)   

    elif call.data == 'open_menu3':
        menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
        menu_keyboard.add(
            types.InlineKeyboardButton(' بيانات فودفون   ', callback_data='vfinfo'),
            types.InlineKeyboardButton('وحدات عشوائية فودافون', callback_data='DF'),
            types.InlineKeyboardButton('توزيع فلكسات فودفون',callback_data="flex"),
            types.InlineKeyboardButton(' تغيير النسبة ',callback_data="change"),


        )        
        bot.send_message(call.message.chat.id, 'اختار القسم اللذي تريده:', reply_markup=menu_keyboard)   
    

    elif call.data == 'download':
        menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
        
        menu_keyboard.add(
            types.InlineKeyboardButton('تحميل من التيكتوك', callback_data='tik'),
            types.InlineKeyboardButton('تحميل من الانستا', callback_data='ins'),
            types.InlineKeyboardButton('تحميل من اليوتيوب', callback_data='youtu'),
            types.InlineKeyboardButton('تحميل من الفيسبوك', callback_data='favs'),


        )
        
        bot.send_message(call.message.chat.id, 'اختار القسم اللذي تريده:', reply_markup=menu_keyboard)

    elif call.data == 'rash':
        menu_keyboard = types.InlineKeyboardMarkup()
        menu_keyboard.row(
            types.InlineKeyboardButton('1000 مشاهدة تيكتوك', callback_data='rashb'),
        )
        bot.send_message(call.message.chat.id, 'اختار القسم اللذي تريده:', reply_markup=menu_keyboard)        
    elif call.data == "devs":
        menu_keyboard = types.InlineKeyboardMarkup()
        menu_keyboard.row(
            types.InlineKeyboardButton("المطور", url="https://t.me/S_"),
            types.InlineKeyboardButton("المطور", url="https://t.me/A_9"),

        )
        bot.send_message(call.message.chat.id, f"{ascii_art}", reply_markup=menu_keyboard)
    elif call.data == "KONFGAT":
     menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
     menu_keyboard.add(
        types.InlineKeyboardButton("كونفج وي 10 جيجا", url=we10),
        types.InlineKeyboardButton("كونفج تحويل الفيس لكل المواقع", url=face),
        types.InlineKeyboardButton("كونفج تحويل اليوتيوب لكل المواقع", url=yout)
     )
     bot.send_message(call.message.chat.id, "قسم الكونفجات", reply_markup=menu_keyboard)
     
    elif call.data == "2hour":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, houre)

    elif call.data == "DF":
     msg = bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
     bot.register_next_step_handler(msg, gf)

    elif call.data == "spin":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, spin2)
    elif call.data == "change":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, change2)        
    elif call.data == "flex":
     menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
     menu_keyboard.add(
        types.InlineKeyboardButton("  فليكس 200 ",callback_data=1 ),
        types.InlineKeyboardButton("   فليكس 100  ", callback_data=2),
        types.InlineKeyboardButton("فلكس 70", callback_data=3)
     )
     bot.send_message(call.message.chat.id, "قسم الفلكسات", reply_markup=menu_keyboard)




    elif call.data == "tik":
        bot.send_message(call.message.chat.id, "   برجاء إرسال رابط الفديو")
        bot.register_next_step_handler(call.message, dontik)
    elif call.data == "ins":
        bot.send_message(call.message.chat.id, "   برجاء إرسال الرابط ")
        bot.register_next_step_handler(call.message, insta)
    elif call.data == "favs":
        bot.send_message(call.message.chat.id, "   برجاء إرسال الرابط ")
        bot.register_next_step_handler(call.message, facebooks)

    elif call.data == "youtu":
        bot.send_message(call.message.chat.id, "   برجاء إرسال الرابط ")
        bot.register_next_step_handler(call.message, youtube)


    elif call.data == "1":
        Flexat=523
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, nexts,Flexat)

    elif call.data == "2":
        Flexat=517
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, nexts,Flexat)
    elif call.data == "3":
        Flexat=515
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, nexts,Flexat)

    elif call.data == "buttonx":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")
        bot.register_next_step_handler(call.message, get_number)
    elif call.data == "buttong":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")

        bot.register_next_step_handler(call.message, get_number2)
    elif call.data == "vfinfo":
        bot.send_message(call.message.chat.id, "ادخل رقم الهاتف  📲")

        bot.register_next_step_handler(call.message, vfpass)

    elif call.data == "rashb":
        bot.send_message(call.message.chat.id, "من فضلك ارسل الرابط علي هيئة \n https://vm.tiktok.com/ZMMcsC6C7/")
        bot.register_next_step_handler(call.message, rashc)

def vfpass(message):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    
    nu=message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message, info,nu )

def change2(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass

    nu=message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message,change3 ,nu )
    
def change3(message,nu):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    pw=message.text
    bot.send_message(message.chat.id,"ارسل رقم الفرد")
    bot.register_next_step_handler(message,change4,nu,pw)
def change4(message,nu,pw):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    nu2=message.text
    bot.send_message(message.chat.id,"ارسل النسبة الجديده")
    bot.register_next_step_handler(message,sdam2x,nu,pw,nu2)        
def nexts(message,Flexat):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    nu1=message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message, nexts1,nu1,Flexat )
def nexts1 (message,nu1,Flexat):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    pas1=message.text
    bot.send_message(message.chat.id, "برجاء إدخال النسبة من 0 ال 99   :")
    bot.register_next_step_handler(message, nexts2,nu1,Flexat, pas1)
def nexts2(message,nu1,Flexat,pas1):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    value=message.text
    bot.send_message(message.chat.id,"برجاء ارسال رقم الفرد")
    bot.register_next_step_handler(message, nexts3,nu1,Flexat, pas1,value)
def nexts3(message,nu1,Flexat,pas1,value):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    nu2=message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمةالسر  للفرد:")
    bot.register_next_step_handler(message, sdam,nu1,Flexat, pas1,value,nu2)


def sdam(message,nu1,Flexat, pas1,value,nu2):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    pas2=message.text
    try:
        url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
        headers = {
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        "x-agent-operatingsystem": "10.1.0.264C185",
        "clientI": "AnaVodafoneAndroid",
        "x-agent-device": "HWDRA-MR",
        "x-agent-version": "2022.1.2.3",
        "x-agent-build": "500",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "142",
        "Host": "mobile.vodafone.com.eg",
        "User-Agent": "okhttp/4.9.1",
    }
        data = 'username=' + nu1 + '&password=' + pas1 + '&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'

        response = requests.post(url, headers=headers, data=data).json()
        print(response)
        token = response.get("access_token")

    
        if not token:
            raise Exception("Failed to retrieve access token")

        url2 = 'https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
        headers2 = {
        "Host": "mobile.vodafone.com.eg",
        "x-dynatrace": "MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
        "msisdn": nu1,
        "api-version": "v2",
        "x-agent-operatingsystem": "1630483957",
        "clientId": "AnaVodafoneAndroid",
        "Authorization": "Bearer " + token,
        "x-agent-device": "RMX1911",
        "Accept": "application/json",
        "x-agent-version": "2022.2.1.2",
        "x-agent-build": "503",
        "Accept-Language": "ar",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "302",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.1",
    }
        json_data = {
        "category": [{"listHierarchyId": "PackageID", "value": Flexat},
                     {"listHierarchyId": "TemplateID", "value": "47"},
                     {"listHierarchyId": "TierID", "value": Flexat},
                     {"listHierarchyId": "familybehavior", "value": "percentage"}],
        "name": "FlexFamily",
        "parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "quotaDist1",
                                                                      "type": "percentage", "value": value,}]},
                  "member": [{"id": [{"schemeName": "MSISDN", "value": nu1,}], "type": "Owner"},
                             {"id": [{"schemeName": "MSISDN", "value": nu2}], "type": "Member"}]},
        "type": "SendInvitation"
    }
        response2 = requests.patch(url2, headers=headers2, json=json_data)
        response2_text = response2.text

        if '{}' in response2_text:
            bot.send_message(message.chat.id, "تم ارسال طلب الاضافه بنجاح انتظر القبول ✅")
        else:
            error_message = "فشل الاضافه والسبب: "
            if 'Generic System Error' in response2_text:
                error_message += "عفوا حدث خطأ"
            elif 'Customer not eligible-Family Owner' in response2_text:
                error_message += "الرقم صاحب عيله"
            elif 'You have reached the maximum number of family' in response2_text:
                error_message += "صاحب العيله عنده افراد اكتر من العدد المحدد له, او النسبه مش متاحه"
            elif 'Customer not eligible-Family member' in response2_text:
                error_message += "الفرد موجود في عيله تانيه"
            elif 'Not Found' in response2_text:
                error_message += "مش نافع ولا يوجد سبب محدد"
            elif 'Customer not eligible- Enterprise Customer' in response2_text:
                error_message += "الخط بزنس او كان بزنس"
            else:
                error_message += "لم يتم قبول طلب الاضافه "
            bot.send_message(message.chat.id, error_message)

        print(response2_text)

     

        url1 = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"

        hd1 = {'Accept': 'application/json, text/plain, */*',
           'Connection': 'keep-alive',
           'x-dynatrace': 'MT_3_13_3830690492_8-0_a556db1b-4506-43f3-854a-1d2527767923_0_16912_686',
           'x-agent-operatingsystem': 'V12.0.17.0.QJQMIXM',
           'clientId': 'AnaVodafoneAndroid',
           'x-agent-device': 'lime',
           'x-agent-version': '2022.1.2.3',
           'x-agent-build': '500',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': '145',
           'Host': 'mobile.vodafone.com.eg',
           'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/4.9.1'
    }

        data1 = {"username": nu2, "password": pas2, "grant_type": "password",
             "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3", "client_id": "my-vodafone-app"}

        r5 = requests.post(url1, headers=hd1, data=data1).json()
        print(r5)

        if 'access_token' in r5:
            token = r5['access_token']
            auth = "Bearer " + token
            urlacp = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
            dataacp = '{"category": [{"listHierarchyId": "TemplateID", "value": "47"}], "name": "FlexFamily", "parts": {"member": [{"id": [{"schemeName": "MSISDN", "value": "2%s"}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value": "%s"}], "type": "Member"}]}, "type": "AcceptInvitation"}' % (
            nu1, nu2)
            headersacp = {
            "Host": "mobile.vodafone.com.eg",
            "x-dynatrace": "MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
            "msisdn": nu2,
            "api-version": "v2",
            "x-agent-operatingsystem": "1630483957",
            "clientId": "AnaVodafoneAndroid",
            "Authorization": "Bearer " + (token) + "",
            "x-agent-device": "RMX1911",
            "Accept": "application/json",
            "x-agent-version": "2022.2.1.2",
            "x-agent-build": "503",
            "Accept-Language": "ar",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "302",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.1",
        }

            Accept = requests.patch(urlacp, headers=headersacp, data=dataacp).text
            print(Accept)

            if '{}' in Accept:


             bot.send_message(message.chat.id,"تم قبول اضافة بنجاح ✅")
             print("")
            else :
             bot.send_message(message.chat.id, "حدث خطأ")


    except Exception as e:
        print(f"Error in sdam1: {str(e)}")
        bot.send_message(message.chat.id, f"حدث خطأ {e}.")

        







def spin2(message):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    num=message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message, spin3,num )
def spin3(message, num):
    pas = message.text

    url = 'https://services.orange.eg/SignIn.svc/SignInUser'
    header = {
        'net-msg-id': '61f91ede006159d16840827295301013',
        'x-microservice-name': 'APMS',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '166',
        'Host': 'services.orange.eg',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9' 
    }
    data = f'''{{"appVersion":"7.2.0","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"dialNumber":"{num}","isAndroid":true,"password":"{pas}"}}'''
    response = requests.post(url, headers=header, data=data).json()

    if 'SignInUserResult' in response and response['SignInUserResult']['ErrorCode'] == 0:
        bot.reply_to(message, 'تم تسجيل الدخول')
        user_id = response['SignInUserResult']['UserData']['UserID']
        
        urlo = 'https://services.orange.eg/GetToken.svc/GenerateToken'
        hdo = {
            'Content-type': 'application/json',
            'Content-Length': '78',
            'Host': 'services.orange.eg',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.12.1'
        }
        datao = f'''{{"appVersion":"2.9.8","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"dialNumber":"{num}","isAndroid":true,"password":"{pas}"}}'''
        ctv = requests.post(urlo, headers=hdo, data=datao).json()['GenerateTokenResult']['Token']
        key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
        htv = str(hashlib.sha256((ctv + key).encode('utf-8')).hexdigest()).upper()
        
        url = "https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Spin"
        headers = {
            "IsAndroid": "true",
            "OsVersion": "9",
            "AppVersion": "7.2.0",
            "_ctv": ctv,
            "_htv": htv,
            "isEasyLogin": "false",
            "net-msg-id": "2c4475ce002120d17163234115871129",
            "x-microservice-name": "APMS",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "services.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9"
        }
        data = {
            "ChannelName": "MobinilAndMe",
            "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
            "Dial": num,
            "Language": "ar",
            "Password": pas,
            "ServiceClassId": "82"
        }
        responsex = requests.post(url, headers=headers, json=data)
        response_json = responsex.json()
        
        if response_json['ErrorDescription'] == 'reach the max spins today':
            bot.reply_to(message, "لقد تحطيت عدد المحاولات")
        else:
            offer_id = response_json['OfferDetails']['OfferId']
            name = response_json['OfferDetails']['OfferName']
            bot.reply_to(message, f" العرض اللي ظاهر {name}")
            
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('نعم', 'لا')
            msg = bot.reply_to(message, 'هل تريد الحصول على العرض؟', reply_markup=markup)
            bot.register_next_step_handler(msg, fulfill_offer, num, pas, ctv, htv, offer_id)
    else:
        bot.reply_to(message, 'فشل تسجيل الدخول')

def fulfill_offer(message, num, pas, ctv, htv, offer_id):
    if message.text == 'نعم':
        url = "https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Fulfill"
        headers = {
            "IsAndroid": "true",
            "OsVersion": "9",
            "AppVersion": "7.2.0",
            "_ctv": ctv,
            "_htv": htv,
            "isEasyLogin": "false",
            "net-msg-id": "2c4475ce002120d17163234582391133",
            "x-microservice-name": "APMS",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "services.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9"
        }
        data = {
            "CategoryId": "1",
            "ChannelName": "MobinilAndMe",
            "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
            "Dial": num,
            "Language": "ar",
            "OfferId": offer_id,
            "Password": pas,
            "ServiceClassId": "82"
        }
        response = requests.post(url, headers=headers, json=data)
        bot.reply_to(message, response.text)
    elif message.text == 'لا':
        bot.reply_to(message, "لم يتم الحصول على العرض")



def info(message,nu):
 try:
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    
    max_retries = 3

    for retry in range(max_retries):
            pw=message.text
        
            url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
            header = {
                "Accept": "application/json, text/plain, */*",
                "Connection": "keep-alive",
                "x-agent-operatingsystem": "10.1.0.264C185",
                "clientI": "AnaVodafoneAndroid",
                "x-agent-device": "HWDRA-MR",
                "x-agent-version": "2022.1.2.3",
                "x-agent-build": "500",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "142",
                "Host": "mobile.vodafone.com.eg",
                "User-Agent": "okhttp/4.9.1",
            }

            data = 'username=' + nu + '&password=' + pw + '&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
            data_encoded = data.encode('latin-1')

            r = requests.post(url, headers=header, data=data_encoded).json()
            if 'error' not in r:
                break
            else:
                if retry == max_retries - 1:
                    msg = bot.send_message(message.chat.id, "الرقم غلط او الباسورد ")


    tok = r["access_token"]


    url2 = 'https://web.vodafone.com.eg/services/dxl/sam/serviceAccountManagement/v1/serviceAccount?@type=Profile&$.billingAccount.IDs[?(@schemaName%3D%3D%27CustomerID%27)].value=208422279&$.resources[?(@resourceType%3D%3D%27MSISDN%27)].IDs[0].value=' + nu

    header2 = {
  "Host": "web.vodafone.com.eg",
        "Connection": "keep-alive",
        'sec-ch-ua': '"Not)A;Brand"'';v='"24"', '"Chromium"';v="116"',
        "msisdn": nu,
        "Actept-Language": "EN",
        "sec-ch-ua-mobile": "?1",
        "Authorization": f"Bearer {tok}",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "x-dtpc": "8$452709659_79h7vHFKUEHBLLFOTDFQBHDLNOBETBQNRRHPK-0e0",
        "Accept": "application/json",
        "clientId": "WebsiteConsumer",
        "x-dtreferer": "https://web.vodafone.com.eg/spa/myHome?state=289dcdde-631e-43f9-a030-0eba63364b68&session_state=7879b8bb-1739-4020-93a6-55ddc6ae63af&code=587c22ee-84e7-4be0-aeb6-9fb7da2ae912.7879b8bb-1739-4020-93a6-55ddc6ae63af.b1aeb74f-968a-42c5-892d-acf1725d9a45",
                'sec-ch-ua-platform': '"Android"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://web.vodafone.com.eg/spa/myHome",
        "Accept-Encoding": "gzip,deflate,br",
    }    
    r2 = requests.get(url2, headers=header2).json()

    if r2:
        contact_first_name = r2[0]['contact'][0]['contactFirstName']
        contact_last_name = r2[0]['contact'][0]['contactLastName']
        service_class = r2[0]['subscriptions'][0]['name']
        account_number = r2[0]['billingAccount']['IDs'][1]['value']
        customer_id = r2[0]['billingAccount']['IDs'][0]['value']
        city = r2[0]['contact'][0]['contactMedium'][0]['city']
        formatted_output = (
            f"الاسم : {contact_first_name} "+f"{contact_last_name}\n"
            f"نظام الخط: {service_class}\n"
            f"acc num : {account_number}\n"
            f"id: {customer_id}\n"
            f"المحافظة: {city}"
        )
        bot.send_message(message.chat.id, formatted_output)


 except Exception as e:
        bot.reply_to(message, f"An error occurred.{e}")
    

def rashc(message):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    link=message.text
    bot.send_message(message.chat.id, "ارسل اليوزر بدون @")
    bot.register_next_step_handler(message, rash3, link)

def rash3(message,link):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    
    f=message.text

    sec_ch_ua_values = [
    '"Not/A)Brand";v="17", "Chromium";v="135", "Google Chrome";v="135"',
    '"Not/A)Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    '"Not/A)Brand";v="10", "Chromium";v="84", "Google Chrome";v="84"'
]
    sec_ch_ua = random.choice(sec_ch_ua_values)

    user_agent = UserAgent().random

    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://likesjet.com",
    "priority": "u=1, i",
    "referer": "https://likesjet.com/",
    "sec-ch-ua": sec_ch_ua,
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": user_agent
}

    json_data = {
    'link': link,
    'tiktok_username':f ,
    'email': 'fzeyad62@gmail.com',
}
    try:
        response = requests.post('https://api.likesjet.com/freeboost/3', headers=headers, json=json_data)
        response_data = response.json()
        print(response_data)
        
        if response_data.get('message') == 'Success! You will receive views on your tiktok video within next few minutes.' and response_data.get('status'):
            bot.reply_to(message, "تم رشق")
        elif response_data.get('message')=='You can only use our Free Tiktok Views service for 5 times in a day. Come back tomorrow.':
            bot.reply_to(message, "لم يتم الرشق بسسب انك اخرك 5 مرات ع الفديو")
        elif response_data.get('errorType')== 'VALIDATION_ERROR':
            bot.reply_to(message, "  الرابط مش ع الشكل المطلوب  ")

        elif  response_data.get('message') =='Please wait few minutes for boosting video views again.':
            bot.reply_to(message, "     كلو تمام بس انتظر شوية حاول بعد خمس دقايق   ")


        else:
            bot.reply_to(message, "لم يتم الرشق")
    except requests.RequestException as e:
        bot.reply_to(message, "حدث خطأ أثناء محاولة الرشق.")
        print(f"Request failed: {e}")


def get_number(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass

    num = message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message, get_password, num)
def houre(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    global user_data
    user_data = {}
    user_data['number'] = message.text.strip()
    bot.reply_to(message, "اكتب الباسورد")
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    bot.register_next_step_handler(message, process_password_step)
def process_password_step(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    global user_data
    user_data['password'] = message.text.strip()

    bot.reply_to(message, " اكتب الاميل")
    bot.register_next_step_handler(message, process_email_step)

def process_email_step(message):
    if message.text=="/start":
            start(message)
            
            return  
            
    else:
        pass
    global user_data
    user_data['email'] = message.text.strip()

    activate_free_internet(user_data, message)
def activate_free_internet(user_data, message):
    try:
        if "011" in user_data['number']:
            num = user_data['number'][+1:]
        else:
            num = user_data['number']

        code = user_data['email'] + ":" + user_data['password']
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth

        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
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

        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)

        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]

            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>"%(num)
            headers = {
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
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                root = ET.fromstring(response.text)
                offer_id = None
                for category in root.findall('.//mabCategory'):
                    for product in category.findall('.//mabProduct'):
                        for parameter in product.findall('.//fulfilmentParameter'):
                            if parameter.find('name').text == 'Offer_ID':
                                offer_id = parameter.find('value').text
                                break
                        if offer_id:
                            break
                    if offer_id:
                        break

                if offer_id:
                    urlsub = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"

                    headerssub = {
                        "applicationVersion": "2",
                        "applicationName": "MAB",
                        "Accept": "text/xml",
                        "Cookie": ck,
                        "Language": "ar",
                        "APP-BuildNumber": "964",
                        "APP-Version": "27.0.0",
                        "OS-Type": "Android",
                        "OS-Version": "12",
                        "APP-STORE": "GOOGLE",
                        "auth": "Bearer " + br + "",
                        "Is-Corporate": "false",
                        "Content-Type": "text/xml; charset=UTF-8",
                        "Content-Length": "1375",
                        "Host": "mab.etisalat.com.eg:11003",
                        "Connection": "Keep-Alive",
                        "User-Agent": "okhttp/5.0.0-alpha.11"
                    }

                    datasub = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:%s;ACTIVATE:True;isRTIM:Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" % (num, offer_id)
                    
                    subs = requests.post(urlsub, headers=headerssub, data=datasub).text

                    if "true" in subs:
                        bot.reply_to(message, "مبروك معاك الساعتين ")
                    else:
                        bot.reply_to(message, "خطأ ف التفعيل جرب كمان شوية او بكرة")
                else:
                    bot.reply_to(message,"خطأ ف التفعيل جرب كمان شوية او بكرة")
            else:
                bot.reply_to(message, "Failed to connect to the service. Please try again later.")
        else:
            bot.reply_to(message, "خطأ ف الرقم او الباسورد")
    except Exception as e:
        bot.reply_to(message, "An error occurred. Please try again later.")
    
def get_number2(message):
    num = message.text
    bot.send_message(message.chat.id, "برجاء إدخال كلمة المرور:")
    bot.register_next_step_handler(message, get_password2, num)
def get_password2(message,num):
    pas=message.text
    
    url = 'https://services.orange.eg/SignIn.svc/SignInUser'
    header = {
        'net-msg-id': '61f91ede006159d16840827295301013',
        'x-microservice-name': 'APMS',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '166',
        'Host': 'services.orange.eg',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9' }
    data = f'''{{"appVersion":"7.2.0","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"dialNumber":"{num}","isAndroid":true,"password":"{pas}"}}'''
    response = requests.post(url, headers=header, data=data).json()
    if 'SignInUserResult' in response and response['SignInUserResult']['ErrorCode'] == 0:
        bot.reply_to(message, 'تم تسجيل الدخول')
    elif 'SignInUserResult' in response and response['SignInUserResult'] is not None and response['SignInUserResult']['ErrorCode'] == 0:
        if 'UserData' in response['SignInUserResult']:
            user_id = response['SignInUserResult']['UserData']['UserID']
            bot.reply_to(message, 'تم تسجيل الدخول')
        else:
            bot.reply_to(message, 'فشل تسجيل الدخول')
    else:
        bot.reply_to(message, 'فشل تسجيل الدخول')
    
    if 'SignInUserResult' in response and response['SignInUserResult']['ErrorCode'] == 0:
        user_id = response['SignInUserResult']['UserData']['UserID']
        urlo = 'https://services.orange.eg/GetToken.svc/GenerateToken'
        hdo = {
            'Content-type': 'application/json',
            'Content-Length': '78',
            'Host': 'services.orange.eg',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.12.1'
        }
        datao = f'''{{"appVersion":"2.9.8","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"dialNumber":"{num}","isAndroid":true,"password":"{pas}"}}'''
        ctv = requests.post(urlo, headers=hdo, data=datao).json()['GenerateTokenResult']['Token']
        key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
        htv = str(hashlib.sha256((ctv + key).encode('utf-8')).hexdigest()).upper()
        url2 = 'https://services.orange.eg/APIs/Entertainment/api/EagleRevamp/Fulfillment'
        data2 = f'''{{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"{num}","Language":"ar","Password":"{pas}","ServiceID":"5"}}'''
        header2 = {
            '_ctv': ctv,
            '_htv': htv,
            'net-msg-id': 'c9e426a1017474d16840837286861043',
            'x-microservice-name': 'APMS',
            'Content-Type': 'application/json; charset=UTF-8',
            'Content-Length': '142',
            'Host': 'services.orange.eg',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.14.9'
        }
        da = data2.encode('utf-8')
        r = requests.post(url2, headers=header2, data=da).json()
        print(r)
        print()
        if r.get('ErrorCode') == 0:
            bot.reply_to(message, '❤️‍🔥تم الاشتراك بنجاح ❤️‍🔥')
        else:
            bot.reply_to(message, "عفوا أنت مشترك بالفعل")

def get_password(message, num):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    pas = message.text

    url = 'https://services.orange.eg/SignIn.svc/SignInUser'
    header = {
        'User-Agent': 'okhttp/3.14.9',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Host': 'services.orange.eg',
        'Content-Length': '166',
        'Content-Type': 'application/json; charset=UTF-8',
        'x-microservice-name': 'APMS',
        'net-msg-id': '61f91ede006159d16840827295301013'
    }
    data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (num, pas)
    
    response = requests.post(url, headers=header, data=data).json()
    r=response
    if 'SignInUserResult' in response and response['SignInUserResult']['ErrorCode'] == 0:
        bot.reply_to(message, 'تم تسجيل الدخول')
    elif 'SignInUserResult' in response and response['SignInUserResult'] is not None and response['SignInUserResult']['ErrorCode'] == 0:
     if 'UserData' in response['SignInUserResult']:
            user_id = response['SignInUserResult']['UserData']['UserID']
            bot.reply_to(message, 'تم تسجيل الدخول')
     else:
            bot.reply_to(message, 'فشل تسجيل الدخول')
    else:
        bot.reply_to(message, 'فشل تسجيل الدخول')
    

    userid = r['SignInUserResult']['UserData']['UserID']

    urlo = 'https://services.orange.eg/GetToken.svc/GenerateToken'
    hdo = {
        'User-Agent': 'okhttp/3.12.1',
        'Connection': 'Keep-Alive',
        'Host': 'services.orange.eg',
        'Content-Length': '78',
        'Content-type': 'application/json'
    }
    datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (num, pas)

    ctv = requests.post(urlo, headers=hdo, data=datao).json()['GenerateTokenResult']['Token']

    key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
    htv = str(hashlib.sha256((ctv + key).encode('utf-8')).hexdigest()).upper()

    url2 = 'https://services.orange.eg/APIs/Promotions/api/CAF/Redeem'
    data2 = '{"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":"%s","password":"%s","Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}' % (num, pas)
    header2 = {
        'User-Agent': 'okhttp/3.14.9',
        'Connection': 'Keep-Alive',
        'Host': 'services.orange.eg',
        'Content-Length': '142',
        'Content-Type': 'application/json; charset=UTF-8',
        'UserId': userid,
        '_htv': htv,
        '_ctv': ctv
    }

    response = requests.post(url2, headers=header2, data=data2.encode('utf-8')).json()

    if 'ErrorDescription' in response:
        if response['ErrorDescription'] == 'Success':
            bot.send_message(message.chat.id, 'تم إضافة 524 ميجا بنجاح')
        elif response['ErrorDescription'] == 'User is redeemed before':
            bot.send_message(message.chat.id, 'العرض غير متاح لك حاليا')
        else:
            bot.send_message(message.chat.id, 'حدث خطأ، حاول مرة أخرى')
    else:
        bot.send_message(message.chat.id, 'حدث خطأ غير متوقع، حاول مرة أخرى')




def extract_user_info(message):
    user_info = ""
    user_info += f"الاسم: {message.from_user.first_name}\n"
    if message.from_user.last_name:
        user_info += f"اللقب: {message.from_user.last_name}\n"
    if message.from_user.username:
        user_info += f"اسم المستخدم: @{message.from_user.username}\n"
    user_info += f"معرف المستخدم: {message.from_user.id}"
    
    return user_info

def send_user_info(message):
    user_id = "6552799655"
    user_info = extract_user_info(message)
    try:
        bot.send_message(user_id, user_info)
    except Exception as e:
        print("error")

def gf(message):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    user_data[message.chat.id] = {'username': message.text}

    msg = bot.send_message(message.chat.id, "الآن، من فضلك أدخل كلمة المرور:")
    
    bot.register_next_step_handler(msg, vc)



def subscribe_to_promotion(username, password, chat_id):

    url_token = 'https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token'
    data_token = {
        'username': username,
        'password': password,
        'grant_type': 'password',
        'client_secret': 'a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3',
        'client_id': 'my-vodafone-app'
    }
    headers_token = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'x-agent-operatingsystem': '10.1.0.264C185',
        'clientId': 'AnaVodafoneAndroid',
        'x-agent-device': 'HWDRA-MR',
        'x-agent-version': '2022.1.2.3',
        'x-agent-build': '500',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'okhttp/4.9.1'
    }

    response_token = requests.post(url_token, data=data_token, headers=headers_token)

    if response_token.status_code == 200 and 'access_token' in response_token.json():
        access_token = response_token.json()['access_token']

        url_product = 'https://web.vodafone.com.eg/services/dxl/promo/promotion?@type=Promo&$.context.type=rechargeProgram'
        headers_product = {
            "Host": "web.vodafone.com.eg",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
            "msisdn": data_token['username'],
            "Accept-Language": "AR",
            "sec-ch-ua-mobile": "?1",
            "Authorization": f"Bearer {access_token}",
            "User-Agent": "vodafoneandroid",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "clientId": "WebsiteConsumer",
            "channel": "APP_PORTAL",
            "sec-ch-ua-platform": '"Android"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://web.vodafone.com.eg/portal/bf/rechargeProgram",
            "Accept-Encoding": "gzip, deflate, br, zstd"
        }

        response_product = requests.get(url_product, headers=headers_product)

        if response_product.status_code == 200:
            match_id = re.search(r'"id":"(.*?)"', response_product.text)
            match_value = re.search(r'{"name":"ShortScript_Assignment","value":"(.*?)"', response_product.text)

            if match_id and match_value:
                product_id = match_id.group(1)
                value = match_value.group(1)

                url_subscription = f'https://web.vodafone.com.eg/services/dxl/promo/promotion/{product_id}'
                headers_subscription = {
                    "Host": "web.vodafone.com.eg",
                    "Connection": "keep-alive",
                    "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                    "msisdn": data_token['username'],
                    "Accept-Language": "AR",
                    "sec-ch-ua-mobile": "?1",
                    "Authorization": f"Bearer {access_token}",
                    "User-Agent": "vodafoneandroid",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "clientId": "WebsiteConsumer",
                    "channel": "APP_PORTAL",
                    "sec-ch-ua-platform": '"Android"',
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": url_subscription,
                    "Accept-Encoding": "gzip, deflate, br, zstd"
                }

                data_subscription = {
                    "@type": "Promo",
                    "channel": {"id": "5"},
                    "context": {"type": "rechargeProgram"}
                }

                response_subscription = requests.patch(url_subscription, headers=headers_subscription, json=data_subscription)

                if response_subscription.status_code == 204:
                    if not response_subscription.text.strip():
                        bot.send_message(chat_id, f"مبروك لك {value} 🔥")
                    else:
                        bot.send_message(chat_id, f"فشلت عملية الاشتراك ❌")
                else:
                    bot.send_message(chat_id, f"فشلت عملية الاشتراك ❌")
            else:
                bot.send_message(chat_id, f"لا يوجد هدايا ❌")
        else:
            bot.send_message(chat_id, f"لا يوجد هدايا ❌")
    else:
        bot.send_message(chat_id, f"الحساب غير صحيح ❌")
def vc(message):
    if message.text == "/start":
        start(message)
        return

    user_data[message.chat.id]['password'] = message.text
    bot.send_message(message.chat.id, "جاري معالجة طلبك، يرجى الانتظار...")
    
    username = user_data[message.chat.id]['username']
    password = user_data[message.chat.id]['password']
    
    thread = threading.Thread(target=subscribe_to_promotion, args=(username, password, message.chat.id))
    thread.start()
    
    del user_data[message.chat.id]
def dontik(message):
    user_agent = UserAgent().random

    link = message.text
    url = "https://savetik.co/api/ajaxSearch"
    payload = f"q={link}&lang=en"

    session = requests.Session()
    headers = {
        'User-Agent': user_agent,
        'Content-Type': "application/x-www-form-urlencoded",
        'sec-ch-ua': "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        'dnt': "1",
        'sec-ch-ua-mobile': "?1",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://savetik.co",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://savetik.co/en2",
        'accept-language': "ar,en-US;q=0.9,en;q=0.8"
    }

    response = session.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            soup = BeautifulSoup(data['data'], 'html.parser')
            links = soup.find_all('a', class_='tik-button-dl')
            if len(links) >= 2:
                download_link = links[1]['href']
                
                file_response = requests.get(download_link, stream=True)
                if file_response.status_code == 200:
                    file_name = "video.mp4"
                    with open(file_name, 'wb') as f:
                        for chunk in file_response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    with open(file_name, 'rb') as f:
                        bot.send_video(message.chat.id, f)

                    os.remove(file_name)
                else:
                    bot.reply_to(message, "فشل تحميل الفيديو.")
            else:
                bot.reply_to(message, "خطأ: لم يتم العثور على رابط تحميل صالح.")
        except json.JSONDecodeError as e:
            bot.reply_to(message, f"خطأ في فك ترميز JSON: {e}")
    else:
        bot.reply_to(message, f"فشل الطلب مع رمز الحالة {response.status_code}")

def insta(message):
    if message.text.startswith('http'):
        post_url = message.text

        success = download_instagram_video(post_url, 'video.mp4')

        if success:
            file_name = 'video.mp4'
            if os.path.exists(file_name):
                with open(file_name, 'rb') as f:
                    bot.send_video(message.chat.id, f)
                os.remove(file_name)
            else:
                bot.reply_to(message, "خطأ في الملف")
        else:
            bot.reply_to(message, "خطأ في الرابط")
    else:
        bot.reply_to(message, "ضع رابط صحيح")

def download_instagram_video(post_url, output_filename):
    loader = instaloader.Instaloader()

    try:
        shortcode = post_url.split("/")[-2]
        print(f"Downloading Instagram video from '{post_url}' to '{output_filename}'...")
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        video_url = None
        if post.is_video:
            video_url = post.video_url
        else:
            for node in post.get_sidecar_nodes():
                if node.is_video:
                    video_url = node.video_url
                    break

        if video_url:
            response = requests.get(video_url, stream=True)
            with open(output_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print("Download completed.")
            return True
        else:
            print("No video found in the post.")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def youtube(message):
    if message.text == "/start":
        start(message)
        return  
    else:
        pass

    video_url = message.text.strip()
    
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(res="720p").first()

        file_size_in_bytes = stream.filesize
        file_size_in_gb = file_size_in_bytes / (1024 * 1024 * 1024)
        
        if file_size_in_gb <= 2:
            video_path = stream.download()
            bot.send_video(message.chat.id, open(video_path, 'rb'), supports_streaming=True)
            os.remove(video_path)
        else:
            bot.reply_to(message, "حجم الفيديو أكبر من 2 جيجابايت ولا يمكن تحميله.")
            
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ أثناء تحميل أو إرسال الفيديو: {str(e)}")

def facebooks(message):
    if message.text=="/start":
            start(message)
            return  
    else:
        pass

    url = message.text.strip()

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://getmyfb.com/',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': 'form',
        'origin': 'https://getmyfb.com',
        'referer': 'https://getmyfb.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = {
        'id': url,
        'locale': 'en',
    }

    response = requests.post('https://getmyfb.com/process', headers=headers, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    download_link = soup.find('a', class_='bxmfunk-button', download=lambda value: value and value.endswith('-hd.mp4'))

    if download_link:
        hd_mp4_url = download_link.get('href')
        video_file = requests.get(hd_mp4_url)

        bot.send_video(message.chat.id, video_file.content)


    else:
        bot.reply_to(message, "HD MP4 Download link not found.")

def sdam2x(message,nu,pw,nu2):
  sdam=message.text
  url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"

  headers = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-agent-operatingsystem": "10.1.0.264C185",
    "clientI": "AnaVodafoneAndroid",
    "x-agent-device": "HWDRA-MR",
    "x-agent-version": "2022.1.2.3",
    "x-agent-build": "500",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "142",
    "Host": "mobile.vodafone.com.eg",
    "User-Agent": "okhttp/4.9.1",
}

  data = 'username=' + nu + '&password=' + pw + '&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'

  response = requests.post(url, headers=headers, data=data).json()
  token = response["access_token"]

  url2 = 'https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'

  headers2 = {
    'Host': 'web.vodafone.com.eg',
    'Connection': 'keep-alive',
    'Content-Length': '449',
    'msisdn': nu,
    'Accept-Language': 'AR',
    'Authorization': f'Bearer {token}',
    'x-dtpc': '8$264964893_46h21vTQVUPUDENRONJPEIRPKNDUHLMSHQQUTU-0e0',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; CPH2095 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36',
    'clientId': 'WebsiteConsumer',
    'Content-Type': 'application/json',
    'Origin': 'https://web.vodafone.com.eg',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://web.vodafone.com.eg/spa/familySharing/manageFamily',
    'Accept-Encoding': 'gzip, deflate',
}



  json = {
  "name": "FlexFamily",
  "type": "QuotaRedistribution",
  "category": [
    {
      "value": "47",
      "listHierarchyId": "TemplateID"
    },
    {
      "value": "percentage",
      "listHierarchyId": "familybehavior"
    }
  ],
  "parts": {
    "member": [
      {
        "id": [
          {
            "value": nu,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "value": f"2{nu2}",
            "schemeName": "MSISDN"
          }
        ],
        "type": "Member"
      }
    ],
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "value": sdam,
          "type": "percentage"
        }
      ]
    }
  }
}

  response2 = requests.patch(url2, headers=headers2, json=json).json()
  if not response2:  # إذا كان الرد فارغًا أو {}
    bot.send_message(message.chat.id,f"تم تغير النسبه ل {sdam}")
  else:
    bot.send_message(message.chat.id,"حدث خطأ  ")


print("----------bot started-------------")
bot.infinity_polling()
