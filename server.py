from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello My name is ArK and I am a 24/7 working bot "

def run():
  app.run(host='0.0.0.0',port=8080)

def host():
    t = Thread(target=run)
    t.start()