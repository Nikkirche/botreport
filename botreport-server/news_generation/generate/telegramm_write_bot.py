#!pip3 install PyTelegramBotAPI
import telebot
import random
from requests import post

CHAT_ID = -1001209168677
TOKEN = "916274685:AAG-ZWgt8Cm_tehotyM4om10dWn2lJAOGJM"
bot = telebot.TeleBot(TOKEN)


def send_message_to_channel(type_event, text, chat_id=CHAT_ID):
    bot.send_message(-1001209168677, text)
    rnd = random.randint(1, 100)
    if 5 <= rnd <= 9:
        if type_event == 'GOAL':
            bot.send_sticker(CHAT_ID, TOKEN)
        if type_event == 'PENALTY':
            bot.send_sticker(CHAT_ID, TOKEN)


# send_message_to_channel('GOAL', 'GOAAAAAAAAAAAAAAAAAAL', CHAT_ID)
# post to https://t.me/sportivit
# send_message_to_channel("123", "123123")
