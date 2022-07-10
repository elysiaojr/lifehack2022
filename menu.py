# from constants import *
import time
import telegram
from constants import *
from telegram import Update
from telegram.ext import CallbackContext
import json

class Menu:
    def __init__(self):
        pass

    # hello
    async def hello(update, context):
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')


    # Start - what can the bot help you with today
    async def start(update, context):
        await update.message.reply_text(f'Hello {update.effective_user.first_name}, welcome to VolunteerBot! Using this bot, you can find volunteering opportunities based on your own criteria, find like-minded friends to volunteer together, and share awesome opportunities with others.')
        # await update.message.reply_text('Join our bot channel at :')
        await update.message.reply_text('What can volunteerBot help you with today?', 
            reply_markup=BOT_START_BTNS)