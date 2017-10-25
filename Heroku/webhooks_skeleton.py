import requests 
import flask 
import telepot
from telepot.loop import OrderedWebhook
from flask import Flask, request
import sys
def handle(msg):
	msg_text = msg['text']
	sender_id = msg['from']['id']
	print('Entered Handler!!!!!')
	print(msg_text)
	bot.sendMessage(sender_id, msg_text)
def handle_update(update):
	if 'message' in update:
		msg_text = update['message']['text']
		sender_id = update['message']['from']['id']
		print(msg_text)
		bot.sendMessage(sender_id, msg_text)

app = Flask(__name__)
bot = telepot.Bot('470225186:AAHY5h4DmqfSl12o9rrFH2FOlGev4E_X5XU')
webhook = OrderedWebhook(bot, {'chat':handle})


URL = '/testing_my_bot'
FULL_URL  = 'https://safe-journey-86486.herokuapp.com/testing_my_bot'

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
	webhook.run_as_thread()
	app.run(debug=True, port=443)
