
from random import choice

from emoji import emojize
from pymongo import MongoClient

import settings0


# create val for db Mongo
db = MongoClient(settings0.MONGO_LINK)[settings0.MONGO_DB]

# # # add my user
# user1 = {
# 	"user_id"	: 5000004444,
# 	'first_name': 'Nike',
# 	'last_name'	: 'White',
# 	'username'	: '_mike_1',
# 	'chat_id'	: 5000004444,
# 	'emo'		: 'giraffe:',
# 	'subscribed': False}
# db.users.insert_one(user1)
# print(user1)

# save user to db
def get_or_create_user(db, effective_user, message):
	user = db.users.find_one({"user_id": effective_user.id})
	if not user:
		user = {
		"user_id"	: effective_user.id,
		'first_name': effective_user.first_name,
		'last_name'	: effective_user.last_name,
		'username'	: effective_user.username,
		'chat_id'	: message.chat.id
		}
		db.users.insert_one(user)
	return user


# # take emo
# def get_user_emo(user_data):
# 	if 'emo' in user_data:
# 		return user_data['emo']
# 	else:
# 		user_data['emo'] = emojize(choice(settings0.USER_EMOJI))
# 		return user_data['emo']


# take emo
def get_user_emo(db, user_data):
	if not 'emo' in user_data:
		user_data['emo'] = choice(settings0.USER_EMOJI)
		db.users.update_one(
			{'_id': user_data['_id']},
			{'$set': {'emo': user_data['emo']}} # change 'emo'
		)
	return emojize(user_data['emo'])


# subscribe to mongoDB
def toggle_subscription(db, user_data):
	if not user_data.get('subscribed'):
		user_data['subscribed'] = True
	else:
		user_data['subscribed'] = False
	db.users.update_one(
		{'_id': user_data['_id']},
		{'$set': {'subscribed': user_data['subscribed']}} # change 'subscribed'
		)


# find subscribes
def get_subscribers(db):
	return db.users.find({'subscribed': True})
