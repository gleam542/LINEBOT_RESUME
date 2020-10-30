from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from module import func
from urllib.parse import parse_qsl

# line_bot_api = LineBotApi('9Z4CJ8vVwvrCrprsDrD6dX4lTQGOMKkj2W8g2SnMWtwuSiG4nTBMXbDTd83vCgRPKno1P0kR6nnu5hZwThbhy6y2zox+oOZ/Ojvl9wFIr7edk8LepcNyjTIIWr+R9pW3r+gW7tcspNEWSzVNHLIqzwdB04t89/1O/w1cDnyilFU=')
# parser = WebhookParser('3bb6c7d3f4b1bf76d6c7b2b1c2f44b98')

# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')
#         try:
#             events = parser.parse(body, signature)
#         except InvalidSignatureError:
#             return HttpResponseForbidden()
#         except LineBotApiError:
#             return HttpResponseBadRequest()

#         for event in events:
#             if isinstance(event, MessageEvent):
#                 if isinstance(event.message, TextMessage):
#                     mtext = event.message.text
#                     if mtext == '@按鈕樣板':
#                         func.sendButton(event)
    
#                     elif mtext == '@確認樣板':
#                         func.sendConfirm(event)
    
#                     elif mtext == '@轉盤樣板':
#                         func.sendCarousel(event)
    
#                     elif mtext == '@圖片轉盤':
#                         func.sendImgCarousel(event)
    
#                     elif mtext == '@購買飲料':
#                         func.sendPizza(event)
    
#                     elif mtext == '@yes':
#                         func.sendYes(event)
    
#             if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
#                 backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
#                 if backdata.get('action') == 'buy':
#                     func.sendBack_buy(event, backdata)
#                 elif backdata.get('action') == 'sell':
#                     func.sendBack_sell(event, backdata)

#         return HttpResponse()

#     else:
#         return HttpResponseBadRequest()
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot.models import MessageEvent,TextMessage,PostbackEvent
from module import func1
line_bot_api=LineBotApi('Zwj20l2P/UDOsTFuyTNe8SmuC7LUBg6Ngo0VB+0FhLFSqPWxNI8gE2Qkvm9UsWDEbBOvTy9RlQ0W7pS0ZLxd6neVmxyDFvXoySe8Jo/mVIUDHryvpUoztCtlcFR0PTw9benMvr777OLqqCRiKjWErwdB04t89/1O/w1cDnyilFU=')
parser=WebhookParser('5794c5910d05312c1a65820b93925db8')
@csrf_exempt
def callback(request):
    if request.method=='POST':
        signature=request.META['HTTP_X_LINE_SIGNATURE']
        body=request.body.decode('utf-8')
        try:
            events=parser.parse(body,signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event,MessageEvent):
                if isinstance(event.message,TextMessage):
                    mtext=event.message.text
                    if mtext=='我要看履歷':
                        func1.sendButton(event) 
                    elif mtext=='我要看證照與作品':
                        func1.sendImgCarousel(event)
                    # elif mtext=='我要看證照相關':
                    #     func1.sendImage3(event)
            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
                if backdata.get('action') =='履歷':
                    if backdata.get('item')=='1':
                    #func1.sendBack_buy(event, backdata)
                        func1.sendImage(event)
                    elif backdata.get('item') == '2':
                        func1.sendMulti(event)
                    elif backdata.get('item') == '3':
                        func1.sendMulti1(event)
                    elif backdata.get('item') == '4':
                        func1.sendPosition(event)
                elif backdata.get('action')=='作品':
                     if backdata.get('item')=='0':
                         func1.sendQuickreply(event)
                     elif backdata.get('item')=='1':
                         func1.sendImage1(event)
                     elif backdata.get('item')=='2':
                         func1.sendImage2(event)
                     elif backdata.get('item')=='3':
                         func1.sendImage4(event)
                     elif backdata.get('item')=='4':
                         func1.sendImage5(event)
                     elif backdata.get('item')=='5':
                         func1.sendImage6(event)
                elif backdata.get('action')=='證照':
                    if backdata.get('item')=='0':
                        func1.sendImage3(event)
                #     elif backdata.fet('item')=='1':
                #         func1.sendBack_sell(event, backdata)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()