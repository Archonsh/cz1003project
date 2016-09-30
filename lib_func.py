 # !/usr/local/bin/python3
#  _*_ coding:utf8 _*_

import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
from data_func import html,extract,ma_A,ma_B
bot = telepot.Bot('194233496:AAFTNsUhxGYgb1ij84x0bys3Zhv3CNnE81w')


# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service
def welcome_keyboard():
	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='Library Current Status Inquiry')],

	[KeyboardButton(text='Library Status Prediction')]
	],
	one_time_keyboard=True
	)
	return tmp


# === secondary request: library selection ===
# by repley keboards

# 1:"Library Current Status Inquiry"
# function return: selected library
def lib_keyboard():

	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='Nearest Lib',request_location=True)],

	[KeyboardButton(text='LWN Lib')],[KeyboardButton(text='BIZ Lib')],[KeyboardButton(text='HSS Lib')],[KeyboardButton(text='CHN Lib')],

	[KeyboardButton(text='ADM Lib')]
	],
	one_time_keyboard=True
	)
	return tmp

# 2:"Library Status Prediction"
# function return:selected library
def lib_p_keyboard():

	tmp=ReplyKeyboardMarkup(keyboard=
	[
	[KeyboardButton(text='LWN lib')],[KeyboardButton(text='BIZ lib')],[KeyboardButton(text='HSS lib')],[KeyboardButton(text='CHN lib')],

	[KeyboardButton(text='ADM lib')]
	],
	one_time_keyboard=True
	)
	return tmp

# === thirdary requests: area selection ===
# by inline keyboards

# 1:"Library Current Status Inquiry"
# funtction parameter: index of the selected library in the "lib" list
# function return: corresponding inline keyboard for area selection
def lib_keyboard_select(n):
	# Lee Wee Nam Library
	lwn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='5F Quite Zone',callback_data='lwn')],[InlineKeyboardButton(text='4F',callback_data='lwn')],
		[InlineKeyboardButton(text='3F',callback_data='lwn')],[InlineKeyboardButton(text='2F',callback_data='lwn')],
		]
		)
	# Humanities an Social Studies Library
	hss_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Inside',callback_data='hss')],[InlineKeyboardButton(text='Outside',callback_data='hss')],
		]
		)
	# Business Library
	biz_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='B4 Quiet Zone',callback_data='biz')],[InlineKeyboardButton(text='B3',callback_data='biz')],
		[InlineKeyboardButton(text='B2 & B1',callback_data='biz')],
		]
		)
	# Art, Design and Media Library
	adm_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='adm')],[InlineKeyboardButton(text='Section B',callback_data='adm')],
		]
		)
	# Chinese Library
	chn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='chn')],[InlineKeyboardButton(text='Section B',callback_data='chn')],
		[InlineKeyboardButton(text='Section C',callback_data='chn')],
		]
		)
	# creat a list of the inline keyboards defined above to match the "lib" list
	tmp=[lwn_lib_keyboard,hss_lib_keyboard,biz_lib_keyboard,adm_lib_keyboard,chn_lib_keyboard]
	# return the coresponding keyboard
	return tmp[n]

# 2:"Library Status Prediction"
# function parameter: index of the selected library in the "lib_p" list
# function return: corresponding inline keyboard for area selection
def lib_p_keyboard_select(n):

	lwn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='5F Quite Zone',callback_data='lwnp')],[InlineKeyboardButton(text='4F',callback_data='lwnp')],
		[InlineKeyboardButton(text='3F',callback_data='lwnp')],[InlineKeyboardButton(text='2F',callback_data='lwnp')],
		]
		)
	hss_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Inside',callback_data='hssp')],[InlineKeyboardButton(text='Outside',callback_data='hssp')],
		]
		)
	biz_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='B4 Quiet Zone',callback_data='bizp')],[InlineKeyboardButton(text='B3',callback_data='bizp')],
		[InlineKeyboardButton(text='B2 & B1',callback_data='bizp')],
		]
		)
	adm_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='admp')],[InlineKeyboardButton(text='Section B',callback_data='admp')],
		]
		)
	chn_lib_keyboard=InlineKeyboardMarkup(inline_keyboard=
		[
		[InlineKeyboardButton(text='Section A',callback_data='chnp')],[InlineKeyboardButton(text='Section B',callback_data='chnp')],
		[InlineKeyboardButton(text='Section C',callback_data='chnp')],
		]
		)
	# creat a list of the inline keyboards defined above to match the "lib_p" list
	tmp=[lwn_lib_keyboard,hss_lib_keyboard,biz_lib_keyboard,adm_lib_keyboard,chn_lib_keyboard]
	# return the coresponding keyboard
	return tmp[n]


# ============= calculation of the nearest library ===============
# by comparing the distance between current location and different libraries
# function parameter: coordinate of current location
# function return: index of the nearest library
def nearest_lib(x,y):
	dis=99999999
	n=0
	if (pow(x-1.347757,2)+pow(y-103.680900,2) < dis):
		dis = pow(x-1.347757,2)+pow(y-103.680900,2)
		n=0
	if (pow(x-1.344308,2)+pow(y-103.682256,2) < dis):
		dis = pow(x-1.344308,2)+pow(y-103.682256,2)
		n=1
	if (pow(x-1.346526,2)+pow(y-103.680051,2) < dis):
		dis = pow(x-1.346526,2)+pow(y-103.680051,2)
		n=2
	if (pow(x-1.349541,2)+pow(y-103.683809,2) < dis):
		dis = pow(x-1.349541,2)+pow(y-103.683809,2)
		n=3
	if (pow(x-1.343871,2)+pow(y-103.682369,2) < dis):
		dis = pow(x-1.343871,2)+pow(y-103.682369,2)
		n=4
	return n


# ============= check if libraries have closed ===============
# give interactive replies based on the requiring time
# function parameter: chat ID
# function return: 1 or 0:
# 	if 1 is returned, which means the library is closed,
#	then the process will exit from the main function
def lib_close(chat_id):
	t=time.localtime()
	#t=time.strptime('Sun Sep 28 18:31:30 2016','%a %b %d %H:%M:%S %Y')

	# on Sun. libraries are closed
	if t.tm_wday==6:
		bot.sendMessage(chat_id,"It's Sunday dude, all libraries are closed.\nGo relax and have fun!\nヽ(✿ﾟ▽ﾟ)ノ")
		return 1

	# from Mon. to Sat., libraries open at 8am
	elif 0<=t.tm_hour<=8:
		bot.sendMessage(chat_id,"So hard-working dude! Libraries are not open yet.\n╮(′～‵〞)╭")
		return 1

	# on Saturday, librabries close at 5pm
	elif t.tm_wday==5:
		if t.tm_hour >= 17 :
			bot.sendMessage(chat_id,"Oops, all libraries have closed.\n( ˘･з･)")
			return 1

	# on weekdays, libraries close at 9pm
	elif t.tm_hour >= 21:
			bot.sendMessage(chat_id,"Oops, all libraries have closed.\n( ˘･з･)")
			return 1
	return 0

# ============= check vacancy ===============
# in complete version of our project, here the function parameter should be selected area
# but currently we have only 2 sets of data grabbed from our own servers
# so the data is shared by all libraries 
# we just put lib_name here
def lib_status(lib_name):
	# set 50 as the number of available seats for both sets of data
	seats = [50,50]

	# get current number of people in the selected library
	num = html()[lib_name]

	# calculate left available seats
	empty = seats[lib_name]-num

	# return information to be sent
	if empty < 10:
		return 'There are only '+str(empty)+' seats available, quite crowded...'
	else:
		return 'There are '+str(empty)+" seats available, lots of space!"
