import telebot
import random
CHAT_ID = -1001209168677
TOKEN = "1487993906:AAEOqag-VZFj1rfYo3zQDEFmcUGspY-zh50"
bot = telebot.TeleBot(TOKEN) 
def send_message_to_channel(type_event, text, chat_id):
    bot.send_message(-1001209168677, text)
    rnd=random.randint(1, 100)
    if(rnd>=5 and rnd<=9):
        if(type_event=='GOAL'):
            bot.send_sticker(CHAT_ID, 'CAACAgIAAxkBAAEBrwxf2J9rjKdERUaj9SVf_mafW9wPJQACCwEAAladvQpOseemCPvtSR4E')
        if(type_event=='PENALTI'):
            bot.send_sticker(CHAT_ID, 'CAACAgIAAxkBAAEBrw9f2J_H33XlAWqv97qPmHcCBtZ-rwACbQMAApzW5wqmXv5sCyuobx4E')
#send_message_to_channel('GOAL','GOAAAAAAAAAAAAAAAAAAL', CHAT_ID)
#post to https://t.me/sportivit
