import telepot 
import sys
import time
from pprint import pprint
from telepot.loop import MessageLoop
import string
KEY = sys.argv[1]
bot = telepot.Bot(KEY)
def rot13(text):
	#Replace 'str' with 'string' in python2
	rot13_trans = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return str.translate(text, rot13_trans)

def handle(msg):
	msg_text = msg['text']
	sender_id = msg['from']['id']
	#pprint(msg)
	if(msg_text.startswith('/rot13 ')):
		#Send back ROT13 of the text
		pprint(msg)
		text = msg_text[7:]
		rot13_text = rot13(text)
		print(rot13_text)
		bot.sendMessage(sender_id, rot13_text)

MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)