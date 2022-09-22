import nest_asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import MessageHandler
from telegram.ext import filters
from bot import bot

nest_asyncio.apply()

try:
    with open('token/secret_file.txt', 'r') as file:
        TOKEN = file.read()
except:
    print('Это код для загрузки файла с секретным токеном спикера.\n'
          'Для работы с вашим ботом вставьте, пожалуйста, свой токен')


async def reply(update : Update, context):
    user_text = update.message.text
    answer = bot(user_text)
    await update.message.reply_text(answer)


app = ApplicationBuilder().token(TOKEN).build()

handler = MessageHandler(filters.Text(), reply)

app.add_handler(handler)

app.run_polling()