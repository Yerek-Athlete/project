from aiogram.dispatcher.filters.state import StatesGroup, State
from Logger import bot, dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from string import Template
from aiogram.dispatcher import FSMContext

#from main import*
class test(StatesGroup):
    q1 = State() # name of client
    q2 = State() # address
    q3 = State() # telephone number

@dp.message_handler(Command('zakaz'), state=None)
async def start_orders_kz(message: types.Message):
    await message.answer("Есіміңіз?")
    await test.q1.set()

@dp.message_handler(state=test.q1)
async def ques1(message: types.Message, state=FSMContext):
    answer = message.text
    global ans1
    ans1 = answer
    await state.update_data(answer1 = answer)
    await message.answer("Толық мекен🛣 жайыңызды(Обылыс, Қала/аудан, ауыл, көше)?")
    await test.next()

@dp.message_handler(state=test.q2)
async def ques2(message: types.Message, state=FSMContext):
    answer = message.text
    global ans2
    ans2 = answer
    await state.update_data(answer2 = answer)
    await message.answer("Телефон номеріңіз📱?")
    await test.next()

@dp.message_handler(state=test.q3)
async def ques3(message: types.Message, state=FSMContext):
    from main import send_data
    try:
        answer = int(message.text)
        global ans3
        ans3 = answer
    except ValueError:
        await bot.send_message(message.from_user.id, "Телефон номерңізді сандармен ғана жазыңыз❗️")

    t = Template('Дробилка типі: $type\n Есімі: $name\n Мекен-жайы: $address\n Телефон номері: $num')

    try:
        info = t.substitute(dict(type=send_data, name=ans1, address=ans2, num=ans3))
    except NameError:
        print("қателік!")

    await state.update_data(answer4 = answer)
    data = await state.get_data()
    await bot.send_message(chat_id='@zakaz_drobilka', text=info)
    await bot.send_message(message.from_user.id, "Тапсырыс бергенңізге рақмет👍🏻, тапсырысты растау үшін 4_Сала директоры Дәурен🤵🏽 мырза сізге  хабарласады!")
    await state.finish()


