#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from news import *
#======這裡是呼叫的檔案內容=====

#旋轉木馬按鈕(健康新聞)
def Carousel_Template_News():
    message = TemplateSendMessage(
        alt_text='選擇新聞發生錯誤',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
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


#旋轉木馬按鈕訊息介面(開始運動) 開發中

def Carousel_Template_Sport():
    message = TemplateSendMessage(
        alt_text='開始運動',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.bing.com/images/create/e4b88ae882a2e8828ce882892be9a2a8e6a0bce7b0a1e596aee6988ee7a2ba/1-660fc368cd024208b6c4f176494d23e0?id=sCAG5At9BRodAxTH%2B4lL2w.PSbF%2BGZC0BD8ubU7LCEuVw&view=detailv2&idpp=genimg&thid=OIG2.F5cqge1.MdFEOjAIPY_5&darkschemeovr=1&edgehub=1&form=GCRIDP',
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
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
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
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
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
