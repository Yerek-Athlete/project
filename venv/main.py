from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from Logger import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup

#import Order
import order_truck
#import ru

Text = "Жем-шөп турауға арналған дробилкалардың⚙ түрлерін жасаймыз\n 25-5000 ірі-қараға🐄  жем-шөп әзірлеуге 40-тан астам түрі бар🔌🚜\n Дробилкаларды қандай мақсатта қолданасыз?\nЖалғастыру⏯ үшін\n  /next түймесін басыңыз "
text_kz = "Дробилкаларды қандай мақсатта қолданасыз?"


text_else = "Конпкаларды ғана қолданыңыз || Используете только кнопку"

support = "Техникалық қателер туындағанда админстратор номеріне хабарласыңыз📞: 87471850499\nВ случае технических ошибок звоните по номеру администратора📞: 87471850499"

# Глобальды айнымалы!
send_data = "5"
#

'''b1 = KeyboardButton('Kz-kz')
b2 = KeyboardButton('Ru-ru')
'''
#markup_language = ReplyKeyboardMarkup().row(b1, b2)
#markup_language = ReplyKeyboardMarkup().add(b1, b2)

#1
inline_drobilka = InlineKeyboardMarkup()
mal = InlineKeyboardButton("Мал шаруашылығы 🐑 ", callback_data='mall')
zhem = InlineKeyboardButton("Жем 🌾 саудасы", callback_data='zhemm')
inline_drobilka.insert(zhem)
inline_drobilka.insert(mal)
#inline_drobilka = InlineKeyboardMarkup().add(zhem)
#end

#2 Choose
inline_chose = InlineKeyboardMarkup()
electrical = InlineKeyboardButton("Электр тоғымен 🔌", callback_data='elec')
truck = InlineKeyboardButton("Трактормен 🚜", callback_data='trucks')
inline_chose.insert(electrical)
inline_chose.insert(truck)
#end

#3 List
inline_electrical = InlineKeyboardMarkup()
inline_zhem3 = InlineKeyboardButton("Жемге 3КВт-тық ~220В🔌 ", callback_data='zhem3')
inline_shop3 = InlineKeyboardButton("Шөпке 3КВт-тық ~220В🔌 ", callback_data='grass3')

inline_zhem4 = InlineKeyboardButton("Жемге 4КВт-тық ~380В🔌 ", callback_data='zhem4')
inline_shop4 = InlineKeyboardButton("Шөпке 4КВт-тық ~380В🔌 ", callback_data='grass4')

inline_zhem5_5 = InlineKeyboardButton("Жемге 5.5КВт-тық ~380Вольтта🔌 ", callback_data='zhem5_5')
inline_shop5_5 = InlineKeyboardButton("Шөпке 5.5КВт-тық ~380Вольтта🔌 ", callback_data='grass5_5')

inline_zhem7_5 = InlineKeyboardButton("Жемге 7.5КВт-тық ~380Вольтта🔌 ", callback_data='zhem7_5')
inline_shop7_5 = InlineKeyboardButton("Шөпке 7.5КВт-тық ~380Вольтта🔌 ", callback_data='grass7_5')

inline_zhem11 = InlineKeyboardButton("Жемге 11КВт-тық ~380Вольтта🔌 ", callback_data='zhem11')
inline_shop11 = InlineKeyboardButton("Шөпке 11КВт-тық ~380Вольтта🔌 ", callback_data='grass11')

inline_zhem15 = InlineKeyboardButton("Жемге 15КВт-тық ~380Вольтта🔌 ", callback_data='zhem15')
inline_shop15 = InlineKeyboardButton("Шөпке 15КВт-тық ~380Вольтта🔌 ", callback_data='grass15')

inline_zhem18_5 = InlineKeyboardButton("Жемге 18.5КВт-тық ~380Вольтта🔌 ", callback_data='zhem18_5')
inline_shop18_5 = InlineKeyboardButton("Шөпке 18.5КВт-тық ~380Вольтта🔌 ", callback_data='grass18_5')

inline_zhem22 = InlineKeyboardButton("Жемге 22КВт-тық ~380Вольтта🔌 ", callback_data='zhem22')
inline_shop22 = InlineKeyboardButton("Шөпке 22КВт-тық ~380Вольтта🔌 ", callback_data='grass22')

inline_electrical.insert(inline_zhem3)
inline_electrical.insert(inline_shop3)
inline_electrical.insert(inline_zhem4)
inline_electrical.insert(inline_shop4)
inline_electrical.insert(inline_zhem5_5)
inline_electrical.insert(inline_shop5_5)
inline_electrical.insert(inline_zhem7_5)
inline_electrical.insert(inline_shop7_5)
inline_electrical.insert(inline_zhem11)
inline_electrical.insert(inline_shop11)
inline_electrical.insert(inline_zhem15)
inline_electrical.insert(inline_shop15)
inline_electrical.insert(inline_zhem18_5)
inline_electrical.insert(inline_shop18_5)
inline_electrical.insert(inline_zhem22)
inline_electrical.insert(inline_shop22)
# end

#4 Truck
inline_truck = InlineKeyboardMarkup()

truck_zhem1500 = InlineKeyboardButton("Жемге 1500кг/сағ", callback_data='zhem_1500')
truck_shop2500 = InlineKeyboardButton("Шөпке 2500кг/сағ", callback_data='grass_2500')

truck_zhem2000 = InlineKeyboardButton("Жемге 2000кг/сағ", callback_data='zhem_2000')
truck_shop3000 = InlineKeyboardButton("Шөпке 3000кг/сағ", callback_data='grass_3000')

truck_zhem2500 = InlineKeyboardButton("Жемге 2500кг/сағ", callback_data='zhem_2500')
truck_shop3000 = InlineKeyboardButton("Шөпке 4000кг/сағ", callback_data='grass_4000')

truck_zhem3000 = InlineKeyboardButton("Жемге 3000кг/сағ", callback_data='zhem_3000')
truck_shop5000 = InlineKeyboardButton("Шөпке 5000кг/сағ", callback_data='grass_5000')

inline_truck.insert(truck_zhem1500)
inline_truck.insert(truck_shop2500)
inline_truck.insert(truck_zhem2000)
inline_truck.insert(truck_shop3000)
inline_truck.insert(truck_zhem2500)
inline_truck.insert(truck_shop3000)
inline_truck.insert(truck_zhem3000)
inline_truck.insert(truck_shop5000)

#end

'''
InlineKeyboardButton("Жемге 11КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh11')
InlineKeyboardButton("Жемге 15КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh15')
InlineKeyboardButton("Жемге 18.5КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh18_5')
InlineKeyboardButton("Жемге 22КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh22')
'''




#Universal
inline_universal = InlineKeyboardMarkup()
uni_zhem_shop11 = InlineKeyboardButton("Жемге 11КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh11')
#uni_zhem_shop_zh3 = InlineKeyboardButton("3Квт Жем-Шөп-Жүгері", callback_data='uni_zh_grass_zh3')

uni_zhem_shop15 = InlineKeyboardButton("Жемге 15КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh15')
#uni_zhem_shop_zh4 = InlineKeyboardButton("4Квт Жем-Шөп-Жүгері", callback_data='uni_zh_grass_zh4')

uni_zhem_shop18_5 = InlineKeyboardButton("Жемге 18.5КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh18_5')
#uni_zhem_shop_zh5_5 = InlineKeyboardButton("5.5Квт Жем-Шөп-Жүгері", callback_data='uni_zh_grass_zh5_5')

uni_zhem_shop22 = InlineKeyboardButton("Жемге 22КВт-тық ~380Вольтта🔌 ", callback_data='uni_zh22')
#uni_zhem_shop_zh7_5 = InlineKeyboardButton("7.5Квт Жем-Шөп-Жүгері", callback_data='uni_zh_grass_zh7_5')

inline_universal.insert(uni_zhem_shop11)
inline_universal.insert(uni_zhem_shop15)
inline_universal.insert(uni_zhem_shop18_5)
inline_universal.insert(uni_zhem_shop22)
#end

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, text=Text)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, text=support)
    
@dp.message_handler(commands=['tap'])
async def kz(message: types.Message):
    await bot.send_message(message.from_user.id, text=text_kz, reply_markup=inline_drobilka)



@dp.message_handler(commands=['con'])
async def con(message: types.Message):
    await bot.send_message(message.from_user.id, text="🔌/🚜", reply_markup=inline_chose)

@dp.message_handler(commands=['E'])
async def E(message: types.Message):
    await bot.send_message(message.from_user.id, text="Бізде электрикалық🔌 дробилкалардың түрі өте көп. Қуат күшіне қарай таңдап алыңыз!", reply_markup=inline_electrical )

@dp.message_handler(commands=['T'])
async def E(message: types.Message):
    await bot.send_message(message.from_user.id, text="Трактор🚜 соқасымен жұмыс жасайтын дробилка",
                           reply_markup=inline_truck)



@dp.message_handler(commands=['universal'])
async def E(message: types.Message):
    await bot.send_message(message.from_user.id, text="Жемге арналған дробилка түрлері🌾", reply_markup=inline_universal)

@dp.message_handler(commands=['next'])
async def E(message: types.Message):
    await bot.send_message(message.from_user.id, text="Қай салада дробилкаларды⚙️ қолданғыңыз келеді таңдаңыз😉", reply_markup=inline_drobilka)


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    m = message.text
    if(m == "Kz-kz"):
        await bot.send_message(message.from_user.id, text=text_kz, reply_markup=inline_drobilka)
    elif(m == "Ru-ru"):
        await bot.send_message(message.from_user.id, text=text_ru)
    elif(m == "mal"):
        await bot.send_message(message.from_user.id, text="Сізге дробилканың қандай түрі керек?", reply_markup=inline_chose)
    elif (m == "electrical"):
        await bot.send_message(message.from_user.id, text="Сізге дробилканың қандай түрі керек?",
                               reply_markup=inline_electrical)
    else:
        await bot.send_message(message.from_user.id, text=text_else)

# Трактор
@dp.callback_query_handler(text = 'zhem_1500')
@dp.callback_query_handler(text = 'grass_2500')

@dp.callback_query_handler(text = 'zhem_2000')
@dp.callback_query_handler(text = 'grass_3000')

@dp.callback_query_handler(text = 'zhem_2500')
@dp.callback_query_handler(text = 'grass_4000')

@dp.callback_query_handler(text = 'zhem_3000')
@dp.callback_query_handler(text = 'grass_5000')
# end

#Universal
@dp.callback_query_handler(text = 'uni_zh11')
@dp.callback_query_handler(text = 'uni_zh15')
@dp.callback_query_handler(text = 'uni_zh18_5')
@dp.callback_query_handler(text = 'uni_zh22')
#end

@dp.callback_query_handler(text = 'mall')
@dp.callback_query_handler(text = 'zhemm')
@dp.callback_query_handler(text = 'elec')
@dp.callback_query_handler(text = 'trucks')
# electrical device
@dp.callback_query_handler(text = 'zhem3')
@dp.callback_query_handler(text = 'grass3')
@dp.callback_query_handler(text = 'zhem4')
@dp.callback_query_handler(text = 'grass4')
@dp.callback_query_handler(text = 'zhem5_5')
@dp.callback_query_handler(text = 'grass5_5')
@dp.callback_query_handler(text = 'zhem7_5')
@dp.callback_query_handler(text = 'grass7_5')
@dp.callback_query_handler(text = 'zhem11')
@dp.callback_query_handler(text = 'grass11')
@dp.callback_query_handler(text = 'zhem15')
@dp.callback_query_handler(text = 'grass15')
@dp.callback_query_handler(text = 'zhem18_5')
@dp.callback_query_handler(text = 'grass18_5')
@dp.callback_query_handler(text = 'zhem22')
@dp.callback_query_handler(text = 'grass22')
#end
async def proccess(call: types.CallbackQuery):
    data = call.data
    global send_data
    #truck
    if(data == "zhem_1500"):

        text = "Трактормен🚜  жұмыс жасайтын қуаты 1500кг/сағ жемге🌾 арналҒан дробилка.\n200 бас ірі қараға арналған🐄\n Бағасы: 500 000тг💰. Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ЖЕМ тартатын дробилка қуаты 1500кг/сағ"
    elif(data == "grass_2500"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 2500кг/сағ шөпке🌾 арналҒан дробилка.\n400 бас ірі қараға арналған🐄\n Бағасы: 500 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ШӨП тартатын дробилка қуаты 2500кг/сағ"
    elif(data == "zhem_2000"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 2000кг/сағ жемге🌾 арналҒан дробилка.\n400 бас ірі қараға арналған🐄\n Бағасы: 650 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ЖЕМ тартатын дробилка қуаты 2000кг/сағ"
    elif (data == "grass_3000"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 3000кг/сағ шөпке🌾 арналҒан дробилка.\n400 бас ірі қараға арналған🐄\n Бағасы: 650 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ШӨП тартатын дробилка қуаты 3000кг/сағ"
    elif (data == "zhem_2500"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 2500кг/сағ жемге🌾 арналҒан дробилка.\n700 бас ірі қараға арналған🐄\n Бағасы: 750 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ЖЕМ тартатын дробилка қуаты 2500кг/сағ"
    elif (data == "grass_4000"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 4000кг/сағ шөпке🌾 арналҒан дробилка.\n700 бас ірі қараға арналған🐄\n Бағасы: 750 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ШӨП тартатын дробилка қуаты 4000кг/сағ"
    elif (data == "zhem_3000"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 3000кг/сағ жемге🌾 арналҒан дробилка.\n1000 бас ірі қараға арналған🐄\n Бағасы: 900 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ЖЕМ тартатын дробилка қуаты 3000кг/сағ"
    elif (data == "grass_5000"):

        text = "Трактормен🚜 жұмыс жасайтын қуаты 5000кг/сағ шөпке🌾 арналҒан дробилка.\n1000 бас ірі қараға арналған🐄\n Бағасы: 900 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Тракторға🚜 арналған ШӨП тартатын дробилка қуаты 5000кг/сағ"
    #end

    #Жем саудасы үшін
    elif(data == "uni_zh11"):
        text = "Қуаты 11КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 1500сағ/кг жем🌾 турай алады.\n Бағасы: 550 000тг💰. \nСізге қауіпсіздік үшін моторды күйдірмейтін (защита⚡🔌 фазаны) құрылғыны ұсынамыз толығырақ білу үшін оператордың қоңырауын📞 күтіңіз\n күтіңіз\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жем саудасына, қуаты 11квт"
    elif (data == "uni_zh15"):
        text = "Қуаты 15КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 2000сағ/кг жем🌾 турай алады.\n Бағасы: 800 000тг💰.\nСізге қауіпсіздік үшін моторды күйдірмейтін (защита⚡🔌 фазаны) құрылғыны ұсынамыз толығырақ білу үшін оператордың қоңырауын📞 күтіңіз\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жем саудасына, қуаты 15квт"
    elif (data == "uni_zh18_5"):
        text = "Қуаты 18.5КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 2500сағ/кг жем🌾 турай алады.\n Бағасы: 1 100 000тг💰.\nСізге қауіпсіздік үшін моторды күйдірмейтін (защита⚡🔌 фазаны) құрылғыны ұсынамыз толығырақ білу үшін оператордың қоңырауын📞 күтіңіз\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жем саудасына, қуаты 18.5квт"
    elif (data == "uni_zh22"):
        text = "Қуаты 22КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾   арналған универсал дробилка, 3000сағ/кг жем🌾 турай алады.\n Бағасы: 1 350 000тг💰.\nСізге қауіпсіздік үшін моторды күйдірмейтін (защита⚡🔌 фазаны) құрылғыны ұсынамыз толығырақ білу үшін оператордың қоңырауын📞 күтіңіз\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жем саудасына, қуаты 22квт"
    #end

    elif(data == "zhem3"):
        text = "Қуаты 3КВт-тық 220Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 250сағ/кг жем турай алады.\n25 бас ірі қараға арналған🐄\n Бағасы: 190 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 3КВт"
    elif(data == "grass3"):
        text = "Қуаты 3КВт-тық 220Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 400сағ/кг жем турай алады.\n 25 бас ірі қараға арналған🐄\n Бағасы: 190 000тг💰.Тапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 3КВт"
    elif(data == "zhem4"):
        text = "Қуаты 4КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 500сағ/кг жем турай алады.\n25 бас ірі қараға арналған🐄\n Бағасы: 300 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 4КВт"
    elif(data == "grass4"):
        text = "Қуаты 4КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 1000сағ/кг жем турай алады.\n25 бас ірі қараға арналған🐄\n Бағасы: 300 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞 күтіңіз\n Тапсырыс беру үшін /zakaz түймесін басыңыз"
    elif (data == "zhem5_5"):
        text = "Қуаты 5.5КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 700сағ/кг жем турай алады.\n60 бас ірі қараға арналған🐄\n Бағасы: 350 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 5.5КВт"
    elif (data == "grass5_5"):
        text = "Қуаты 5.5КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 1200сағ/кг жем турай алады.\n60 бас ірі қараға арналған🐄\n Бағасы: 350 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 5.5КВт"
    elif (data == "zhem7_5"):
        text = "Қуаты 7.5КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 1000сағ/кг жем турай алады.\n120 бас ірі қараға арналған🐄\n Бағасы: 400 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 7.5КВт"
    elif (data == "grass7_5"):
        text = "Қуаты 7.5КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 1700сағ/кг жем турай алады.\n120 бас ірі қараға арналған🐄\n Бағасы: 400 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 7.5КВт"
    elif (data == "zhem11"):
        text = "Қуаты 11КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 1500сағ/кг жем турай алады.\n200 бас ірі қараға арналған🐄\n Бағасы: 550 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 11КВт"
    elif (data == "grass11"):
        text = "Қуаты 11КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 1500сағ/кг жем турай алады.\n200 бас ірі қараға арналған🐄\n Бағасы: 550 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 11КВт"
    elif (data == "zhem15"):
        text = "Қуаты 15КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 2000сағ/кг жем турай алады.\n400 бас ірі қараға арналған🐄\n Бағасы: 800 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 15КВт"
    elif (data == "grass15"):
        text = "Қуаты 15КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 3000сағ/кг жем турай алады.\n400 бас ірі қараға арналған🐄\n Бағасы: 800 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 15КВт"
    elif (data == "zhem18_5"):
        text = "Қуаты 18.5КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 2500сағ/кг жем турай алады.\n700 бас ірі қараға арналған🐄\n Бағасы: 1 100 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Жемге арналған дробилка 18.5КВт"
    elif (data == "grass18_5"):
        text = "Қуаты 18.5КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 4000сағ/кг жем турай алады.\n700 бас ірі қараға арналған🐄\n Бағасы: 1 100 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 18.5КВт"
    elif (data == "zhem22"):
        text = "Қуаты 22КВт-тық 380Вольтта🔌 жұмыс жасайтын жемге 🌾 арналған дробилка, 3000сағ/кг жем турай алады.\n1200 бас ірі қараға арналған🐄\n Бағасы: 1 350 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз "
        about = "Жемге арналған дробилка 22КВт"
    elif (data == "grass22"):
        text = "Қуаты 22КВт-тық 380Вольтта🔌 жұмыс жасайтын шөпке 🌿 арналған дробилка, 5000сағ/кг жем турай алады.\n1200 бас ірі қараға арналған🐄\n Бағасы: 1 350 000тг💰.\nСізге қауіпсіздік үшін защита⚡🔌 фазасын ұсынамыз толығырақ білу үшін оператордың қоңырауын📞\nТапсырыс беру үшін /zakaz түймесін басыңыз"
        about = "Шөпке арналған дробилка 22КВт"
    elif (data == "elec"):
        text = "Электрикалық 🔌 дробилкаларды таңдау үшін /E түймесін басыңыз! "
    elif (data == "trucks"):
        text = "Тракторға🚜 арналған дробилкаларды таңдау үшін /T түймесін басыңыз! "

    elif (data == "mall"):
        text = "Дробилканы электр тоғымен🔌 немесе трактор🚜 соқасымен  /con түймесін басыңыз"
        #text_other = "Дробилканы электр тоғымен🔌 немесе трактор🚜 соқасымен  /con түймесін басыңыз"
        #await bot.send_message(call.from_user.id, text=text_other)
    elif(data == "zhemm"):
        text = "Жемге арналған дробилкалар түрлерін көру үшін /universal түймесін басыңыз "
    else:
        text = "тауарды кнопкалардан таңдаңыз, выберите консоль с помощью кнопок"
    #global send_data
    await bot.send_message(call.from_user.id, text=text)
    #global send_data

    try:
        send_data = about
    except UnboundLocalError:
        print("Қателік!")

