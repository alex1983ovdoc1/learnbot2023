from glob import glob
import logging
from random import choice

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler

from utils_bot import get_keyboard, get_user_emo
import a9_calculator

# command /start1	
def greet_user(bot, update, user_data):	
	emo = get_user_emo(user_data)
	# emo = emojize(choice(settings0.USER_EMOJI))	
	user_data['emo'] = emo
	text = ' Hello {} (user clicked/start0)'.format(emo)
	print(text)
	
	update.message.reply_text(text, reply_markup=get_keyboard())
	text0 = 'User /{}/: "{}"'.format(update.message.chat.first_name, text)
	logging.info(text0)



# send text user 
def talk_to_me(bot, update, user_data):
	user_text = update.message.text

	if user_text[:5] == 'calc:':
		string_r = user_text[5:]
		result_r = a9_calculator.calculator(string_r)
		print(result_r)
		bot.send_message(chat_id=update.message.chat.id, text = f'Your result: {result_r}', reply_markup = get_keyboard())		
	
	else:
		user_text = 'User {}*{} sended: "{}"'.\
		format(update.message.chat.first_name, user_data['emo'], update.message.text)
		# print(update.message)
		# print()
		print(user_text)
		update.message.reply_text(user_text, reply_markup=get_keyboard())
		# logging.info(user_text)
		logging.info("User: %s, Chat id: %s, Message: %s",
			update.message.chat.first_name, update.message.chat.id,
			update.message.text)


# send photo to user
def send_cat_picture(bot, update, user_data):
	cat_list = glob('images/cat*.jp*g')
	cat_pic = choice(cat_list)
	print(cat_pic)
	bot.send_photo(chat_id=update.message.chat.id,
	 photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())


# change avatar
def change_avatar(bot, update, user_data):
	if 'emo' in user_data:
		del user_data['emo']
	emo = get_user_emo(user_data)
	update.message.reply_text('Ready: {}'.format(emo), reply_markup=get_keyboard())


# users contacts
def get_contact(bot, update, user_data):
	print(update.message.contact)
	update.message.reply_text('Ready! {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())


# users location
def get_location(bot, update, user_data):
	print(update.message.location)
	update.message.reply_text('Ready! {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

# start calculator
def start_calculater(bot, update, user_data):
	calc_text = ('Plese enter (calc: 2 + 2 * 6....): ')
	print(calc_text)
	update.message.reply_text(calc_text, reply_markup=get_keyboard())


# Strart bot
def start_bot(bot, update, user_data):
	update.message.reply_text('/start0', reply_markup=get_keyboard())
	# print(update.message)
	# print()


# Start form
def anketa_start(bot, update, user_data):
	update.message.reply_text("What's your name? Please write your first_name and last_name", reply_markup=ReplyKeyboardRemove())
	return "name"


# first step form
def anketa_get_name(bot, update, user_data):
	user_name = update.message.text
	if len(user_name.split(" ")) != 2:
		update.message.reply_text("Please enter your first and last name:")
		return "name"
	else:
		user_data['anketa_name'] = user_name
		reply_keyboard = [["1", "2", "3", "4", "5"]]

		update.message.reply_text(
			"Rate our BOT from 1 to 5:",
			reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
			)
		return "rating"

# next step form
def anketa_rating(bot, update, user_data):
	user_data['anketa_rating'] = update.message.text
	update.message.reply_text("""Please write a review\
		or /skip for go next step""")
	return "comment"

# print comment
def anketa_comment(bot, update, user_data):
	user_data['anketa_comment'] = update.message.text
	text = """
	<b>Last name, Name:</b> {anketa_name}
	<b>Rating:</b> {anketa_rating}
	<b>Comment:</b> {anketa_comment}""".format(**user_data)
	update.message.reply_text(text, reply_markup=get_keyboard(), parse_mode=ParseMode.HTML)
	return ConversationHandler.END

# skip comment
def anketa_skip_comment(bot, update, user_data):
	user_data['anketa_comment'] = update.message.text
	text = """
	<b>Last name, Name:</b> {anketa_name}
	<b>Rating:</b> {anketa_rating}""".format(**user_data)
	update.message.reply_text(text, reply_markup=get_keyboard(), parse_mode=ParseMode.HTML)
	return ConversationHandler.END

# print don't know if rating != int()
def dontknow(bot, update, user_data):
	update.message.reply_text("Sorry, I don't undestandin you...", reply_markup=get_keyboard())
	return ConversationHandler.END

