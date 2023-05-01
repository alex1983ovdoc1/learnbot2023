from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings0



# take emo
def get_user_emo(user_data):
	if 'emo' in user_data:
		return user_data['emo']
	else:
		user_data['emo'] = emojize(choice(settings0.USER_EMOJI))
		return user_data['emo']


# keyboard
def get_keyboard():
	contact_button = KeyboardButton('Send contacts', request_contact=True)
	location_button = KeyboardButton('Send coordinates', request_location=True)
	my_keyboard = ReplyKeyboardMarkup([
		['', '-start bot-', ''],
		['Send a cat', 'Change avatar'],
		[contact_button, location_button, 'calculator']
		], resize_keyboard=True
		)
	return my_keyboard
