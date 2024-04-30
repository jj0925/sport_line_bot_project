import datetime
import time

def check_reminders():
    while True:
        now = datetime.now().time()
        for user_id, reminder_times in reminders.items():
            for reminder_time in reminder_times:
                if now == reminder_time:
                    line_bot_api.push_message(user_id, TextSendMessage(text="該睡覺了！"))
        # 每分鐘檢查一次
        time.sleep(60)
