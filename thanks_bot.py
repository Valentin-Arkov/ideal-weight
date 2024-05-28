from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define the command handler for start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me anything and I will acknowledge it.')

# Define a message handler
def handle_text(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Thank you.')

# Main function to handle the bot
def main():

    token = '...'
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Start command
    dp.add_handler(CommandHandler("start", start))

    # Text message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

