TOKEN = '7162755689:AAFprDuPUcVsADb6rfkZk9CVhcF4Cw2tGc8'

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update

async def start(update, context):
    await update.message.reply_text("Please enter your height in cm:")

async def handle_height(update, context):
    height_input = update.message.text
    try:
        height = int(height_input)
        weight = height - 100
        await update.message.reply_text(f"Your predicted weight is {weight} kg.")
    except ValueError:
        await update.message.reply_text("Please enter a valid height in cm.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_height))

app.run_polling()

