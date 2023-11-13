from openai import OpenAI
import openai
from aiogram import Bot, Dispatcher, types, executor


previousresponse = ""
messages = []

bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
client = OpenAI(api_key='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')
openai.api_key = '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'


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')


@dp.message_handler()
async def chat(message: types.Message):

    try:
        global previousresponse
        global messages
        if message.reply_to_message is None:
            chat_text = message.text
            assistant = client.beta.assistants.create(
                name="Math Tutor",
                instructions="You are a personal math tutor. Write and run code to answer math questions.",
                tools=[{"type": "code_interpreter"}],
                model="gpt-4-1106-preview")
            thread = client.beta.threads.create()
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=chat_text)
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id,
                instructions="Please address the user as Jane Doe. The user has a premium account.")
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id)
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )

            previousresponse = completion.choices[0].message.content
        else:
            chat_text = message.text
            messages.append({"role": "user", "content": chat_text})
            messages.append({"role": "assistant", "content": previousresponse})
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=messages)

        # response = completion.choices[0].message.content
        await message.reply(messages)
    except:
        pass


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp)
