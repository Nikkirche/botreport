import telebot
import requests as rq

#
# def write_to_bot(text):
#     bot = telebot.TeleBot('1487993906:AAEOqag-VZFj1rfYo3zQDEFmcUGspY-zh50')
#     bot.send_message(-1001209168677, text)
#
#
# write_to_bot('Obama')

# # post to https://t.me/sportivit

CHAT_ID = -1001209168677
TOKEN = "1487993906:AAEOqag-VZFj1rfYo3zQDEFmcUGspY-zh50"


def send_message_to_channel(text, chat_id):
    rq.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}")


send_message_to_channel("HELLO It's MARIO", CHAT_ID)
