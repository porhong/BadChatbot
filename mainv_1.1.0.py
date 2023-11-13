import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, executor


API_KEY = 'AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc'

text = ""

bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
genai.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')


def ai(user_text, c_reply):
    if c_reply == 0:
        response = genai.chat(model='models/chat-bison-001',
                              temperature=0.5, messages=[user_text])
        return response.last
    else:
        reply = input(user_text)
        reply = reply.response(model='models/chat-bison-001',
                               temperature=0.5, messages=[user_text])
        return reply.last


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')


@dp.message_handler()
async def chat(message: types.Message):
    try:
        global text
        text = message.text
        print(text)
        if message.reply_to_message is None:
            result = ai(text, 0)
        else:
            result = ai(text, 1)

        await message.reply(text=result)

    except:
        pass


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp)
