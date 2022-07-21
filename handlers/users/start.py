from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.data import datas
from data.config import ADMINS
from keyboards.default.key import anketa
from loader import dp, bot
count = {1201187905, 1983515720}


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id not in count:
        notification = f"{message.from_user.get_mention(as_html=True)} bazaga qo'shildi..."
        await bot.send_message(chat_id=ADMINS[0], text=notification)
        count.add(message.from_user.id)
    else:
        pass            
    await message.answer(f"Xush kelibsiz {message.from_user.full_name}!", reply_markup=anketa)
    
@dp.message_handler(commands = "count", chat_id = ADMINS[0])
async def members(message: types.Message):
    await message.answer(len(count))