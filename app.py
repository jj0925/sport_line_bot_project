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
#======python的函數庫==========

#======這裡是呼叫的檔案內容=====
from message import *
from news import *
from reminder import *
from sport import *
from bmi import *
from weight_plot import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OPENAI API Key初始化設定
openai.api_key = os.getenv('OPENAI_API_KEY')

def GPT_response(text):
    Chat_prompt = "記住你是健身教練，同時也是貓娘，活潑開朗可愛，多使用語氣詞「喔~！」、「呢」、「喲」 時不時會有「喵」的口癖，稱呼使用者為小夥伴，回答問題:"
    # 接收回應
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=Chat_prompt+text, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response['choices'][0]['text'].replace('。','')
    return answer
def get_usage_instructions():
    instructions = (
        "Linebot 介紹以及使用說明\n\n"
        "根據下方圖文介面點選不同功能:\n"
        "1. 開始運動: 總共分為上肢、核心、下肢、有氧以及熱身收操，五大部分，每個部分3個小項目供根據小伙伴的需求去改善自己需要的部位。\n"
        "2. 健身顧問: 小伙伴只要發送訊息，就可以直接跟 ChatGPT 的健身顧問進行對話哦！\n"
        "3. BMI 健康: 根據不同的 BMI 狀態有不同的改善方法，如果想要知道自己的 BMI 的話可以輸入自己的身高體重健身顧問會直接幫你計算。\n"
        "4. 健康新聞: 三種不同風格的內容，幫你爬取最新的五篇健康新聞。\n"
        "5. 健身提醒: 個人化服務，可以設定睡覺時間以及記錄體重變化（偵測「體重:」關鍵字，把你的體重以及當日日期存入）\n"
        "順便附上肌肉結構圖幫助了解自己的肌肉部位名稱\n"
    )
    return instructions

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

#儲存使用者體重
user_weight_data = {}

# 處理訊息
#接收user回傳信息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    user_id = event.source.user_id
    
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
    elif msg.startswith("體重:"):
        message = add_weight_entry(user_id,msg)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    elif msg == "繪製體重變化圖":
        image_url = plot_weight_changes(user_id)
        if image_url:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='正在繪製體重變化圖...'))
            line_bot_api.push_message(
                event.source.user_id,
                ImageSendMessage(
                    original_content_url=image_url,
                    preview_image_url=image_url
                )
            )
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='上傳圖片失敗了呢...'))
    elif msg == "使用說明"
        instructions = get_usage_instructions()
        muscle_image_url = "https://hacker1356.wordpress.com/wp-content/uploads/2020/12/image-53.png"
        line_bot_api.reply_message(
            event.reply_token, 
            [
                TextSendMessage(text=instructions),
                ImageSendMessage(
                    original_content_url=muscle_image_url,
                    preview_image_url=muscle_image_url
                )
            ]
        )
    else:#ChatGPT回覆
       try:
           GPT_answer = GPT_response(msg)
           print(GPT_answer)
           line_bot_api.reply_message(event.reply_token, TextSendMessage(GPT_answer))
       except:
           print(traceback.format_exc())
           line_bot_api.reply_message(event.reply_token, TextSendMessage('你所使用的OPENAI API key額度可能已經超過，請於後台Log內確認錯誤訊息'))

reminders = {}#用於存取用戶設定的提醒時間(提醒功能)
# 創建一個新的執行緒來運行 check_reminders 函數，並將 reminders 作為參數傳遞進去
t = threading.Thread(target=check_reminders, args=(line_bot_api,reminders))
t.start()

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
#===================================開始健身====================================================
    elif postback_data == 'upper_limbs':
        links = upper_limbs()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'pecs_back':
        links = pecs_back()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'arm':
        links = arm()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'core':
        links = core()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'abdomen':
        links = abdomen()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'waist':
        links = waist()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'lower_limbs':
        links = lower_limbs()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'thigh':
        links = thigh()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'calf':
        links = calf()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'jogging':
        links = jogging()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'swim':
        links = swim()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'bike':
        links = bike()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'warm_up':
        links = warm_up()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'take_care':
        links = take_care()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
    elif postback_data == 'joke':
        links = get_jokes()
        links_text = "\n\n".join(links)
        message = TextSendMessage(text=links_text)
        line_bot_api.reply_message(event.reply_token, message)
#===================================開始健身====================================================
#===================================bmi========================================================
    elif postback_data == 'underweight':
        links = underweight_links()
        links_text = "\n\n".join(links)
        line_bot_api.reply_message(event.reply_token, [
            TextSendMessage(text=links_text),
            TextSendMessage(text='飲食建議:\n1、多吃碳水\n2、保證蛋白質的攝入但不過量，例如:牛奶、白飯、紅肉')
        ])
    elif postback_data == 'normal':
        links = normal_links()
        links_text = "\n\n".join(links)
        line_bot_api.reply_message(event.reply_token, [
            TextSendMessage(text=links_text),
            TextSendMessage(text='希望以上內容能幫助你保持健康、雕塑身形')
        ])
    elif postback_data == 'overweight':
        links = overweight_links()
        links_text = "\n\n".join(links)
        line_bot_api.reply_message(event.reply_token, [
            TextSendMessage(text=links_text),
            TextSendMessage(text='飲食建議:\n1、限制熱量且營養均衡的飲食，三餐定時定量\n2、避免食用高熱量、高糖的精緻食物')
        ])
    elif postback_data == 'bmi_news':
        links = fetch_bmi_news()
        links_text = "\n\n".join([f"{news_item['title']}\n{news_item['link']}" for news_item in links])
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=links_text))
#===================================bmi========================================================
#===================================提醒功能====================================================
    elif postback_data == 'set_sleep_time': #睡覺提醒
         selected_time = event.postback.params['time']
         reminders[user_id] = selected_time
         line_bot_api.reply_message(event.reply_token, TextSendMessage(f'已設定睡覺時間為 {selected_time}(¦3[▓▓]'))
    elif postback_data == 'stop_sleep_reminder':
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
        

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

