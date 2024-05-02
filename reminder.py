from datetime import datetime
import pytz
import time
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def check_reminders(reminders):
    while True:
        taipei = pytz.timezone('Asia/Taipei')
        now = datetime.now(taipei).strftime('%H:%M')
        for reminder_user_id, reminder_time in reminders.items():
            if now == reminder_time:
                line_bot_api.push_message(reminder_user_id, TextSendMessage(text="該睡覺了！"))
        # 每分鐘檢查一次
        time.sleep(60)
