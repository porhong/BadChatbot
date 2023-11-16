import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, executor


API_KEY = 'AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc'
bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
genai.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')





def start_chat(text, type):
    global response
    if type == 1:
        response = genai.chat(
            model='models/chat-bison-001', temperature=0.50, top_p=0.95, top_k=40, messages=[text])
        if response.last is None:
            answer = "I can not answer for this topic 😥"
        else:
            answer = response.last
        return answer
    elif type == 2:
        response = response.reply(text)
        if response.last is None:
            answer = "I can not answer for this topic 😥"
        else:
            answer = response.last
        return answer


@dp.message_handler()
async def chat(message: types.Message):
    try:
        text = message.text
        if message.reply_to_message is None:
            await message.answer_chat_action("typing")
            answer = start_chat(text, 1)
            await message.answer_chat_action("typing")
            await message.reply(answer)
        else:
            await message.answer_chat_action("typing")
            answer = start_chat(text, 2)
            await message.answer_chat_action("typing")
            await message.reply(answer)
    except Exception as e:
        print(e)
        await message.reply(f"""Error⚠️
Bot was ran into an errot: <b>{e}</b>
Please report this case to administrator.""")


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Service Started🟢")
    executor.start_polling(dp)
