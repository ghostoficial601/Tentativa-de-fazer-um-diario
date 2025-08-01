from flask import Flask, render_template, url_for
import json 
import os

app = Flask(__name__)

if not os.path.exists('textos.json'):
    with open('textos.json', "w", encoding="UTF-8") as f:
        json.dump([],f)
@app.route('/')
def home():
    caminho = "textos.json"
    with open(caminho, "r", encoding="UTF-8") as f:
        textos = json.load(f)
    return render_template('index.html', textos=textos)

@app.route('/adicao')
def adc():
    return render_template('adc.html')
if __name__=='__main__':
    app.run(debug=True)