#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#旋轉木馬按鈕(健康新聞)
def Carousel_Template_News():
    message = TemplateSendMessage(
        alt_text='選擇新聞',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/RDmhf6r/e17deab6-5ff4-4eb2-bb96-c87bc5a235d4.jpg',
                    title='選擇新聞',
                    text='要選哪一個ლ(╹◡╹ლ)',
                    actions=[
                        PostbackTemplateAction(
                            label='食品、健康',
                            data='bbc食品、健康'
                        ),
                        PostbackTemplateAction(
                            label='健身運動科學研究',
                            data='健身運動科學研究'
                        ),
                        PostbackTemplateAction(
                            label='yahoo健康小八卦',
                            data='yahoo健康新聞'
                        )
                    ]
                )
            ]
        )
    )
    return message

#健身提醒 *開發中
def Carousel_Template_reminder():
    message = TemplateSendMessage(
        alt_text='提醒設定',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://ease-sleep.com/uploadfiles/l/20191121105548_52546.jpg',
                    title='想要提醒你睡覺嘛?',
                    text='成人每天建議睡眠時間約為7至9小時',
                    actions=[
                        DatetimePickerAction(
                            label='設定睡覺時間',
                            data='set_sleep_time',
                            mode='time',
                            initial='22:00',
                            min='00:00',
                            max='23:59'
                         ),
                     ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/zv1QhJ',
                    title='關閉提醒',
                    text='刪除之前的設定',
                    actions=[
                        PostbackTemplateAction(
                            label='關閉睡眠提醒',
                            data='stop_sleep_reminder'
                         )
                     ]
                )
            ]
        )
    )
    return message



#bmi快速回覆選單 *開發中
def Quick_Reply_Button_bmi():
    message = TextSendMessage(
        text='你的情況',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label='過輕', data='過輕'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='正常', data='正常'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='過重', data='過重'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='肥胖', data='肥胖'),
                    image_url=None
                )
            ]
        )
    )
    return message



#旋轉木馬按鈕訊息介面(開始運動) *開發中
def Carousel_Template_Sport():
    message = TemplateSendMessage(
        alt_text='開始運動',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/qnMNHg0/2024-04-05-175234.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/qnMNHg0/2024-04-05-175234.png',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.ibb.co/qnMNHg0/2024-04-05-175234.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message
