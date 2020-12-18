from PIL import Image

import requests
import random
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

logger = logging.getLogger(__name__)

BASE_URL = "https://hardboiled.tech/"

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
print(TOKEN)


def image_url_generator():
    image_id = random.randint(1000000, 1000000000)
    image_url = "http://" + BASE_URL + "/images/" + str(image_id) + ".jpg"
    resp = requests.get(image_url)

    if resp.status_code == 200:
        image_url_generator()
    else:
        return [image_url, image_id]


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Enter /stonkify <concept> to start generating memes')


def stonkify(update: Update, context: CallbackContext) -> None:
    #Search for the images on stock website merge images and return the merged image

    stonk_base = str(context.args[0])
    print(stonk_base)
    update.message.reply_photo('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg')


def merge_two_images(image1_location, image2_location):
    image1 = Image.open(image1_location)
    image2 = Image.open(image2_location)
    image1_size = image1.size
    image2_size = image2.size
    image2.paste(image1, (0, 0), image1)
    image2.show()


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("stonkify", stonkify))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()