from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

anketa = ReplyKeyboardMarkup(

	keyboard = [
		[
			KeyboardButton(text="Ro'yxatdan_o'tish"),
			KeyboardButton(text="Admin_aloqa"),
		],
	],
	resize_keyboard=True
)

tests = ReplyKeyboardMarkup(

	keyboard = [
		[
			KeyboardButton(text="Ha"),
			KeyboardButton(text="Yo'q"),
		],			
	],
	resize_keyboard=True
)

xabar = ReplyKeyboardMarkup(

	keyboard = [

		[
			KeyboardButton(text="Stop chat")	
		],

	],
	resize_keyboard=True
)