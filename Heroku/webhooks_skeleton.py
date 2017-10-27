import requests 
import flask 
import telepot
from flask import Flask, request
import sys
app = Flask(__name__)
bot = telepot.Bot('470225186:AAHY5h4DmqfSl12o9rrFH2FOlGev4E_X5XU')
URL = '/bot_webhook'
FULL_URL  = 'https://rocky-spire-61081.herokuapp.com/bot_webhook'

def handle_update(update):
	if 'message' in update:
		msg_text = update['message']['text']
		sender_id = update['message']['from']['id']
		print(msg_text)
		bot.sendMessage(sender_id, msg_text[::-1])

@app.route(URL, methods=['GET', 'POST'])
def pass_update():
	print('Received a POST request')
	update = request.get_json()
	handle_update(update)
	return 'OK'

try:
	bot.setWebhook(FULL_URL)
except telepot.exception.TooManyRequestsError:
	pass
if __name__ == '__main__':
	app.run()