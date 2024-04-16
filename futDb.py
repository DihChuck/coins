from flask import Flask, requests, render_template, request , json

futdbHost = "https://futdb.app/api/"
futdbToken = '56a5793c-2c92-4104-8636-1293ff082b8a'

app = Flask(__name__,template_folder='templates')

@app.route('/pycall')
def pycall():
    content = request.args.get('content', 0, type=str)
    print("call_received",content)
    
    players = requests.get(futdbHost+"?page=1", headers={'accept':'application/json','X-AUTH-TOKEN': futdbToken})
    players.text
    players.json()
    print(players.text)