import requests
import json
from flask import Flask, render_template, request
from connection import selectUserData,selectLastPlayers

app = Flask(__name__,template_folder='templates')
user = selectUserData(2);

@app.route("/")
def home():
    css_custom = [
        './static/css/fut24.css',
        './static/css/main-new.css',
        './static/css/all.css',
        './static/assets/vendor/css/pages/ui-carousel.css'
    ]
    js_custom = [
        './static/assets/js/ui-carousel.js'
    ]
    lastPlayers = selectLastPlayers()
 
    return render_template('home.html', datauser = user , page = 'home' ,css_custom = css_custom,lastPlayers = lastPlayers, js_custom = js_custom)

@app.route("/sniper")
def sniper():
    return render_template('sniper.html', datauser = user, page = 'sniper',css_custom = "", js_custom = "")
