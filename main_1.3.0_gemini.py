import google.generativeai as genai
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor

messages = []
load_dotenv()

bot = Bot(token=os.getenv('API_tele'))
dp = Dispatcher(bot)
genai.configure(api_key=os.getenv('API_google'))


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def converstion(text, type):
    global messages
    if type == 1:
        messages = [
            {'role': 'user',
             'parts': [text]}]
        response = model.generate_content(messages, generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=2048,
            temperature=1.0))

        messages.append({'role': 'model',
                         'parts': [response.text]})
        return response.text
    elif type == 2:
        messages.append({'role': 'user',
                         'parts': [text]})
        response = model.generate_content(messages, generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=2048,
            temperature=1.0))
        messages.append({'role': 'model',
                         'parts': [response.text]})
        return response.text


@dp.message_handler(content_types=['photo'])
async def download_image(message: types.Message):
    try:
        file_id = message.photo[-1].file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, destination='D:\Program\Project AI Chat\BadChatbot\img')
        await message.answer_chat_action("typing")
        await message.reply(file_id)
    except Exception as e:
        print(e)


@dp.message_handler()
async def chat(message: types.Message):
    global messages
    try:
        text = message.text
        if message.reply_to_message is None:
            await message.answer_chat_action("typing")
            answer = converstion(text, 1)
            await message.answer_chat_action("typing")
            await message.reply(answer)
        else:
            await message.answer_chat_action("typing")
            answer = converstion(text, 2)
            await message.answer_chat_action("typing")
            await message.reply(answer)
    except Exception as e:
        error_name = type(e).__name__
        print(error_name)
        if error_name == "ValueError":
            messages.pop()
            await message.reply("I can not answer for this promp 😥. Please try again by make it more specific.")
        else:
            await message.reply(f"""Error⚠️
    --------------------------------------------------------
    Bot was ran into an error: <strong>{error_name}</strong>
    --------------------------------------------------------
    We are sorry that make you feel 
    inconvenience due this tool is on Develoment.
    Please report this case to administrator.
    --------------------------------------------------------""", parse_mode="html")


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Service Started🟢")
    executor.start_polling(dp)
