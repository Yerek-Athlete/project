from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from Logger import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup

@dp.message_handler(commands=['taps'])
async def kz(message: types.Message):
    await bot.send_message(message.from_user.id, text="Для какого целью вам нужен дробилка", reply_markup=inline_drobilka_ru)

@dp.message_handler(commands=['corm'])
async def kz(message: types.Message):
    await bot.send_message(message.from_user.id, text="Выберите тип измельчителя кормов", reply_markup=inline_corm)

@dp.message_handler(commands=['divide'])
async def kz(message: types.Message):
    await bot.send_message(message.from_user.id, text="🔌/🚜", reply_markup=inline_divide)

@dp.message_handler(commands=['elec'])
async def kz(message: types.Message):
    await bot.send_message(message.from_user.id, text="У нас есть много типов электрических дробилок. Выбирайте по мощности!", reply_markup=inline_elec)


#choose
inline_drobilka_ru = InlineKeyboardMarkup()
inline_zhem = InlineKeyboardButton("торговля кормами🌾", callback_data='zh')
inline_mal = InlineKeyboardButton("домашний скот🐑", callback_data='mall_ru')
inline_drobilka_ru.insert(inline_zhem)
inline_drobilka_ru.insert(inline_mal)
#end

#corm
inline_corm = InlineKeyboardMarkup()
uni_zhem_shop11 = InlineKeyboardButton("Подача 11кВт при ~ 380 вольт🔌 ", callback_data='uni_zh11')
uni_zhem_shop15 = InlineKeyboardButton("Подача 15кВт при ~ 380 вольт 🔌 ", callback_data='uni_zh15')
uni_zhem_shop18_5 = InlineKeyboardButton("Подача 18.5кВт при ~ 380 вольт🔌 ", callback_data='uni_zh18_5')
uni_zhem_shop22 = InlineKeyboardButton("Подача 22кВт при ~ 380 вольт 🔌", callback_data='uni_zh22')

inline_corm.insert(uni_zhem_shop11)
inline_corm.insert(uni_zhem_shop15)
inline_corm.insert(uni_zhem_shop18_5)
inline_corm.insert(uni_zhem_shop22)
#end

# divide
inline_divide = InlineKeyboardMarkup()
electrical_ru = InlineKeyboardButton("C электрический ток 🔌", callback_data='elec')
truck_ru = InlineKeyboardButton("С трактором 🚜", callback_data='trucks')
inline_divide.insert(electrical_ru)
inline_divide.insert(truck_ru)
#

# elec
inline_elec = InlineKeyboardMarkup()
inline_zhem3 = InlineKeyboardButton("Жемге 3КВт-тық ~220В🔌 ", callback_data='zhemru3')
inline_shop3 = InlineKeyboardButton("Шөпке 3КВт-тық ~220В🔌 ", callback_data='grassru3')

inline_zhem4 = InlineKeyboardButton("Жемге 4КВт-тық ~380В🔌 ", callback_data='zhemru4')
inline_shop4 = InlineKeyboardButton("Шөпке 4КВт-тық ~380В🔌 ", callback_data='grassru4')

inline_zhem5_5 = InlineKeyboardButton("Жемге 5.5КВт-тық ~380Вольтта🔌 ", callback_data='zhemru5_5')
inline_shop5_5 = InlineKeyboardButton("Шөпке 5.5КВт-тық ~380Вольтта🔌 ", callback_data='grassru5_5')

inline_zhem7_5 = InlineKeyboardButton("Жемге 7.5КВт-тық ~380Вольтта🔌 ", callback_data='zhemru7_5')
inline_shop7_5 = InlineKeyboardButton("Шөпке 7.5КВт-тық ~380Вольтта🔌 ", callback_data='grassru7_5')

inline_zhem11 = InlineKeyboardButton("Жемге 11КВт-тық ~380Вольтта🔌 ", callback_data='zhemru11')
inline_shop11 = InlineKeyboardButton("Шөпке 11КВт-тық ~380Вольтта🔌 ", callback_data='grassru11')

inline_zhem15 = InlineKeyboardButton("Жемге 15КВт-тық ~380Вольтта🔌 ", callback_data='zhemru15')
inline_shop15 = InlineKeyboardButton("Шөпке 15КВт-тық ~380Вольтта🔌 ", callback_data='grassru15')

inline_zhem18_5 = InlineKeyboardButton("Жемге 18.5КВт-тық ~380Вольтта🔌 ", callback_data='zhemru18_5')
inline_shop18_5 = InlineKeyboardButton("Шөпке 18.5КВт-тық ~380Вольтта🔌 ", callback_data='grassru18_5')

inline_zhem22 = InlineKeyboardButton("Жемге 22КВт-тық ~380Вольтта🔌 ", callback_data='zhemru22')
inline_shop22 = InlineKeyboardButton("Шөпке 22КВт-тық ~380Вольтта🔌 ", callback_data='grassru22')

inline_elec.insert(inline_zhem3)
inline_elec.insert(inline_shop3)
inline_elec.insert(inline_zhem4)
inline_elec.insert(inline_shop4)
inline_elec.insert(inline_zhem5_5)
inline_elec.insert(inline_shop5_5)
inline_elec.insert(inline_zhem7_5)
inline_elec.insert(inline_shop7_5)
inline_elec.insert(inline_zhem11)
inline_elec.insert(inline_shop11)
inline_elec.insert(inline_zhem15)
inline_elec.insert(inline_shop15)
inline_elec.insert(inline_zhem18_5)
inline_elec.insert(inline_shop18_5)
inline_elec.insert(inline_zhem22)
inline_elec.insert(inline_shop22)


#
@dp.callback_query_handler(text = 'zh')
@dp.callback_query_handler(text = 'mall_ru')
@dp.callback_query_handler(text = 'elec')
@dp.callback_query_handler(text = 'trucks')
#
@dp.callback_query_handler(text = 'zhemru3')
@dp.callback_query_handler(text = 'grassru3')
@dp.callback_query_handler(text = 'zhemru4')
@dp.callback_query_handler(text = 'grassru4')
@dp.callback_query_handler(text = 'zhemru5_5')
@dp.callback_query_handler(text = 'grassru5_5')
@dp.callback_query_handler(text = 'zhemru7_5')
@dp.callback_query_handler(text = 'grassru7_5')
@dp.callback_query_handler(text = 'zhemru11')
@dp.callback_query_handler(text = 'grassru11')
@dp.callback_query_handler(text = 'zhemru15')
@dp.callback_query_handler(text = 'grassru15')
@dp.callback_query_handler(text = 'zhemru18_5')
@dp.callback_query_handler(text = 'grassru18_5')
@dp.callback_query_handler(text = 'zhemru22')
@dp.callback_query_handler(text = 'grassru22')
#

async def proccess(call: types.CallbackQuery):
    d = call.data
    # chose
    if(d == 'zh'):
      t = "Нажмите кнопку /corm, чтобы увидеть типы измельчителей кормов."
    elif(d == 'mall_ru'):
        t = "Нажмите на дробилку с помощью электрического плуга 🔌 или трактора /divide."
    elif (d == 'elec'):
        t = "Нажмите кнопку /elec, чтобы выбрать 🔌 электрические дробилки!."


