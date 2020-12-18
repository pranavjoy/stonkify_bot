from PIL import Image

import string
import requests
import random
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext
import os
import shutil

logger = logging.getLogger(__name__)

BASE_URL = ""

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
print(TOKEN)


def move(src, dest):
    shutil.move(src, dest)


def image_url_generator():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(16))
    image_url = "http://{}/images/{}.jpg".format(BASE_URL, result_str)
    resp = requests.get(image_url)
    if resp.status_code == 200:
        image_url_generator()
    else:
        return image_url, result_str


def merge_two_images(image1_location, image2_location):
    image1 = Image.open(image1_location)
    image2 = Image.open(image2_location)
    image1_size = image1.size
    image2_size = image2.size
    image2.paste(image1, (0, 0), image1)
    image2.show()


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Enter /stonkify <concept> to start generating memes')


def stock_photo(image_name):
    # search for image, download it and return image location
    image_location = "image2.jpeg"
    return (image_location)


def stonkify(update: Update, context: CallbackContext) -> None:
    #Search for the images on stock website merge images and return the merged image
    stonk_base = str(context.args[0])
    image2_location = stock_photo(stonk_base)
    merge_two_images("image1.png", image2_location)
    url, image_id = image_url_generator()
    move(image2_location, "images/" + image_id)
    update.message.reply_photo(url)


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
