from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, re, json
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

text_message = TextSendMessage(text='Hello, world !this is first build.')
text_message2 = TextSendMessage(text='This is smart bot for help your trade.')
text_message3 = TextSendMessage(text='Please enter stcok name for anlyse data.')
line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message)
line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message2)
line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message3)

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
    # specify the url
    quote_page = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol=' + str(event.message.text)

    # query the website and return the html to the variable 'page'
    page = urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={'class': 'round-border'})

    name = name_box.text.strip(' \t\n\r') # strip() is used to remove starting and trailing
    text_message = TextSendMessage(text=name)
    line_bot_api.reply_message(
            event.reply_token,
            text_message)
    

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


# def job():
#     text_message = TextSendMessage(text='This is job every day.')
#     line_bot_api.push_message('U3f3b79342293017ebce23e9bc12f5c63', text_message)
#     return

# schedule.every().day.at("17:30").do(job)

# while True:
#     schedule.run_pending()
    # time.sleep(6000) # wait one minute