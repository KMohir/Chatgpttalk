
from handlers.from_pic_get_text import main
from handlers.translation import translation, translationuz
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import pyttsx3

from gtts import gTTS
from loader import dp,bot
import openai
openai.api_key = "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"


from keybord.default import button
@dp.message_handler(Command("start"))
async def start(message:Message):
    await message.reply("Kategoriyani tanlang",reply_markup=button)
@dp.message_handler(text="Rasmdagi matnni o'zbek tiliga tarjima qilish")
async def start(message:Message):
    await message.reply("Rasm tashlang")
    @dp.message_handler(content_types=['photo'])
    async def handle_docs_photo(message):

        await message.photo[-1].download('pictranslate/test.jpg')

        a=main()
        t=translation(a[1:-1])
        await message.reply(t)


@dp.message_handler(text="Texni o'zbek tiliga tarjima qilish")
async def start(message:Message):
    await message.reply("Textni tashlang")


    @dp.message_handler()
    async def translate(message:Message):
        text = message.text

        t = translation(text)
        print(t)
        await message.reply(t)

@dp.message_handler(text="Chatgpt bilan suhbatlashish")
async def audio_start(message:Message):
    await message.reply("Textni tashlang")


    @dp.message_handler(content_types='text')
    async def auido(message:Message):
        t=message.text

        text = translation(t)
        print(text)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.text}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        textuz=translationuz(response.choices[0].text)
        engine = pyttsx3.init()


        engine.say(textuz)
        print(textuz)
        tts = gTTS(text=response.choices[0].text, lang='ru')
        tts.save('file.mp3')
        await bot.send_audio(message.from_user.id, open('file.mp3', 'rb'))
