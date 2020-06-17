from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import os
chatbot=ChatBot('Bot')
chatboot=ChatBot('Boot')
trainer=ChatterBotCorpusTrainer(chatbot)
traineer=ListTrainer(chatboot)
def bot1():
    return chatbot
def bot2():
    return chatboot

'''
while True:
    message=input('You:')
    if message != 'Bye' or message != 'bye' :
        reply = chatbot.get_response(message)
        print('ChatBot: ',reply)
    if message == 'Bye' or message == 'bye':
        print('Chatbot : Bye')
        break

while True:
    message=input('You:')
    if message != 'Bye' or message != 'bye' :
        reply = chatboot.get_response(message)
        print('ChatBot: ',reply)
    if message == 'Bye' or message == 'bye':
        print('Chatbot : Bye')
        break
'''

