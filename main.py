import google.generativeai as palm
import asyncio
from aiogram import Bot, Dispatcher, types, executor

API_KEY = 'AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc'



bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')

@dp.message_handler()
async def a(message: types.Message):
    try:
        msg = message.reply_to_message.text # if replied
        palm.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')
        response = palm.reply(messages=[msg])
        print (response.last)
        await message.reply(text= response.last)

    except:
        text = message.text
        palm.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')
        response = palm.chat(messages=[text])
        print (response.last)
        await message.reply(text= response.last)
       

  
async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
  executor.start_polling(dp)
