import asyncio
import openai
from aiogram import Bot, Dispatcher, types, executor


bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')

@dp.message_handler()
async def a(message: types.Message):
    if message.text=="Hello":
       await message.reply(text="Welcome")
    else:
      await message.reply(text=message.text)


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
  executor.start_polling(dp)