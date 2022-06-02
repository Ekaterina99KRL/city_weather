import eel
import pyowm

owm = pyowm.OWM("a25a248243ddf52e6bb4f1229d84b608")

@eel.expose
def get_weather(city):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + str.title(city) + " сейчас " + str(round(temp)) + " градусов."


eel.init("web")
eel.start("main.html", size=(700, 700))
