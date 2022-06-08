from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from NTPUFoodie_bot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext=event.message.text
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)
                name=profile.display_name
                pic_url=profile.picture_url
                message = []
                cate_list = ['中式','健康餐','咖啡廳','日式','早餐','泰式','火鍋','牛排','甜點','義式','韓式','飲料']
                if mtext == '會員資料':
                    if User_Info.objects.filter(uid=uid).exists()==False:
                        User_Info.objects.create(uid=uid,name=name,pic_url=pic_url,mtext=mtext)
                        message.append(TextSendMessage(text='會員資料新增完畢'))

                    elif User_Info.objects.filter(uid=uid).exists()==True:
                        message.append(TextSendMessage(text='已經有建立會員資料囉'))
                        user_info = User_Info.objects.filter(uid=uid)
                        for user in user_info:
                            info = 'UID: %s\nNAME: %s'%(user.uid,user.name)
                            message.append(TextSendMessage(text=info))

                elif mtext == '餐廳查詢':
                    message.append(TextSendMessage(text= name +'請問你要什麼類型的餐廳?'))
                    message.append(TextSendMessage(text= '如果不知道，可以打"種類"會推薦給你呦!'))

                elif mtext == '種類':
                    message.append(TextSendMessage(text= '有 中式\n健康餐\n咖啡廳\n日式\n早餐\n泰式\n火鍋\n牛排\n甜點\n義式\n韓式\n飲料'))


                elif FoodieDatabase.objects.filter(class_field=mtext).exists()==True:
                    ress = FoodieDatabase.objects.filter(class_field=mtext)
                    # result = dict()
                    result = []
                    for res in ress:
                        info = 'Restaurant:%s\nAddress:%s\n\n'%(res.restaurant,res.address)
                        result.append(info)
                    result_ = ''.join(result)
                    message.append(TextSendMessage(text=result_))

                # elif mtext in cate_list:
                #     rest = foodie_database_1_.objects.get(Name= mtext)
                #     message.append(TextSendMessage(text=rest))

                
                line_bot_api.reply_message(event.reply_token,message)


        return HttpResponse()
    else:
        return HttpResponseBadRequest()