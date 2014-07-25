from flask import *
from NLP import parser
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parser',methods=['POST'])
def process():
    text = parser.parse(request.form['text'])
    def map_text(p):
        return [{'text':sentence[0],'categories':list(sentence[1]),'message':sentence[2]} for sentence in p]
    score = text[0]
    text = map(map_text, text[1])
    return json.dumps({'score': score, 'text': text})


if __name__ == '__main__':
    app.run('0.0.0.0')
