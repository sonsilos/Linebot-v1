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

schedule.every().monday.at("17:30").do(job)
schedule.every().tuesday.at("17:30").do(job)
schedule.every().wednesday.at("17:30").do(job)
schedule.every().thursday.at("17:30").do(job)
schedule.every().friday.at("17:30").do(job)

text_message = TextSendMessage(text='Hello, world !this is first build from app.')
line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello Translator-Bot</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

