import telebot
from telebot import types

bot = telebot.TeleBot("7504616814:AAE-toFkzsXufqMIxa-YLuzJhD9P7KfmTSQ")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🏦 Получить реферальную ссылку")
    btn2 = types.KeyboardButton("ℹ️ Информация")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для получения реферальных ссылок банков. Выбери действие:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🏦 Получить реферальную ссылку")
def ref(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    alfa_500 = types.InlineKeyboardButton(text='Карта альфа банк (500руб)', callback_data="REF_ALFA_500")
    alfa_GOLD_APPLE = types.InlineKeyboardButton(text='Карта альфа банк (Золотое яблоко)', callback_data="REF_ALFA_GOLD_APPLE")
    MTS = types.InlineKeyboardButton(text='Карта МТС банк', callback_data="REF_MTS")
    PSB = types.InlineKeyboardButton(text='Карта ПСБ банк', callback_data="REF_PSB")
    INVEST_ALFA = types.InlineKeyboardButton(text='Инвест счёт альфа банка', callback_data="REF_INVEST_ALFA")
    GAZ_PROM = types.InlineKeyboardButton(text='Карта газпром банка', callback_data="REF_GAZ_PROM")


    keyboard.add(alfa_500)
    keyboard.add(alfa_GOLD_APPLE)
    keyboard.add(MTS)
    keyboard.add(PSB)
    keyboard.add(INVEST_ALFA)
    keyboard.add(GAZ_PROM)

    bot.send_message(message.chat.id, "Выберите карту:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "REF_ALFA_500":
        bot.send_message(call.message.chat.id, "🏦КАРТА АЛЬФА БАНК🏦\n"
                                               "Всего за несколько действий оформления карты «<b>АЛЬФА БАНКА</b>» ты получаешь 500 РУБЛЕЙ💵\n\n"
                                               "Данную карту можно оформить уже с \n1️⃣4️⃣➕\n\n"
                                               "чтобы получить вознаграждение нужно сделать несколько действий:\n\n"
                                               "1️⃣<b>Оформить карту по данной ссылке</b> https://clck.ru/3MgtJt\n\n"
                                               "2️⃣<b>Получить карту</b> \n\n"
                                               "3️⃣<b>Сделать любую покупку от 100 рублей</b> \n\n"
                                               "Если ты выполнил все пункты то 500 рублей придут тебе в течении 5 дней🧾", parse_mode='HTML')


    elif call.data == "REF_ALFA_GOLD_APPLE":
        bot.send_message(call.message.chat.id, "🏦КАРТА АЛЬФА БАНК🏦\n"
                                               "Оформив карту «<b>АЛЬФА БАНКА</b>» за пару дней , ты получаешь СЕРТИФИКАТ В ЗОЛОТЕ ЯБЛОКО ✨ на сумму 1200 рублей\n\n"
                                               "Данную карту можно оформить уже с \n1️⃣4️⃣➕\n"
                                               "чтобы получать сертификат нужно выполнить пару действий:\n\n"
                                               "1️⃣<b>Оформить карту по данной ссылке</b> https://clck.ru/3MaeLN\n\n"
                                               "2️⃣<b>Забрать карту</b>\n\n"
                                               "3️⃣<b>Сделать любую покупку от 100 рублей</b> \n\n"
                                               "Если ты выполнил все пункты то сертификат придёт тебе в течении месяца🍐", parse_mode='HTML')


    elif call.data == "REF_MTS":
        bot.send_message(call.message.chat.id, "🏦КАРТА МТС БАНК🏦\n"
                                               "Оформив карту «<b>МТС БАНКА</b>» ты получаешь сертификат на выбор: OZON , либо ЗОЛОТОЕ ЯБЛОКО,на сумму 1000 рублей💵\n\n"
                                               "Данную карту можно оформить с\n1️⃣8️⃣➕ \n"
                                               "Для того чтобы получить сертификат нужно сделать несколько действий:\n\n"
                                               "1️⃣<b>Оформить карту по данной ссылке</b> https://clck.ru/3MaeH2\n\n"
                                               "2️⃣<b>Забрать карту</b>\n\n"
                                               "3️⃣<b>Сделать покупку на сумму от 501 рубля</b>\n\n"
                                               "Если все пункты выполнены то сертификат придёт в течении месяца 💅", parse_mode='HTML')


    elif call.data == "REF_PSB":
        bot.send_message(call.message.chat.id, "🏦КАРТА ПСБ БАНКА🏦\n"
                                               "Оформив карту «<b>ПСБ БАНКА</b>» ты получаешь СЕРТИФИКАТ В ЗОЛОТОЕ ЯБЛОКО💅на сумму 1000 рублей 💵\n\n"
                                               "Данную карту можно оформить с \n1️⃣4️⃣➕\n"
                                               "чтобы забрать сертификат нужно сделать несколько действий:\n\n"
                                               "1️⃣<b>Оформить карту по данной ссылке</b> https://clck.ru/3Mawgm\n\n"
                                               "2️⃣<b>Получить карту</b>\n\n"
                                               "3️⃣<b>Сделать покупку от 1000 рублей</b> \n\n"
                                               "Если ты все сделал то сертификат придёт в течении месяца 🍐", parse_mode='HTML')




    elif call.data == "REF_INVEST_ALFA":
        bot.send_message(call.message.chat.id, "Ссылка на реферальную программу для инвестиционного счёта Альфа банка: [ссылка]", parse_mode='HTML')





    elif call.data == "REF_GAZ_PROM":
        bot.send_message(call.message.chat.id, "⛽️КАРТА ГАЗПРОМ БАНКА⛽️\n"
                                               "Оформив карту «<b>ГАЗПРОМ БАНКА</b>» ты получаешь 1000 рублей 💵\n\n"
                                               "Данную карту можно оформить с 1️⃣8️⃣➕\nчтобы получить вознаграждение нужно выполнить несколько действий:\n\n"
                                               "1️⃣<b>Заказать карту по данной ссылке</b> https://clck.ru/3Mawvi \n\n"
                                               "2️⃣<b>Забрать карту</b>\n\n"
                                               "3️⃣<b>Сделать покупку от 1000 рублей</b> \n\n"
                                               "Если ты выполнил все пункты то ожидай выплату в течении двух недель 💵", parse_mode='HTML')


    bot.answer_callback_query(call.id)


@bot.message_handler(func=lambda message: message.text == "ℹ️ Информация")
def info(message):
    bot.send_message(message.chat.id, "📌 Этот бот предоставляет реферальные ссылки для оформления карт в разных банках.\n\n"
        "🔹 При регистрации по ссылке ты и я получаем бонусы (деньги, кэшбэк и т.д.).\n"
        "🔹 Выбирай банк и переходи по ссылке для оформления.\n\n"
        "❓ Вопросы? Пиши @@BANDERASBLACK", parse_mode='HTML')



bot.polling(none_stop=True)