from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models.send_messages import SendMessage

# ポケモンの名前を渡して弱点を返すモジュール
import calcPokeType as calPT
import pandas as pd

app = Flask(__name__)

line_bot_api = LineBotApi('vqFhvGRmbpGUg6xOozuS2SqDcHFdUz5lOO9FhOAz+M9y1GFJbmv2Hsw/Ldk6c5jOn1KKc4Um3VMaszvdBkatEkpIlZHj75M1otkJmU3VzlQmFzJOfQmmNTS9QcuGFPZSezxx4nUmv/FxTYDlIyujWwdB04t89/1O/w1cDnyilFU=s')
handler = WebhookHandler('1d7a1fb66f75082cf09f49d0fac62fb9')

@app.route("/")
def test():
    return "OKKKKKK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    sendMessage = calPT.calPokeTypeMain(event.message.text)

    if sendMessage != False :
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=sendMessage))
        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="入力されたポケモンは存在しません。"))


if __name__ == "__main__":
    app.run()

