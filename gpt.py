from openai import OpenAI
from aiogram import Bot, Dispatcher, types, executor
import requests
from PIL import Image
import os
previousresponse = ""
messages = []

bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
client = OpenAI(api_key='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')


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('''Welcome to Badbot.AI🇰🇭, a powerful AI assistant built on the GPT-3.5 turbo platform. I'm here to help you with any questions or tasks you have. Feel free to ask me anything!''')


@dp.message_handler(commands=['clean',])
async def welcome(message: types.Message):
    await message.reply('''Bot Cleaned!! 🧹''')


@dp.message_handler(commands=['img',])
async def image(message: types.Message):
    promp = message.text
    word_to_remove = "/img"
    words = promp.split()
    filtered_words = [word for word in words if word != word_to_remove]
    new_promp = " ".join(filtered_words)
    await message.answer_chat_action("typing")
    await message.reply('Bot is generating : '+new_promp.strip())
    response = client.images.generate(
        model="dall-e-3",
        prompt=new_promp.strip(),
        size="1792x1024",
        quality="hd",
        n=1,)
    image_url = response.data[0].url
    img_path = "./img/"+new_promp.strip()+".png"
    img = Image.open(requests.get(image_url, stream=True).raw)
    img.save(img_path)
    source = open(img_path, "rb")
    await message.answer_chat_action("upload_photo")
    await bot.send_document(message.chat.id, document=source)
    os.remove(img_path)


@dp.message_handler()
async def chat(message: types.Message):

    try:
        global previousresponse
        global messages
        if message.reply_to_message is None:
            await message.answer_chat_action("typing")
            messages = []
            chat_text = message.text
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chat_text}
            ]
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages)
            previousresponse = completion.choices[0].message.content
        else:
            await message.answer_chat_action("typing")
            chat_text = message.text
            messages.append({"role": "user", "content": chat_text})
            messages.append({"role": "assistant", "content": previousresponse})
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages)
        await message.answer_chat_action("typing")
        response = completion.choices[0].message.content
        await message.reply(response)
    except Exception as e:
        print(e)


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Service Started 🟢")
    executor.start_polling(dp)
