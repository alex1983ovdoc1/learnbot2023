from glob import glob
import logging
from random import choice

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
	# print(user_text)
	# print(type(user_text))
	# print(user_text[:5])
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
	# print(type(update.message.text))
	# if update.message.text[:5] == '/calc':
	# 	print('__+++')

# Strart bot
def start_bot(bot, update, user_data):
	update.message.reply_text('/start0', reply_markup=get_keyboard())
	# print(update.message)
	# print()





