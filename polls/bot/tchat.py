from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import os
message=''
chatbot=ChatBot('Bot')
chatboot=ChatBot('Boot')
trainer=ChatterBotCorpusTrainer(chatbot)
print('ListTrainer starts here')

traineer=ListTrainer(chatboot)
for files in os.listdir(r'C:\Users\Vishal\mysite\bot\data'):
    convData = open(r'C:\Users\Vishal\mysite\bot\data/' + files, 'r').readlines()
    traineer.train(convData)

print('Corpus trainer starts here')
trainer.train(
              'chatterbot.corpus.english.politics',
              'chatterbot.corpus.english.psychology',
              'chatterbot.corpus.english.science',
'chatterbot.corpus.english.gossip',
'chatterbot.corpus.english.health',
'chatterbot.corpus.english.history',
'chatterbot.corpus.english.humor',
'chatterbot.corpus.english.literature',
'chatterbot.corpus.english.money',
'chatterbot.corpus.english.movies',
'chatterbot.corpus.english.sports',
'chatterbot.corpus.english.trivia',

              )
while True:
    while True:
        if message != 'Bye' or message != 'bye' :
            if len(str(message))==0:
                message='hi'
                reply = chatbot.get_response(message)
                message=reply
                print('ChatBot: ',reply)
                break
            else:
                reply = chatbot.get_response(message)
                message=reply
                print('ChatBot: ', reply)
                break
        if message == 'Bye' or message == 'bye':
            print('Chatbot : Bye')
            break

    while True:
        if message != 'Bye' or message != 'bye' :
            if len(str(message))==0:
                message='hi'
                reply = chatboot.get_response(message)
                message=reply
                print('ChatBoot: ',reply)
                break
            else:
                reply = chatboot.get_response(message)
                message=reply
                print('ChatBoot: ', reply)
                break
        if message == 'Bye' or message == 'bye':
            print('Chatboot : Bye')
            break

