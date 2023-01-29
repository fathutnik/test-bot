from telegram import *
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import datetime, time

t = {}
utc = time.timezone/3600

async def start(update: Update, context: CallbackContext):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='./IMG_7374.jpg', caption=time + " UTC: " + str(utc))
    message = update.message
    t["@" + str(message.chat.username)] = time
    print(t)


if __name__ == '__main__':
    application = ApplicationBuilder().token('6160247743:AAGaMTnk5hVCgq5lGiU2cYFs_h0WkyZKCHY').build()

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)

    application.run_polling()

