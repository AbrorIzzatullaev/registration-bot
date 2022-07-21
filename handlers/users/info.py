from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, bot
from states.data import datas
from keyboards.default.key import tests, anketa, xabar
from aiogram.types import Message , ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from filters import IsGroup
sett = {1983515720}

 

@dp.message_handler(text="Ro'yxatdan_o'tish")
async def royxat(message: types.Message):
    if message.from_user.id not in sett:
        sett.add(message.from_user.id)
        await message.answer("To'liq ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
        await datas.fullname.set()
    else:
        await message.answer("Siz ro'yxatdan o'tib bo'lgansiz")    

@dp.message_handler(state = datas.fullname) 
async def fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"fullname": fullname}
    )
    
    await message.answer('Yoshingizni kiriting')
    await datas.next()

@dp.message_handler(state = datas.old)
async def old(message: types.Message, state: FSMContext):
    old = message.text
    await state.update_data({"old": old})
    
    await message.answer('Ingliz  tilini bilish darajangiz qanday')
    await datas.next()

@dp.message_handler(state = datas.language)
async def language(message: types.Message, state: FSMContext):
    language = message.text
    await state.update_data(
        {"language": language}
    )       
    await message.answer("Shaxsiy kompyuteringiz bormi(Ha/Yo'q)")
    await datas.next()


@dp.message_handler(state = datas.pc)
async def pc(message: types.Message, state: FSMContext):
    pc = message.text
    await state.update_data(
        {"pc": pc}
    )       
    await message.answer("Matematika bilish darajangiz qanday")
    await datas.next()


@dp.message_handler(state = datas.math)
async def math(message: types.Message, state: FSMContext):
    math = message.text
    await state.update_data(
        {"math": math}
    )   
    await message.answer("Telefon raqamingizni kiriting")
    await datas.next()


@dp.message_handler(state = datas.phone)
async def phone(message: types.Message, state: FSMContext):
    phone  = message.text 
    await state.update_data(
        {"phone": phone}
    )   
    data = await state.get_data()
    fullname = data.get('fullname')
    old = data.get("old")
    language = data.get('language')
    pc = data.get("pc")
    math = data.get("math")
    phone = data.get('phone')
    msg = "Yangi o'quvchi\n"
    msg+=f"Ismi: {fullname}\n"
    msg+=f"Yoshi: {old}\n"
    msg+=f"English: {language}\n"
    msg+=f"PC: {pc}\n"
    msg+=f"Math: {math}\n"
    msg+=f"Phone Number: {phone}"
    await message.answer(f"Siz kiritgan malumotlar to'g'rimi:\n\n{msg}", reply_markup = tests)
    await datas.next()

@dp.message_handler(state = datas.test)
async def phone(message: types.Message, state: FSMContext):
    if message.text=="Ha":
        data = await state.get_data()
        fullname = data.get('fullname')
        old = data.get("old")
        language = data.get('language')
        pc = data.get("pc")
        math = data.get("math")
        phone = data.get('phone')
        g = "Yangi o'quvchi\n\n"
        g+=f"Profile: {message.from_user.get_mention(as_html=True)}\n"
        g+=f"Ismi: {fullname}\n"
        g+=f"Yoshi: {old}\n"
        g+=f"English: {language}\n"
        g+=f"PC: {pc}\n"
        g+=f"Math: {math}\n"
        g+=f"Phone Number: {phone}"
        await message.answer("Siz bilan tez orada bog'lanamiz", reply_markup = anketa)
        await bot.send_message(chat_id = "@qwertyjhgfdsdfdgg", text = f"{g}")
        await bot.send_message(chat_id = ADMINS[0], text = f"{g}")
        sett.add(message.from_user.id)
        await state.finish()    
    else:
        await message.answer('Qayta boshlashingiz mumkin', reply_markup=anketa)
        await state.finish()


@dp.message_handler(text = "Admin_aloqa")
async def aloqa(message: types.Message, state: FSMContext):
    await datas.call.set()
    await message.answer("Admin ga xabar yo'llashingiz mumkin", reply_markup = xabar )
    


@dp.message_handler(state = datas.call)   
async def is_forwarded(message: types.Message,  state: FSMContext):
    if message.text == "Stop chat":
        await state.finish()
        await message.answer("Savollarga tez orada javob berishadi", reply_markup = anketa)
    else:
        await bot.forward_message(from_chat_id = message.from_user.id, chat_id = ADMINS[0], message_id=message.message_id)  
    




@dp.message_handler(Text(contains="#message", ignore_case=True), user_id=ADMINS[0])
async def dafsd(message: types.Message):
    for i in sett:
        await bot.send_message(chat_id = i, text = f"{message.text}")
        


@dp.message_handler(chat_id = ADMINS[0])
async def forward(message: types.Message):
    await bot.send_message(message.reply_to_message.forward_from.id, text = message.text)        