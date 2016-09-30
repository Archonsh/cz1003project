#!/usr/local/bin/python3
# _*_ coding:utf8 _*_

# import necessary libraries and functions
import telepot
import telepot.aio
import time
import math
import time
import asyncio
from lib_func import lib_keyboard,lib_keyboard_select,nearest_lib,lib_close,lib_status,welcome_keyboard,lib_p_keyboard,lib_p_keyboard_select
from data_func import html,extract,ma_A,ma_B


# ================= library list init =======================
lib=['LWN Lib','HSS Lib','BIZ Lib','ADM Lib','CHN Lib']		# 'Lib' for 'Library Current Status Inquiry'
lib_p=['LWN lib','HSS lib','BIZ lib','ADM lib','CHN lib']	# 'lib' for 'Library Status Prediction'


# =========== function to handle on-chat message ============
async def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	# ====== check if lib is closed ======
	if lib_close(chat_id):
			return

	# ====== check the content type ======
	# only when users ask for nearest lib, the content type will be 'lcoation'
	# otherwise, it will be 'text'
	if content_type=='text':
		# === after service selection ===
		# select lib
		if msg['text']=='Library Current Status Inquiry':
			# await asyncio.sleep(10)
			await bot.sendMessage(chat_id, 'Please Choose Your Library', reply_markup=lib_keyboard())

		elif msg['text']=='Library Status Prediction':
		  	await bot.sendMessage(chat_id, 'Where do you want to go?', reply_markup=lib_p_keyboard())

		# ===== after lib selection =====
		# select area
		elif msg['text'] in lib:		# for lib current status inquiry
			n=lib.index(msg['text'])
			await bot.sendMessage(chat_id, 'Please Choose Your Floor and Section', reply_markup=lib_keyboard_select(n))

		elif msg['text'] in lib_p:		# for lib status prediction
			n=lib_p.index(msg['text'])
			await bot.sendMessage(chat_id, 'Please Choose Your Floor and Section', reply_markup=lib_p_keyboard_select(n))

		# ====== start / restart ======
		# any other text sent by users will start/restart the chat session
		else:
			await bot.sendMessage(chat_id, 'Welcome to NTU library assistant,\nwhat can I do for you?', reply_markup=welcome_keyboard())

	# ======= ask for nearest lib ========
	if content_type=='location':
		n=nearest_lib(msg['location']['latitude'],msg['location']['longitude'])
		print(n)
		await bot.sendMessage(chat_id, 'The nearest lib is '+lib[n]+'rary.'+'\nChoose your destination', reply_markup=lib_keyboard_select(n))


# ========== function to handle callback queries ==========
async def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, from_id, query_data)

	# display waiting information
	await bot.answerCallbackQuery(query_id, text='Got it, just a moment...')

	# distinguish the callback queries by the length of callback_data
	# i.e. 3 for "Library Current Status Inquiry"
	#	4 for "Library Status Prediction"
	# see more in 'lib_func.py'

	# ===== reply for "Library Current Status Inquiry" =====
	# use lib_status() to tell the number of available seats
	# see more in 'lib_func.py'
	if len(query_data)==3:
		if query_data=='lwn':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='hss':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='biz':
			await bot.sendMessage(from_id,text=lib_status(0))
		elif query_data=='adm':
			await bot.sendMessage(from_id,text=lib_status(1))
		elif query_data=='chn':
			await bot.sendMessage(from_id,text=lib_status(1))

	# ======= reply for "Library Status Prediction" ========
	# use ma_A() & ma_B() to predict the estimated number of people
	# see more in 'data_func.py'
	else:
		if query_data=='lwnp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12))
		elif query_data=='hssp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12))
		elif query_data=='bizp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_A(12))
		elif query_data=='admp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_B(12))
		elif query_data=='chnp':
			await bot.sendMessage(from_id,text='In the next hour, there may be around %d people in the selected area.' % ma_B(12))

# ============== function to update database ====================
async def database_update():
	while True:
		await html()
		await asyncio.sleep(300)	# update every 300 seconds

# =================== to keep the bot running ====================
bot = telepot.aio.Bot('194233496:AAFTNsUhxGYgb1ij84x0bys3Zhv3CNnE81w')
loop = asyncio.get_event_loop()
tasks = [bot.message_loop({'chat':on_chat_message,'callback_query':on_callback_query}),database_update()]
loop.create_task(asyncio.wait(tasks))

print ('Listening ...')
loop.run_forever()



# my id 121898056
