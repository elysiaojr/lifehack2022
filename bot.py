from calendar import timegm
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Update, Bot
from telegram.ext import ApplicationBuilder, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters, CallbackContext
import requests
import os
from dotenv import load_dotenv
import json
from menu import Menu
from constants import *

load_dotenv()

# ConversationHandler functions [START]

# Constants
LOCATION, BENEFICIARY, TIMING, FRIENDS, OTHERINFO = range(5)

# Get all the user inputs


async def getUserData(update, context):
    # user = update.message.from_user
    user_info = {
        'username': update.effective_user.first_name,
        'chat_id': update.effective_chat.id,
        'location': 'stub',
        'beneficiary': 'stub',
        'timing': 'stub',
        'friends': 'stub',
        'other_info': 'stub'
    }

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[update.effective_user.first_name] = user_info

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    # CBQ Locations
    await update.callback_query.message.edit_text('Lets go! I have some questions to find the right volunteer opportunity for you.\n\nSelect the area at which you want to volunteer:',
                                                  reply_markup=SELECT_LOCATION_BTNS)

    return LOCATION


async def saveLocation(update, context):
    query = update.callback_query
    await query.answer()
    location = query.data.upper()

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[str(update.effective_user.first_name)]['location'] = location

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    # CBQ Beneficiaries
    await update.callback_query.message.edit_text(
        f'You have selected: {location}\n\nSelect the beneficiaries you are interested to help:',
        reply_markup=SELECT_BENEFICIARIES_BTNS)

    return BENEFICIARY


async def saveBeneficiary(update, context):
    query = update.callback_query
    await query.answer()
    beneficiary = query.data.upper()

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[str(update.effective_user.first_name)]['beneficiary'] = beneficiary

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    # CBQ Timing
    await update.callback_query.message.edit_text(f'You wish to work with {beneficiary}\n\nHow often do you want to volunteer?',
                                                  reply_markup=TIMING_BTNS)

    return TIMING


async def saveTiming(update, context):
    query = update.callback_query
    await query.answer()
    timing = query.data.upper()

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[str(update.effective_user.first_name)]['timing'] = timing

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    # CBQ Friends
    await update.callback_query.message.edit_text(f'You prefer to volunteer {timing}\n\nAre you volunteering with friends?',
                                                  reply_markup=FRIENDS_BTN)

    return FRIENDS


async def saveFriends(update, context):
    query = update.callback_query
    await query.answer()
    friends = query.data.upper()

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    users[str(update.effective_user.first_name)]['friends'] = friends

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    await update.callback_query.message.edit_text(f'You are volunteering {friends}\n\nDo you have any information or skills to help us figure out what suits you? e.g. can you teach music? do you have a car to help for deliveries? are you fluent in dialect? do you prefer physically demanding volunteer work?',
                                                  )

    return OTHERINFO


async def saveOtherInfo(update, _: CallbackContext):
    otherInfo = update.message.text

    with open('users.json', 'r') as user_db:
        users = json.load(user_db)

    location = users[str(update.effective_user.first_name)]['location'].lower()
    beneficiary = users[str(update.effective_user.first_name)
                        ]['beneficiary'].lower()
    timing = users[str(update.effective_user.first_name)]['timing'].lower()
    friends = users[str(update.effective_user.first_name)]['friends'].lower()

    users[str(update.effective_user.first_name)]['other_info'] = otherInfo

    with open('users.json', 'w') as user_db:
        json.dump(users, user_db)

    await update.message.reply_text(
        f'VOLUNTEER REQUEST #1\n👤 {update.effective_user.first_name}\n🧭 {location}\n🤝 {beneficiary}\n📅 {timing}\n\n {update.effective_user.first_name} is volunteering {friends}\n\n{otherInfo}\n\nRecommended beneficiary:\nFood from the Heart\nEvent: Bread delivery 45 min/week')

    await _.bot.send_message(chat_id=-1001770990502,
                             text=f'VOLUNTEER REQUEST #1\n👤{update.effective_user.first_name}\n🧭 {location}\n🤝 {beneficiary}\n📅 {timing}\n\n {update.effective_user.first_name} is volunteering {friends}\n\n{otherInfo}\n\nRecommended beneficiary:\nFood from the Heart\nEvent: Bread delivery 45 min/week')

    return ConversationHandler.END


async def cancel(update, context):
    await update.message.reply_text("Conversation ended")

    return ConversationHandler.END

# ConversationHandler functions [END]


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # ConversationHandler
    user_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(getUserData, pattern='volunteer')],
        states={
            LOCATION: [CallbackQueryHandler(saveLocation)],

            BENEFICIARY: [CallbackQueryHandler(saveBeneficiary)],

            TIMING: [CallbackQueryHandler(saveTiming)],

            FRIENDS: [CallbackQueryHandler(saveFriends)],

            OTHERINFO: [MessageHandler(filters.TEXT, saveOtherInfo)]

        },
        fallbacks=[CommandHandler("cancel", cancel)])

    # hello
    bot.add_handler(CommandHandler("hello", Menu.hello))
    bot.add_handler(CommandHandler("start", Menu.start))
    bot.add_handler(user_handler)

    bot.run_polling()


if __name__ == '__main__':
    main()
