import time
import telebot
import nltk
import os
import logging
from bs4 import BeautifulSoup
from telebot import types

bot_token = '628798470:AAHuAHk2A4FearTIGRrPfkBZhNxvn1rppM4'
keyword = ["/search", "/rent", "/sale", "/post", "/new", "/start"]
listings = ["For rent in Makati \n House and Lot \n 4br \n 24M \n cotact: 095656556", "For rent in Caloocan \n House and Lot \n 4br \n 24M \n cotact: 095656556" ]
listing_forsale = ["For sale in Makati \n House and Lot \n 4br \n 24M \n cotact: 095656556", "For sale in Caloocan \n House and Lot \n 4br \n 24M \n cotact: 095656556", "For sale in Manila \n House and Lot \n 4br \n 24M \n cotact: 095656556"]
listing_types = [];
response = [];
logger = telebot.logger

mlpbot = telebot.TeleBot(token=bot_token)
@mlpbot.message_handler(commands=['start'])
def start(message):
    #print(os.name)
    #telebot.logger.setLevel(logging.DEBUG)
    telebot.logger.info("start log")
    mlpbot.send_message(message.chat.id, '**Hello, Welcome to RealtyTel!**')
    mlpbot.send_message(message.chat.id, 'You can use this set of commands to find or post listings. '
                                        '\n /new - create new listings'
                                         '\n /find - search any listings from this group'
                                         '\n /keywords - view keywords')
    #mlpbot.send_message(message.chat_id, '*bold* Example message')


@mlpbot.message_handler(commands=['find'])
def find_listing(message):
    mlpbot.send_message(message.chat.id, 'searching... ')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('For Rent', 'For Sale', 'house', 'hotels')
    listing_type = mlpbot.reply_to(message, 'What listing you want to search?', reply_markup=markup)
    mlpbot.register_next_step_handler(listing_type, process_searching)


def process_searching(message):
    # mlpbot.send_message(message.chat.id, "Please type some keyword to search" )
    # mlpbot.send_message(message.chat.id, "Results: " + str(message.chat.id) )
    if(message.text == "For Rent"):
        for k in listings:
            mlpbot.send_message(message.chat.id, k)
    elif(message.text == "For Sale"):
        for k in listing_forsale:
            mlpbot.send_message(message.chat.id, k)
    process_token(message.text)

@mlpbot.message_handler(commands=['search'])
def view_keywords(message):
    for k in keyword:
      mlpbot.send_message(message.chat.id, k)

def process_token(sentence):
    keyword = nltk.word_tokenize(sentence)
    #print(keyword)
while True:
    try:
        mlpbot.polling()
    except Exception:
        time.sleep(5)
