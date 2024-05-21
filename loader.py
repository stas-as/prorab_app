from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from confing import TOKEN


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()