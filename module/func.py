from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn

line_bot_api = LineBotApi('9Z4CJ8vVwvrCrprsDrD6dX4lTQGOMKkj2W8g2SnMWtwuSiG4nTBMXbDTd83vCgRPKno1P0kR6nnu5hZwThbhy6y2zox+oOZ/Ojvl9wFIr7edk8LepcNyjTIIWr+R9pW3r+gW7tcspNEWSzVNHLIqzwdB04t89/1O/w1cDnyilFU=')
baseurl = 'https://linebot-resume.onrender.com/static/'

def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
			    #thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                thumbnail_image_url=baseurl +'蘋果.jpg',
                title='按鈕樣版示範',  #主標題
                text='請選擇：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買飲料'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='連結網頁',
                        uri='https://www.lccnet.com.tw/commercial/career/33/transfer_gad.asp?med=g003&mpo=37898&gclid=CjwKCAiAi4fwBRBxEiwAEO8_HmclU4DPBg-ZA7GDKANGam5pVjMpzsZXWedFK5SYSdpAtM974-9WghoCFf8QAvD_BwE'
                    ),
                    PostbackTemplateAction(  #執行Postback功能,觸發Postback事件
                        label='回傳訊息',  #按鈕文字
                        #text='@購買飲料',  #顯示文字計息
                        data='action=buy'  #Postback資料
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendConfirm(event):  #確認樣板
    try:
        message = TemplateSendMessage(
            alt_text='確認樣板',
            template=ConfirmTemplate(
                text='你確定要購買這項商品嗎？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        #thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
						thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='這是樣板一',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息一',
                                text='賣飲料'
                            ),
                            URITemplateAction(
                                label='連結聯成電腦網頁',
                                uri='https://www.lccnet.com.tw/commercial/career/33/transfer_gad.asp?med=g003&mpo=37898&gclid=CjwKCAiAi4fwBRBxEiwAEO8_HmclU4DPBg-ZA7GDKANGam5pVjMpzsZXWedFK5SYSdpAtM974-9WghoCFf8QAvD_BwE'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息一',
                                data='action=sell&item=飲料'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='這是樣板二',
                        text='第二個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息二',
                                text='賣水果'
                            ),
                            URITemplateAction(
                                label='連結yahoo奇摩網頁',
                                uri='https://tw.yahoo.com/'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息二',
                                data='action=sell&item=炸雞'
                            ),
                        ]
                    ),
 					CarouselColumn(
                        #thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
						thumbnail_image_url=baseurl +'蘋果.jpg',
                        title='這是樣板三',
                        text='第三個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息三',
                                text='賣巧克力'
                            ),
                            URITemplateAction(
                                label='連結pchome網頁',
                                uri='https://www.pchome.com.tw/'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息三',
                                data='action=sell&item=火鍋'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣飲料'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=炸雞'
                        )
                    ),
 					ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣飲料'
                        )
                    ),
 					ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣飲料'
                        )
                    ),
 					ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買飲料，我們將盡快為您製作。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，\n我們將盡快寄出商品。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買可不可紅茶，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = '點選的是賣 ' + backdata.get('item')
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

