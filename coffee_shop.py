import telebot
bot = telebot.TeleBot("...")
from telebot import types
user_queue = []
@bot.message_handler(commands=['start'])
def initial_part(message):
    mark_up = types.ReplyKeyboardMarkup(resize_keyboard=True)
    botton_1 = types.KeyboardButton("📕 Меню")
    botton_2 = types.KeyboardButton("📞 Контакты")
    mark_up.add(botton_1, botton_2)
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}! , что вы хотели бы заказать? ".format(message.from_user), reply_markup=mark_up)

@bot.message_handler(content_types=['text'])
def functionality(message):
    if (message.text == "📕 Меню"):
        b_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botton_1 = types.KeyboardButton("Американо")
        botton_2 = types.KeyboardButton("Эспрессо")
        botton_3 = types.KeyboardButton("Капучино")
        botton_4 = types.KeyboardButton("Латте")
        botton_5 = types.KeyboardButton("Какао")
        botton_6 = types.KeyboardButton("Горячий шоколад")
        botton_7 = types.KeyboardButton("Фраппучино")
        re_turn = types.KeyboardButton("Вернуться в главное меню")
        b_mar.add(botton_1, botton_2, botton_3, botton_4, botton_5, botton_6, botton_7, re_turn)
        bot.send_message(message.chat.id, text="У нас в ассортименте есть: \n1.Американо \n2.Эспрессо \n3.Капучино \n4.Латте \n5.Какао \n6.Горячий шоколад \n7.Фраппучино ", reply_markup=b_mar)

    elif (message.text in ["0.3л", "0.4л"]):
        user_queue.append(message.text)
        order = " ".join(user_queue)
        bot.send_message(message.chat.id, text="Ваш заказ: " + order + ". Принимаете ли вы заказ?")

    elif (message.text == "Да"):
        order = " ".join(user_queue)
        bot.send_message(message.chat.id, text="Ваш заказ: " + order + ", успешно оформлен")
        user_queue.clear()
        user_queue.clear()

    elif (message.text == "Нет"):
        order = " ".join(user_queue)
        bot.send_message(message.chat.id, text="Упс, вышла ошибка. По пробуйте еще раз")
        user_queue.clear()
        user_queue.clear()
        user_queue.clear()

    elif (message.text == "Американо"):
        qt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt_1 = types.KeyboardButton("0.3л")
        bt_2 = types.KeyboardButton("0.4л")
        repay = types.KeyboardButton("Вернуться в главное меню")
        qt.add(bt_1, bt_2, repay)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=qt)
        user_queue.append(message.text)

    elif (message.text == "Капучино"):
        tt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("0.3л")
        bt2 = types.KeyboardButton("0.4л")
        repay_1 = types.KeyboardButton("Вернуться в главное меню")
        tt.add(bt1, bt2, repay_1)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=tt)
        user_queue.append(message.text)

    elif (message.text == "Эспрессо"):
        xt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt8 = types.KeyboardButton("0.3л")
        bt9 = types.KeyboardButton("0.4л")
        repay_4 = types.KeyboardButton("Вернуться в главное меню")
        xt.add(bt8, bt9, repay_4)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=xt)
        user_queue.append(message.text)

    elif (message.text == "Горячий шоколад"):
        ct = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt10 = types.KeyboardButton("0.3л")
        bt11 = types.KeyboardButton("0.4л")
        repay_5 = types.KeyboardButton("Вернуться в главное меню")
        ct.add(bt10, bt11, repay_5)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=ct)
        user_queue.append(message.text)

    elif (message.text == "Какао"):
        wt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt3 = types.KeyboardButton("0.3л")
        bt4 = types.KeyboardButton("0.4л")
        repay_2 = types.KeyboardButton("Вернуться в главное меню")
        wt.add(bt3, bt4, repay_2)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=wt)
        user_queue.append(message.text)

    elif (message.text == "Фраппучино"):
        ht = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt5 = types.KeyboardButton("0.3л")
        bt6 = types.KeyboardButton("0.4л")
        repay_3 = types.KeyboardButton("Вернуться в главное меню")
        ht.add(bt5, bt6, repay_3)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=ht)
        user_queue.append(message.text)

    elif (message.text == "Латте классический"):
        zt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt12 = types.KeyboardButton("0.3л")
        bt13 = types.KeyboardButton("0.4л")
        repay_6 = types.KeyboardButton("Вернуться в главное меню")
        zt.add(bt12, bt13, repay_6)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=zt)
        user_queue.append(message.text)

    elif (message.text == "Латте с сиропом"):
        mt = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt14 = types.KeyboardButton("0.3л")
        bt15 = types.KeyboardButton("0.4л")
        repay_7 = types.KeyboardButton("Вернуться в главное меню")
        mt.add(bt14, bt15, repay_7)
        bot.send_message(message.chat.id, text="1. 0.3\n2. 0.4", reply_markup=mt)
        user_queue.append(message.text)

    elif (message.text == "Латте"):
        a_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botton1 = types.KeyboardButton("Латте классический")
        botton2 = types.KeyboardButton("Латте с сиропом")
        come_back = types.KeyboardButton("Вернуться назад")
        a_mar.add(botton1, botton2, come_back)
        bot.send_message(message.chat.id, text="1.Латте классический \n2.Латте с сиропом", reply_markup=a_mar)

    elif (message.text == "Вернуться назад"):
        a_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botton_1 = types.KeyboardButton("Американо")
        botton_2 = types.KeyboardButton("Эспрессо")
        botton_3 = types.KeyboardButton("Капучино")
        botton_4 = types.KeyboardButton("Латте")
        botton_5 = types.KeyboardButton("Какао")
        botton_6 = types.KeyboardButton("Горячий шоколад")
        botton_7 = types.KeyboardButton("Фраппучино")
        re_turn = types.KeyboardButton("Вернуться в главное меню")
        a_mar.add(botton_1, botton_2, botton_3, botton_4, botton_5, botton_6, botton_7, re_turn)
        bot.send_message(message.chat.id, text="Вернуться назад", reply_markup=a_mar)


    elif (message.text == "📞 Контакты"):
        c_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Номер телефона")
        btn_2 = types.KeyboardButton("Адрес")
        btn_3 = types.KeyboardButton("Почта")
        back = types.KeyboardButton("Вернуться в главное меню")
        c_mar.add(btn_1, btn_2, btn_3, back)
        bot.send_message(message.chat.id, text="Что вы ищите?", reply_markup=c_mar)

    elif (message.text == "Номер телефона"):
        bot.send_message(message.chat.id, "87779602483")

    elif message.text == "Адрес":
        bot.send_message(message.chat.id, text=" Шоссе Корғалжын, 8")

    elif message.text == "Почта":
        bot.send_message(message.chat.id, text=" 01islamk@gmail.com")

    elif (message.text == "Вернуться в главное меню"):
        d_mar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("📕 Меню")
        button2 = types.KeyboardButton("📞 Контакты")
        d_mar.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=d_mar)

bot.polling(none_stop=True)
