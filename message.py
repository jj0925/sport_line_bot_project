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

#健身提醒
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
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.chinatimes.com/newsphoto/2018-08-18/656/20180818002667.jpg',
                    title='紀錄您的體重變化?',
                    text='使用範例，輸入>體重:60.0，會記錄您的體重',
                    actions=[
                              MessageAction(
                                  label='繪製體重變化圖',
                                  text='繪製體重變化圖'
                              )
                          ]
                     )
            ]
        )
    )
    return message



#bmi快速回覆選單
def Quick_Reply_Button_bmi():
    message = TextSendMessage(
        text='你的情況',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label='過輕', data='underweight'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='正常', data='normal'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='過重、肥胖', data='overweight'),
                    image_url=None
                ),
                QuickReplyButton(
                    action=PostbackAction(label='相關新聞', data='bmi_news'),
                    image_url=None
                ),
            ]
        )
    )
    return message



#旋轉木馬按鈕訊息介面(開始運動)
def Carousel_Template_Sport():
    message = TemplateSendMessage(
        alt_text='開始運動',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/PNoHApL.png',
                    title='上肢運動',
                    text='選擇上肢運動吧！',
                    actions=[
                        PostbackTemplateAction(
                            label='上肢運動 綜合',
                            data='upper_limbs'
                        ),
                        PostbackTemplateAction(
                            label='胸肌、背部',
                            data='pecs_back'
                        ),
                        PostbackTemplateAction(
                            label='手臂',
                            data='arm'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/A9y6Igl.png',
                    title='核心運動',
                    text='選擇核心運動吧！',
                    actions=[
                        PostbackTemplateAction(
                            label='核心運動 綜合',
                            data='core'
                        ),
                        PostbackTemplateAction(
                            label='腹部',
                            data='abdomen'
                        ),
                        PostbackTemplateAction(
                            label='腰部',
                            data='waist'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/ntYwhn7.png',
                    title='下肢運動',
                    text='選擇下肢運動吧！',
                    actions=[
                        PostbackTemplateAction(
                            label='下肢運動 綜合',
                            data='lower_limbs'
                        ),
                        PostbackTemplateAction(
                            label='大腿',
                            data='thigh'
                        ),
                        PostbackTemplateAction(
                            label='小腿',
                            data='calf'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/Te1cGVc.png',
                    title='有氧運動',
                    text='選擇有氧運動吧！',
                    actions=[
                        PostbackTemplateAction(
                            label='慢跑',
                            data='jogging'
                        ),
                        PostbackTemplateAction(
                            label='游泳',
                            data='swim'
                        ),
                        PostbackTemplateAction(
                            label='騎車',
                            data='bike'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/lxae5eV.png',
                    title='其他運動',
                    text='選擇其他運動吧！',
                    actions=[
                        PostbackTemplateAction(
                            label='熱身運動',
                            data='warm_up'
                        ),
                        PostbackTemplateAction(
                            label='收操',
                            data='take_care'
                        ),
                        PostbackTemplateAction(
                            label='隨機一則笑話',
                            data='joke'
                        )
                    ]
                ),
            ]
        )
    )
    return message
