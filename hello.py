TOKEN = '...'

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def hello(update, context):
    await update.message.reply_text('Hello!')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

