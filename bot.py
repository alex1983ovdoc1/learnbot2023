from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings0




logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')


def greet_user(bot, update):
	text = 'clicked/start'
	print(text)
	update.message.reply_text(text)
	text0 = 'User /{}/: "{}"'.format(update.message.chat.first_name, text)
	logging.info(text0)


def talk_to_me(bot, update):
	# user_text = update.message.text
	user_text = 'User /{}/ sended: "{}"'.\
	format(update.message.chat.first_name, update.message.text)
	# print(update.message)
	# print()
	print(user_text)
	update.message.reply_text(user_text)
	# logging.info(user_text)
	logging.info("User: %s, Chat id: %s, Message: %s",
		update.message.chat.first_name, update.message.chat.id,
		update.message.text)


def main():
	mybot = Updater(settings0.API_KEY)
	# mybot = Updater((API_KEY, request_kwargs = PROXY)

	text2 = '--Bot starting --'
	print(text2)
	logging.info(text2)	

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))


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

	''')