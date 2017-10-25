import requests 
import flask 
import telepot
from flask import Flask, request
import sys
KEY = sys.argv[1]
app = Flask(__name__)
bot = telepot.Bot(KEY)
URL = '/bot_webhook'
FULL_URL  = 'https://safe-journey-86486.herokuapp.com/bot_webhook'

def handle_update(update):
	if 'message' in update:
		msg_text = update['message']['text']
		sender_id = update['message']['from']['id']
		print(msg_text)
		bot.sendMessage(sender_id, msg_text)

@app.route(URL, methods=['GET', 'POST'])
def pass_update():
	print('Received a POST request')
	update = request.get_json()
	handle_update(update)
	return 'OK'

if __name__ == '__main__':
	try:
		bot.setWebhook(FULL_URL)
	except telepot.exception.TooManyRequestsError:
		pass
	app.run(debug=True, port=443)
