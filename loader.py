from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
bot=Bot(config.token,parse_mode=types.ParseMode.HTML)
storage=MemoryStorage()
dp=Dispatcher(bot,storage=storage)
