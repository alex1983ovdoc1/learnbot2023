from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

import settings0




logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')



# command /start don't work
def greet_user1(bot, update, user_data):
	print('Working com /start (gree_user1')


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
	# user_text = update.message.text
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


# keyboard
def get_keyboard():
	contact_button = KeyboardButton('Send contacts', request_contact=True)
	location_button = KeyboardButton('Send coordinates', request_location=True)
	my_keyboard = ReplyKeyboardMarkup([
		['', '-start bot-', ''],
		['Send a cat', 'Change avatar'],
		[contact_button, location_button]
		], resize_keyboard=True
		)
	return my_keyboard


# take emo
def get_user_emo(user_data):
	if 'emo' in user_data:
		return user_data['emo']
	else:
		user_data['emo'] = emojize(choice(settings0.USER_EMOJI))
		return user_data['emo']


# Strart bot
def start_bot(bot, update, user_data):
	update.message.reply_text('/start0', reply_markup=get_keyboard())



# bot function
def main():
	mybot = Updater(settings0.API_KEY)
	# mybot = Updater((API_KEY, request_kwargs = PROXY)

	text2 = '--Bot starting --'
	print(text2)
	logging.info(text2)	

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user1, pass_user_data=True))
	dp.add_handler(CommandHandler('start0', greet_user, pass_user_data=True))
	dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
	dp.add_handler(RegexHandler('^(-start bot-)$', start_bot, pass_user_data=True))
	dp.add_handler(RegexHandler('^(Send a cat)$', send_cat_picture, pass_user_data=True))
	dp.add_handler(RegexHandler('^(Change avatar)$', change_avatar, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))

	dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))


	mybot.start_polling()
	mybot.idle()

if __name__=='__main__':
	main()


print('''
	1)  Updater()        - connect with telegram
	2)  .start_polling() - hears server telegram
	3)  .idle()          - don't break bot
	4)  .dispatcher      - bot dispatcher
	5)  .add_handler     - add handler
	6)  CommandHandler() - handlers command
	7)  .message         - sending to chat
	8)  .reply_text(text)- send to chat
	9)  .basicConfig     - configuration logging
	10) format=          - text to file.log
	11) level=           - level letter to file.log
	12) filename=        - name file.log
	13) .info(text)      - save to file.log
	14) MessageHandler() - handlers messages
	15) Filters()        - filter massages-text, foto, ...
	16) glob('/cat*.jp*g')- take list(files)
	17) choice(list)     - random choice
	18) .send_photo(id=,)- send photo
	19) imojize()        - emoticons
	20) ReplyKeyboardMarkup(^ $)- keyboard ^ start str, $ finish
	21) KeyboardButton   - use the keyboards button ('Send contacts', 'Send coordinats')

	''')