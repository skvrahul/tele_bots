import telepot 
import time
from pprint import pprint
from telepot.loop import MessageLoop
import string
import requests
thread_no = 0
downloads = []
progress = []
WELCOME_MESSAGE = 'Hi! Welcome to the download bot. Here are the available commands:\n1. /download <link> - Download the given file on the local machine. \n2. /progress - Display the progress of the download \n3. /help - Display available commands'
HELP_MESSAGE = 'Here are the available commands:\n1. /download <link> - Download the given file on the local machine. \n2. /progress - Display the progress of the download \n3. /help - Display available commands'

bot = telepot.Bot('470225186:AAHY5h4DmqfSl12o9rrFH2FOlGev4E_X5XU')

def download(link, index = None):
	file_name = link.split('/')[-1]
	with open(file_name, "wb") as f:
		print("Downloading %s" % file_name)
		response = requests.get(link, stream=True)
		#Checking the file header for size or 'content-length'
		total_length = response.headers.get('content-length')
		if total_length is None:
			f.write(response.content)
		else:
			dl = 0
			total_length = int(total_length)
			for data in response.iter_content(chunk_size=4096):
				dl += len(data)
				f.write(data)
				#Calculating percentage of file that is done downloading 
				done = int(100 * dl / total_length)
				print(done)
def start_dl(link):
	t = threading.Thread(target=download, kwargs={'link':link, 'index':thread_no})
	downloads.append(thread_no)
	thread_no += 1
def handle(msg):
	msg_text = msg['text']
	sender_id = msg['from']['id']
	print(msg_text)
	if msg_text == '/start':
		bot.sendMessage(sender_id, WELCOME_MESSAGE)

	elif msg_text.startswith('/download '):
		dl_link = msg_text[10:]
		file_name = dl_link.split('/')[-1]
		download(dl_link)
		bot.sendMessage(sender_id, file_name+' has been downloaded to local PC!')

	elif msg_text == '/progress':
		pass
	elif msg_text == '/help':
		#Send back available commands
		bot.sendMessage(sender_id, HELP_MESSAGE)
		pass


MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)