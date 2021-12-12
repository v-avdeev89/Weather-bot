from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import config as cfg

config = cfg.get_default_config()
config['language'] = 'ru'
owm = OWM('f844047317897316315be2434707bd38', config)
mgr = owm.weather_manager()

place = input("Привет! Подскажи из кого ты города:")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас примерно " + str(temp))