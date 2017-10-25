import telepot 
import time
from pprint import pprint
from telepot.loop import MessageLoop
import string
import requests
import sys
from DLThread import *
thread_no = 0
downloads = []
WELCOME_MESSAGE = 'Hi! Welcome to the download bot. Here are the available commands:\n1. /download <link> - Download the given file on the local machine. \n2. /progress - Display the progress of the download \n3. /help - Display available commands'
HELP_MESSAGE = 'Here are the available commands:\n1. /download <link> - Download the given file on the local machine. \n2. /progress - Display the progress of the download \n3. /help - Display available commands'
KEY = sys.argv[1]
bot = telepot.Bot(KEY)


def start_dl(link):
	t = DLThread(link)
	t.start()
	downloads.append(t)

def handle(msg):
	msg_text = msg['text']
	sender_id = msg['from']['id']
	print(msg_text)
	if msg_text == '/start':
		bot.sendMessage(sender_id, WELCOME_MESSAGE)

	elif msg_text.startswith('/download '):
		dl_link = msg_text[10:]
		file_name = dl_link.split('/')[-1]
		start_dl(dl_link)
		bot.sendMessage(sender_id, 'Starting download....\nCheck progress with /progress')

	elif msg_text == '/progress':
		incomplete_downloads = [download for download in downloads if not download.done]
		reply = ''
		if len(incomplete_downloads)!=0:
			for download in incomplete_downloads:
				reply = reply + download.filename+'  :  '+str(download.progress)+'% \n'
			bot.sendMessage(sender_id, reply)
		else:
			bot.sendMessage(sender_id ,'No downloads in progress')
	elif msg_text == '/help':
		#Send back available commands
		bot.sendMessage(sender_id, HELP_MESSAGE)
		pass


MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)