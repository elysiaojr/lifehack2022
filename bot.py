from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters
import requests
import os
from dotenv import load_dotenv
import json

# from menu import Menu

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def hello(update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

bot = ApplicationBuilder().token(BOT_TOKEN).build()

bot.add_handler(CommandHandler("hello", hello))

# Example Callback
# bot.add_handler(CallbackQueryHandler(Menu.xxx, pattern="xxx"))

bot.run_polling()
