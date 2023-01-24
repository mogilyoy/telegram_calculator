
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import cv2
import telebot
import time
import traceback

import matplotlib.pyplot as plt
import seaborn as sns
from model_prep.cfg import bot_token

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands='start')
def start(message):
    pass

@bot.message_handler(content_types=['photo'])
def photo(message):
    img = message.photo()
    # img pass to letter exraction
    # model.predict 
    # evaluate and send the message back

def send_exeption(exeption):
    bot.send_message(
        chat_id=-1001750080589,
        text=exeption
        )

if __name__ == '__main__':
    model = joblib.load('random_forest.pkl')
    while True:
        try:
            bot.polling(non_stop=True)
        except:
            time.sleep(0.3)
            send_exeption(traceback.format_exc())
