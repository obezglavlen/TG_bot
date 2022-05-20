import requests
import threading
from src.config import HEROKU, TOKEN


def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


setInterval(lambda: requests.get(HEROKU + TOKEN), 1740)
