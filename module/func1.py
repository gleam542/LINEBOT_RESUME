# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 03:58:14 2020

@author: gleam
"""

from django.conf import settings
from linebot import LineBotApi
from linebot.models import URIAction,VideoSendMessage,MessageAction,QuickReply,QuickReplyButton,LocationSendMessage,StickerSendMessage,TextSendMessage, ImageSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
line_bot_api=LineBotApi('Zwj20l2P/UDOsTFuyTNe8SmuC7LUBg6Ngo0VB+0FhLFSqPWxNI8gE2Qkvm9UsWDEbBOvTy9RlQ0W7pS0ZLxd6neVmxyDFvXoySe8Jo/mVIUDHryvpUoztCtlcFR0PTw9benMvr777OLqqCRiKjWErwdB04t89/1O/w1cDnyilFU=')
baseurl = 'https://linebot-resume.onrender.com/static/'
def sendButton(event):
    try:
        message=TemplateSendMessage(
            alt_text='黃冠智履歷表',
            template=ButtonsTemplate(
                    thumbnail_image_url=baseurl +'bear.jpg',
                    title='黃冠智履歷表',
                    text='請選擇:',
                    actions=[
                             PostbackTemplateAction(label='期待工作職稱',text='期待工作職稱',data='action=履歷&item=3'),
                              PostbackTemplateAction(label='期待薪資',text='期待薪資',data='action=履歷&item=2' ),
                             PostbackTemplateAction(label='期待工作區域',text='期待工作區域',data='action=履歷&item=4' ),
                             PostbackTemplateAction(  #執行Postback功能,觸發Postback事件
                             label='顯示完整履歷',  #按鈕文字
                             text='顯示完整履歷',
                             data='action=履歷&item=1'  #Postback資料
                             ),
                    ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='error'))
def sendImage1(event):  #傳送圖片
    try:
        message = [TextSendMessage(  #傳送y文字
                text = "Python全國ibon列表爬蟲作品如下,請點進去觀看呦~"),
                   VideoSendMessage(
            original_content_url=baseurl + 'ibon.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'ibon.jpg'
            ),
            TextSendMessage(
            text='觀看其他作品請點下列選項',
            quick_reply=QuickReply(
                items=[
                    
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="每日Foodpanda優惠碼爬蟲", text="每日Foodpanda優惠碼爬蟲",data='action=作品&item=2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(1)", text="python資料分析-疫情與美股(1)",data='action=作品&item=3')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(2)", text="python資料分析-疫情與美股(2)",data='action=作品&item=4')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(3)", text="python資料分析-疫情與美股(3)",data='action=作品&item=5')
                    ),]))
           ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImage2(event):  #傳送圖片
    try:
        message = [TextSendMessage(  #傳送y文字
                text = "每日Foodpanda優惠碼爬蟲作品如下,請點進去觀看呦~"),
                  VideoSendMessage(
            original_content_url=baseurl + 'Foodpanda.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'Foodpanda.jpg'
            ),
            TextSendMessage(
            text='觀看其他作品請點下列選項',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="Python全國ibon列表爬蟲", text="Python全國ibon列表爬蟲",data='action=作品&item=1')
                    ),
                    
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(1)", text="python資料分析-疫情與美股(1)",data='action=作品&item=3')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(2)", text="python資料分析-疫情與美股(2)",data='action=作品&item=4')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(3)", text="python資料分析-疫情與美股(3)",data='action=作品&item=5')
                    ),]))
           ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImage3(event):
    try:
        message=[TextSendMessage(text='以下是python程式語言證照與python爬蟲技術證照'),
                  ImageSendMessage(
                      original_content_url='https://i.imgur.com/Me8PFSe.jpg',
                      preview_image_url='https://i.imgur.com/Me8PFSe.jpg'),
                   ImageSendMessage(
                       original_content_url='https://i.imgur.com/jaESwoo.jpg',
                       preview_image_url='https://i.imgur.com/jaESwoo.jpg'),
                    TextSendMessage(text='以下是本人的大學畢業證書'),
                    ImageSendMessage(
                        original_content_url='https://i.imgur.com/umvK53H.jpg',
                        preview_image_url='https://i.imgur.com/umvK53H.jpg')
                 ]
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, message)
def sendImage4(event):  #傳送圖片
    try:
        message = [ImageSendMessage(
            original_content_url = "https://i.imgur.com/2c9SARk.jpg",
            preview_image_url = "https://i.imgur.com/2c9SARk.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/wsgBi2w.jpg",
            preview_image_url = "https://i.imgur.com/wsgBi2w.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/hsiXtek.jpg",
            preview_image_url = "https://i.imgur.com/hsiXtek.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/QOetuBn.jpg",
            preview_image_url = "https://i.imgur.com/QOetuBn.jpg"),
           
            TextSendMessage(
            text='觀看其他作品請點下列選項',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="Python全國ibon列表爬蟲", text="Python全國ibon列表爬蟲",data='action=作品&item=1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="每日Foodpanda優惠碼爬蟲", text="每日Foodpanda優惠碼爬蟲",data='action=作品&item=2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(2)", text="python資料分析-疫情與美股(2)",data='action=作品&item=4')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(3)", text="python資料分析-疫情與美股(3)",data='action=作品&item=5')
                    ),]))
            ]
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImage5(event):  #傳送圖片
    try:
        message = [
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/oHdC0Om.jpg",
            preview_image_url = "https://i.imgur.com/oHdC0Om.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/IdToXpA.jpg",
            preview_image_url = "https://i.imgur.com/IdToXpA.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/k9wUJ7p.jpg",
            preview_image_url = "https://i.imgur.com/k9wUJ7p.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/wYxY3Fh.jpg",
            preview_image_url = "https://i.imgur.com/wYxY3Fh.jpg"),
            
            TextSendMessage(
            text='觀看其他作品請點下列選項',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="Python全國ibon列表爬蟲", text="Python全國ibon列表爬蟲",data='action=作品&item=1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="每日Foodpanda優惠碼爬蟲", text="每日Foodpanda優惠碼爬蟲",data='action=作品&item=2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(1)", text="python資料分析-疫情與美股(1)",data='action=作品&item=3')
                    ),
                    
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(3)", text="python資料分析-疫情與美股(3)",data='action=作品&item=5')
                    ),]))]
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImage6(event):  #傳送圖片
    try:
        message = [
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/O9nLS8G.jpg",
            preview_image_url = "https://i.imgur.com/O9nLS8G.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/J02fK7q.jpg",
            preview_image_url = "https://i.imgur.com/J02fK7q.jpg"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/cVrw6Py.jpg",
            preview_image_url = "https://i.imgur.com/cVrw6Py.jpg"),
            TextSendMessage(
            text='觀看其他作品請點下列選項',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="Python全國ibon列表爬蟲", text="Python全國ibon列表爬蟲",data='action=作品&item=1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="每日Foodpanda優惠碼爬蟲", text="每日Foodpanda優惠碼爬蟲",data='action=作品&item=2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(1)", text="python資料分析-疫情與美股(1)",data='action=作品&item=3')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(2)", text="python資料分析-疫情與美股(2)",data='action=作品&item=4')
                    ),
                    ]))]
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '黃冠智履歷如下\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendMulti(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  #傳送文字
                text = "薪資大概至少5萬元/月"),
            StickerSendMessage(  #傳送貼圖
                package_id='1',  
                sticker_id='2'
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendMulti1(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  #傳送文字
                text = "理想職稱是軟體工程師"),
            ImageSendMessage(
            original_content_url = "https://i.imgur.com/8XWg85f.jpg",
            preview_image_url = "https://i.imgur.com/8XWg85f.jpg"),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendPosition(event):  #傳送位置
    try:
        message = LocationSendMessage(
        title='台北市',
        address='台北市信義區',
        latitude=25.034207,  #緯度
        longitude=121.564590  #經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='以下這些是目前的作品，請點選您要觀看的作品',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="Python全國ibon列表爬蟲", text="Python全國ibon列表爬蟲",data='action=作品&item=1')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="每日Foodpanda優惠碼爬蟲", text="每日Foodpanda優惠碼爬蟲",data='action=作品&item=2')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(1)", text="python資料分析-疫情與美股(第1部分)",data='action=作品&item=3')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(2)", text="python資料分析-疫情與美股(第2部分)",data='action=作品&item=4')
                    ),
                    QuickReplyButton(
                        action=PostbackTemplateAction(label="python資料分析-疫情與美股(3)", text="python資料分析-疫情與美股(第3部分)",data='action=作品&item=5')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgCarousel(event):
    try:
        message = [TextSendMessage(text='請左右滑動圖片並點選您要的項目'),TemplateSendMessage(
            alt_text='證照與作品',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/v3qsKFj.png',
                        action=PostbackTemplateAction(
                            label='證照相關',
                            text='我要看證照相關',
                            data='action=證照&item=0'
                        )
                    ),
 					ImageCarouselColumn(
                        image_url='https://i.imgur.com/dlJwk2t.jpg',
                        action=PostbackTemplateAction(
                            label='作品',
                            text='我要看作品',
                            data='action=作品&item=0'
                        )
                    )
                ]
            )
        )]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = '這是本人的 ' + backdata.get('item')
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel_allresume(event):
    try:
        #履歷图片
        image_urls = [
                    "https://i.imgur.com/FKehB23.jpg"
                     ,"https://i.imgur.com/3yCKd4p.jpg"
                     ,"https://i.imgur.com/LuhjgBO.jpg"
                     ,"https://i.imgur.com/jKnUFKR.jpg"
                     ,"https://i.imgur.com/9emzvHH.jpg"
                     ,"https://i.imgur.com/TLkhOO7.jpg"
                     ,"https://i.imgur.com/YffnSaH.jpg"
                     ,"https://i.imgur.com/tGIbrLw.jpg"
                 
                 ]
        message = [TextSendMessage(text='請左右滑動圖片'),TemplateSendMessage(
            alt_text='完整履歷',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/FKehB23.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/FKehB23.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/3yCKd4p.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/3yCKd4p.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/LuhjgBO.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/LuhjgBO.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/jKnUFKR.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/jKnUFKR.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/9emzvHH.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/9emzvHH.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/TLkhOO7.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/TLkhOO7.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/YffnSaH.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/YffnSaH.jpg'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/tGIbrLw.jpg',
                        action=URIAction(
                            label='點我查看完整圖片',
                            uri='https://i.imgur.com/tGIbrLw.jpg'
                        )
                    ),
                ]
            )
        )]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))