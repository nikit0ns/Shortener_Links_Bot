from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import config
import bitly_api


bot = Bot(token = config.TOKEN) #Ваш токен 
dp = Dispatcher()
connection = bitly_api.Connection(access_token = config.Access_Token) #Токен Bitly


@dp.message(Command(commands = ['start']))
async def cmd_start(message: types.Message):
    await message.answer('👋 <b>Привіт, я Скорочувач URL.</b> \n✂️ <b>Я зможу скорочувати ваші посилання.</b> \n🔗 <b>Надішліть посилання, яке хочете скоротити.</b>', parse_mode = 'HTML')


@dp.message(Command(commands = ['help']))
async def cmd_help(message: types.Message):
    await message.answer("⁉️<b> Якщо у вас є проблеми.</b> \n✉️ <b>Напишіть мені</b> <a href='https://t.me/nikit0ns'>@nikit0ns</a><b>.</b>", disable_web_page_preview = True, parse_mode = 'HTML')


@dp.message()
async def cmd_short(message: types.Message):
    if message.text.startswith('https://bit.ly/') or message.text.startswith('http://bit.ly/'):
        await message.answer('❗️<b>Це вже скорочене посилання. Надішліть інше посилання.</b>', parse_mode = 'HTML')
    elif message.text.startswith('http://') or message.text.startswith('https://'):
        if ' ' in message.text:
            await message.answer('⚠️<b> URL-адреса повинна починатися з <i>http://</i> або <i>https://</i> і не повинна містити пробілів.</b>', parse_mode = 'HTML')
        else:
            url = message.text
            short_url = connection.shorten(url)
            shortened_url = short_url.get('url')
            await message.answer(f'🔗 <b>Ваше посилання: {message.text}</b> \n✂️ <b>Скорочене посилання: {shortened_url}</b> \n\n📌 <b>Скорочено за допомогою @Shortener_Links_Bot</b>', disable_web_page_preview = True, parse_mode = 'HTML')
    else:
        await message.answer('⚠️<b> URL-адреса повинна починатися з <i>http://</i> або <i>https://</i> і не повинна містити пробілів.</b>', parse_mode = 'HTML')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())