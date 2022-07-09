from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#[InlineKeyboardButton('', callback_data='')]

# inline keyboard for what can the bot help u with today
BOT_START_BTNS = InlineKeyboardMarkup(
    [[InlineKeyboardButton('I want to volunteer', callback_data='volunteer')],
     [InlineKeyboardButton('About', callback_data='about')]])

# IK for different locations
SELECT_LOCATION_BTNS = InlineKeyboardMarkup(
    [[InlineKeyboardButton('NUS', callback_data='nus')],
     [InlineKeyboardButton('SMU', callback_data='smu')],
     [InlineKeyboardButton('NTU', callback_data='ntu')],
     [InlineKeyboardButton('SUTD', callback_data='sutd')],
     [InlineKeyboardButton('SIT', callback_data='sit')],
     [InlineKeyboardButton('North', callback_data='north')],
     [InlineKeyboardButton('South', callback_data='south')],
     [InlineKeyboardButton('Central', callback_data='central')],
     [InlineKeyboardButton('East', callback_data='east')],
     [InlineKeyboardButton('West', callback_data='west')]])

# IK for benefeciaries
SELECT_BENEFICIARIES_BTNS = InlineKeyboardMarkup(
    [[InlineKeyboardButton('elderly', callback_data='elderly')],
     [InlineKeyboardButton('children', callback_data='children')],
     [InlineKeyboardButton('patients (with severe illness)', callback_data='patients')],
     [InlineKeyboardButton('low-income group', callback_data='low income')],
     [InlineKeyboardButton('foreign domestic workers', callback_data='foreign domestic workers')],
     [InlineKeyboardButton('no preference', callback_data='no preference')]])

# IK for timing
TIMING_BTNS = InlineKeyboardMarkup(
    [[InlineKeyboardButton('weekly', callback_data='weekly')],
     [InlineKeyboardButton('monthly', callback_data='monthly')],
     [InlineKeyboardButton('a few times yearly', callback_data='few times a year')]])

# IK for friends
FRIENDS_BTN = InlineKeyboardMarkup(
    [[InlineKeyboardButton('i am volunteering alone', callback_data='alone')],
     [InlineKeyboardButton('i am volunteering in a group', callback_data='with a group')],
     [InlineKeyboardButton('i am looking for fellow volunteers', callback_data='with new friends')]])
