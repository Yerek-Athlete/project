from aiogram.dispatcher.filters.state import StatesGroup, State
from Logger import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext

class Test(StatesGroup):
    Q1 = State() # name of device
    Q2 = State() # name of client
    Q3 = State() # address
    Q4 = State() # telephone number

@dp.message_handler(Command('zakaz'), state=None)
async def start_order_kz(message: types.Message):
    await message.answer("Қандай дробилкаға тапсырыс бересіз? Мысалы(Жемге, 3КВт)")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def qu1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Есіміңіз")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def qu2(message: types.Message, state=FSMContext):
    answer = message.text
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Қай жерге жеткіземіз(Өтініш толыққанды мекен-жайыңызды жазуыңызды сұраймыз!)")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def qu3(message: types.Message, state=FSMContext):
    answer = message.text
    global ans3
    ans3 = answer
    await state.update_data(answer3 = answer)
    await message.answer("Телефон номеріңіз📱?")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def qu4(message: types.Message, state=FSMContext):
    answer = int(message.text)
    global ans4
    ans4 = answer
    t = Template('Дробилка типі: $type\n Есімі: $name\n Мекен-жайы: $address\n Телефон номері: $num')
    #info = t.substitute(dict(console=type_of_console, name=ans1, number=ans2, address=ans3, payments=ans4))
    info = t.substitute(dict(type=ans1, name=ans2, address=ans3, num=ans4))
    await state.update_data(answer4 = answer)
    data = await state.get_data()
    await bot.send_message(chat_id='@zakaz_drobilka', text=info)
    await bot.send_message(message.from_user.id, "Тапсырыс бергенңізге рақмет👍🏻, тапсырысты растау үшін оператор сізге хабарласады. Төлемді жеткізілген соң төлесеңіз болады🚛😉")
    await state.finish()
