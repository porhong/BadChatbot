import google.generativeai as genai 
from aiogram import Bot, Dispatcher, types, executor


API_KEY = 'AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc'

old_msg = []

bot = Bot(token="6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE")
dp = Dispatcher(bot)
genai.configure(api_key='AIzaSyBcJCFrUHkLrF5ZhjJ_dsGyitgIPvqZlMc')


@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
  await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.AI is an AI chat bot that can help you with a variety of tasks, including playing games, generating creative text formats, answering questions, translating languages, writing creative content, performing mathematical operations, analyzing data, and more. It is still under development, but it is constantly learning and improving.''')


@dp.message_handler(commands = ['clean',])
async def welcome(message: types.Message):
  await message.reply('''Bot Cleaned!! 🧹''')

@dp.message_handler()
async def chat(message: types.Message):
    try:
      global old_msg
      if message.reply_to_message is None:
        
        old_msg=[]
        text = message.text
        old_msg.append(text)
        await message.answer_chat_action("typing")
        response = genai.chat(model='models/chat-bison-001',temperature=0.5,messages=[text])
        await message.answer_chat_action("typing")
        print(response.last)
        if response.last is None:
           await message.reply(text= "I Can not answer for this topic 😥")
        else:
          await message.reply(text= response.last)
      else:
        
        for check in old_msg:
          await message.answer_chat_action("typing")
          response = genai.chat(model='models/chat-bison-001',temperature=0.5,messages=[check])
        old_msg.append(message.text)
        old_msg.reverse()
        reponse = response.reply(old_msg[0])
        old_msg.reverse()
        await message.answer_chat_action("typing")
        print(reponse.last)
        if reponse.last is None:
           await message.reply(text= "I Can not answer for this topic 😥")
        else:
          await message.reply(text= reponse.last)

    except:
        pass

async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
  executor.start_polling(dp)
