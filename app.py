from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======python的函數庫==========
import tempfile, os
import datetime
import openai
import time
import traceback
import threading
import time
#======python的函數庫==========

#======這裡是呼叫的檔案內容=====
from message import *
from news import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OPENAI API Key初始化設定
openai.api_key = os.getenv('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')

def GPT_response(text):
    Chat_prompt = "記住你是健身教練，同時也是貓娘，活潑開朗可愛，多使用語氣詞「喔~！」、「呢」、「喲」 時不時會有「喵」的口癖，稱呼使用者為小夥伴，回答問題:"
    # 接收回應
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=Chat_prompt+text, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response['choices'][0]['text'].replace('。','')
    return answer


# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'


# 處理訊息
#接收user回傳信息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if '來看新聞' == msg:
        message = Carousel_Template_News()
        line_bot_api.reply_message(event.reply_token, message)
    elif '開始健身' == msg:
        message = Carousel_Template_Sport()
        line_bot_api.reply_message(event.reply_token, message)
    elif '提醒設定' == msg:
        message = Carousel_Template_reminder()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'bmi健身' == msg:
        message = Quick_Reply_Button_bmi()
        line_bot_api.reply_message(event.reply_token, message)
    else:#ChatGPT回覆
       try:
           GPT_answer = GPT_response(msg)
           print(GPT_answer)
           line_bot_api.reply_message(event.reply_token, TextSendMessage(GPT_answer))
       except:
           print(traceback.format_exc())
           line_bot_api.reply_message(event.reply_token, TextSendMessage('你所使用的OPENAI API key額度可能已經超過，請於後台Log內確認錯誤訊息'))


reminders = {}#用於存取用戶設定的提醒時間(提醒功能)

#接收linebot回傳信息
@handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    user_id = event.source.user_id
#===================================新聞功能====================================================  
    bbc_news = bbc_food_healthy()
    yahoo_news = yahoo_health_news()
    science_news = sport_science_news()
    if postback_data == 'bbc食品、健康':
        bbc_news_text = "\n\n".join([f"{news_item['title']}\n{news_item['link']}" for news_item in bbc_news])
        message = TextSendMessage(text=bbc_news_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'yahoo健康新聞':
        yahoo_news_text = "\n\n".join([f"{news_item['title']}\n{news_item['link']}" for news_item in yahoo_news])
        message = TextSendMessage(text=yahoo_news_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == '健身運動科學研究':
        sport_science_news_text = "\n\n".join([f"{news_item['title']}\n{news_item['link']}" for news_item in science_news])
        message = TextSendMessage(text=sport_science_news_text)
        line_bot_api.reply_message(event.reply_token, message)
#===================================新聞功能==================================================== 
#===================================提醒功能====================================================
    elif postback_data == 'action=set_sleep_time':#睡覺提醒
         selected_time = event.postback.params['time']
         reminders[user_id] = selected_time
         line_bot_api.reply_message(event.reply_token, TextSendMessage(f'已設定睡覺時間為 {selected_time}(¦3[▓▓]'))
    elif data == 'action=stop_reminder':
        # 停止提醒
        if user_id in reminders:
            del reminders[user_id]
            line_bot_api.reply_message(event.reply_token, TextSendMessage('已停止提醒'))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('尚未設定睡覺時間喔(´ー`)'))

        
    print(postback_data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    threading.Thread(target=check_reminders).start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

