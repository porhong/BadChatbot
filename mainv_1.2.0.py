import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, executor


API_KEY = 'AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc'

old_msg = []

bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
genai.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')


response = ""


def start_chat(text, type):
    global response
    if type == 1:
        response = genai.chat(
            model='models/chat-bison-001', temperature=0.50, top_p=0.95, top_k=40, messages=[text])
        return response.last
    else:
        response = response.reply(text)
        return response.last


@dp.message_handler()
async def chat(message: types.Message):
    try:
        text = message.text
        if message.reply_to_message is None:
            answer = start_chat(text, 1)
            await message.reply(answer)
        else:
            answer = start_chat(text, 2)
            await message.reply(answer)
    except Exception as e:
        print(e)


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp)
