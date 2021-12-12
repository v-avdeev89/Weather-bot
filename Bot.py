from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import config as cfg
import telebot

config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('f844047317897316315be2434707bd38', config)
bot = telebot.TeleBot("2066963676:AAEuWRgqfdrr2w3XJAANByQ_KKefu04pfCc")

mgr = owm.weather_manager()
@bot.message_handler(func=lambda m: True)

def echo_all(message):
	#bot.reply_to(message, message.text)
	observation = mgr.weather_at_place(message.text)
	w = observation.weather

	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура примерно " + str(temp)

	bot.send_message(message.chat.id, answer)


bot.infinity_polling()