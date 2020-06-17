from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from .bot import trainedbot
from .models import bot1,bot2,bot3
import speech_recognition as sr
def home(request):
    bot1.objects.all().delete()
    bot2.objects.all().delete()
    bot3.objects.all().delete()
    return render(request, 'home.html')
def home1(request):
    bot1.objects.all().delete()
    bot2.objects.all().delete()
    bot3.objects.all().delete()
    return render(request, 'home.html')
    
def bot11(request):
    if request.method == 'POST':
        if 'Speak' in request.POST:
            r1=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r1.listen(source)
            try:
                questio = str(r1.recognize_google(audio))
            except Exception:
                bot=bot1.objects.all()
                return render(request, 'bot11.html',{'bot':bot,'a':10,'message':'Something went wrong please speak again'})
        elif 'Send' in request.POST:
            questio = str(request.POST['question'])      
            
        bot11=trainedbot.bot1()

        reply = str(bot11.get_response(str(questio)))
        bot=bot1(req1=questio,res1=reply)
        bot.save()
        bot=bot1.objects.all()
        return render(request, 'bot11.html',{'bot':bot,'a':10})
    else:
        return render(request, 'bot11.html',{'a':12})

def bot22(request):
    
    if request.method =='POST':
        
        if 'Speak' in request.POST:
            r1=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r1.listen(source)
            try:
                questio = str(r1.recognize_google(audio))
            except Exception:
                bot=bot2.objects.all()
                return render(request, 'bot22.html',{'bot':bot,'a':10,'message':'Something went wrong please speak again'})
        elif 'Send' in request.POST:
            questio = str(request.POST['question'])      
            
        bot22=trainedbot.bot2()

        reply = str(bot22.get_response(str(questio)))
        bot=bot2(req2=questio,res2=reply)
        bot.save()
        bot=bot2.objects.all()

        return render(request, 'bot22.html',{'bot':bot,'a':10})
    else:
        return render(request, 'bot22.html')

def bot33(request):
    if request.method =='POST':
        max=0
        if str(request.POST['reply']) and int(request.POST['max']):
            message=str(request.POST['reply'])
            max=int(request.POST['max'])
        bot22=trainedbot.bot2()
        bot11=trainedbot.bot1()
        if max==0:
            max=max+1
            reply = str(bot22.get_response('hi'))
            bot=bot3(req3='hi',res3=reply,Ousestion='Bot1')
            bot.save()
            bot=bot3.objects.all()
            
            return render(request, 'bot33.html',{'bot':bot,"max":max,'reply':reply,'x':10})
        
        elif max%2==1 and max<100:
            max=max+1
            reply = str(bot11.get_response(message))
            bot=bot3(req3=message,res3=reply,Ousestion='Bot2')
            bot.save()
            bot=bot3.objects.all()
            return render(request, 'bot33.html',{'bot':bot,"max":max,'reply':reply,'x':10})

        elif max%2==0 and max<100:
            max=max+1
            reply = bot22.get_response(message)
            bot=bot3(req3=message,res3=reply,Ousestion='Bot1')
            bot.save()
            bot=bot3.objects.all()
            return render(request, 'bot33.html',{'bot':bot,"max":max,'reply':reply,'x':10})
    else:
        return render(request, 'bot33.html')


        

