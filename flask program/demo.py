import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] =True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1><center>HOME PAGE</center></h1>'''

@app.route('/all_books', methods=['GET'])
def api_all():
    return jsonify(books)

if __name__=='__main__':
    app.run()

