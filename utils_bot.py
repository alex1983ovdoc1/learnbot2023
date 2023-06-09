from clarifai.rest import ClarifaiApp
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings0


# keyboard
def get_keyboard():
	contact_button = KeyboardButton('Send contacts', request_contact=True)
	location_button = KeyboardButton('Send coordinates', request_location=True)
	my_keyboard = ReplyKeyboardMarkup([
		['', '-start bot-', ''],
		['Send a cat', 'Change avatar'],
		[contact_button, location_button, 'calculator'],
		['Fill in the form', 'Subscribe', 'Unsubscribe', 'Setalarm']
		], resize_keyboard=True
		)
	return my_keyboard


# photo processing -> is cat
def is_cat(file_name):
	# ClarifaiApp not working!!!
	app = ClarifaiApp(api_key = '00a1e85297f64f35b3e680112db4f207')
	model = app.public_models.general_model
	response = model.predict_by_filename(file_name, max_concepts=5)
	print(response)
	


if __name__=='__main__':
	is_cat('images\cat1.jpeg')