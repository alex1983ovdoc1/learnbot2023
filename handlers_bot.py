from glob import glob
import logging
from random import choice

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode, error
from telegram.ext import ConversationHandler
from telegram.ext import messagequeue as mq

from utils_bot import get_keyboard
from db import db, get_or_create_user, get_user_emo, toggle_subscription, get_subscribers
from bot import subscribers
import a9_calculator



# command /start1	
def greet_user(bot, update, user_data):	
	# print(update.message.chat_id)
	# print(update.effective_user)
	# print(update.message)
	user = get_or_create_user(db, update.effective_user, update.message)
	# print(user)
	emo = get_user_emo(db, user)
	text = ' Hello {} (user clicked/start0)'.format(emo)
	print(text)
	
	update.message.reply_text(text, reply_markup=get_keyboard())
	text0 = 'User /{}/: "{}"'.format(user['first_name'], text)
	logging.info(text0)


# send text user 
def talk_to_me(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	emo = get_user_emo(db, user)
	user_text = update.message.text

	if user_text[:5] == 'calc:':		
		string_r = user_text[5:]
		result_r = a9_calculator.calculator(string_r)
		print(result_r)
		bot.send_message(chat_id=user['chat_id'], text = f'Your result: {result_r}', reply_markup = get_keyboard())		
	
	else:
		user_text = 'User {}*{} sended: "{}"'.\
		format(user['first_name'], emo, update.message.text)
		print(user_text)
		update.message.reply_text(user_text, reply_markup=get_keyboard())
		logging.info("User: %s, Chat id: %s, Message: %s",
			user['first_name'], user['chat_id'],
			update.message.text)


# send photo to user
def send_cat_picture(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	cat_list = glob('images/cat*.jp*g')
	cat_pic = choice(cat_list)
	print(cat_pic)
	bot.send_photo(chat_id=user['chat_id'],
	 photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())


# change avatar
def change_avatar(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	if 'emo' in user:
		del user['emo']
	emo = get_user_emo(db, user)
	update.message.reply_text('Ready: {}'.format(emo), reply_markup=get_keyboard())


# users contacts
def get_contact(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	print(update.message.contact)
	update.message.reply_text('Ready! {}'.format(get_user_emo(db, user)), reply_markup=get_keyboard())


# users location
def get_location(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	print(update.message.location)
	update.message.reply_text('Ready! {}'.format(get_user_emo(db, user)), reply_markup=get_keyboard())


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


# subscribe
def subscribe(bot, update, user_data):
	user = get_or_create_user(db, update.effective_user, update.message)
	if not user.get('subscribed'):
		toggle_subscription(db, user)
	# subscribers.add(update.message.chat_id)
	update.message.reply_text('You subscribed!!!')
	print('subscriber')


# send messages users (if he subscribe)
@mq.queuedmessage
def send_updates(bot, job):
	# for chat_id in subscribers:
	# 	bot.sendMessage(chat_id=chat_id, text='Busyyy')
	for user in get_subscribers(db):
		try:
			bot.sendMessage(chat_id=user['chat_id'], text='Busyyy')
		except error.BadRequest:
			print('User {} not found'.format(user['chat_id']))


# unsubscribe
def unsubscribe(bot, update, user_data):
	# if update.message.chat_id in subscribers:
	# 	subscribers.remove(update.message.chat_id)
	user = get_or_create_user(db, update.effective_user, update.message)
	if user.get('subscribed'):
		toggle_subscription(db, user)
		update.message.reply_text('You unsubscribed!!!')
		print('Unsubscriber')
	else:
		update.message.reply_text("You don't subscribed, please tach /subscribe")


# users alarm button Setalarm
def set_alarm1(bot, update, user_data):
	update.message.reply_text("Enter number time after comand /alarm")


# users alarm
def set_alarm(bot, update, user_data, args, job_queue):
	# update.message.reply_text("/alarm")
	# print('/alarm')
	try:
		seconds = abs(int(args[0]))
		job_queue.run_once(alarm, seconds, context=update.message.chat_id)
	except (IndexError, ValueError):
		update.message.reply_text("Enter number time after comand_2 /alarm")


# send messages alarm
@mq.queuedmessage
def alarm(bot, job):
	bot.sendMessage(chat_id=job.context, text='Start ALARM!', reply_markup=get_keyboard())
