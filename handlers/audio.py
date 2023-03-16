# from aiogram.dispatcher.filters import Command
# from aiogram.types import Message
# import pyttsx3
# from aiogram.types.base import InputFile
# from gtts import gTTS
# from loader import dp,bot
# from time import sleep
# from .photo import handle_docs_photo
# @dp.message_handler(Command('start'))
# async def audio(message:Message):
#
#     await message.answer('textni kiriting')
# @dp.message_handler()
# async def auido2(message:Message):
#     engine = pyttsx3.init()
#     text =handle_docs_photo
#
#     engine.say(text)
#     print(text)
#     tts = gTTS(text=text, lang='ru')
#     tts.save('file.mp3')
#     await bot.send_audio(message.from_user.id, open('file.mp3', 'rb'))

