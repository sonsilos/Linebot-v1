import os, re, json
import schedule
import time
from datetime import datetime, date, timedelta
from flask import Flask, request, abort
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

def job(t):
    text_message = TextSendMessage(text='This is job every day.')
    line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message)
    return

text_message = TextSendMessage(text='Hello, world !this is first build.')
line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message)

schedule.every().day.at("17:30").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(6000) # wait one minute

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello Translator-Bot</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print ("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print ("event.reply_token: " + event.reply_token)
    text = event.message.text
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text))
    

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)