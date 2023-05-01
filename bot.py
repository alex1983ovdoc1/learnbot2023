
import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

from handlers_bot import *
import settings0




logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

## command /start don't work
#def greet_user1(bot, update, user_data):
#	print('Working com /start (gree_user1')


# bot function
def main():
	mybot = Updater(settings0.API_KEY)
	# mybot = Updater((API_KEY, request_kwargs = PROXY)

	text2 = '--Bot starting --'
	print(text2)
	logging.info(text2)	

	dp = mybot.dispatcher
	#dp.add_handler(CommandHandler('start', greet_user1, pass_user_data=True))
	dp.add_handler(CommandHandler('start0', greet_user, pass_user_data=True))
	dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
	dp.add_handler(RegexHandler('^(-start bot-)$', start_bot, pass_user_data=True))
	dp.add_handler(RegexHandler('^(Send a cat)$', send_cat_picture, pass_user_data=True))
	dp.add_handler(RegexHandler('^(Change avatar)$', change_avatar, pass_user_data=True))
	dp.add_handler(RegexHandler('^(calculator)$', start_calculater, pass_user_data=True))
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