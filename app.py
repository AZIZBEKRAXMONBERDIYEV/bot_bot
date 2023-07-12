from flask import Flask , request
from telegram import Bot

TOKEN="6354682365:AAFbm5e6TnyQtgVpUMrFZrQ7P6rRmjsz17k"


app=Flask(__name__)
bot=Bot(token=TOKEN)

@app.route('/', methods=["GET" , "POST"])
def salom():
    if request.method=='GET':
        return 'salom dunyo'
    elif request.method=='POST':
        updet=request.get_json()
        chr_id=updet['message']['chat']['id']
        txt='salom qalaysiz charchamasdan yuribsizmi '

        bot.send_message(chat_id=chr_id , text=txt)

        return 'got a post request!'

