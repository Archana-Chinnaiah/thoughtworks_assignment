from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
bookDB = [
    {
        'id': '101',
        'name': 'python',
        'author': 'guido van rossum'
    },
    {'id': '201',
     'name': 'scala',
     'author': 'martin odersky'
     },
    {'id': '301',
     'name': 'generic java',
     'author': 'martin odersky'
     },
    {'id': '401',
     'name': 'java',
     'author': 'james gosling'
     },
    {'id': '501',
     'name': 'c',
     'author': 'dennis ritchie'
     },
    {'id': '601',
     'name': 'c++',
     'author': 'Bjarne Stroustrup'
     }
]


# get all books
@app.route('/bookdb/book', methods=['GET'])
def getAllBooks():
    return jsonify(bookDB)


# get book by ID
@app.route('/bookdb/book/<bookId>', methods=['GET'])
def getBook(bookId):
    usr = [bk for bk in bookDB if (bk['id'] == bookId)]
    return jsonify({'bk': usr})


# update a book given its ID
@app.route('/bookdb/book/<bookId>', methods=['POST'])
def updateBook(bookId):
    em = [bk for bk in bookDB if (bk['id'] == bookId)]
    if 'name' in request.json:
        em[0]['name'] = request.json['name']
    if 'author' in request.json:
        em[0]['author'] = request.json['author']
    return jsonify({'bk': em[0]})


# run app
if __name__ == '__main__':
    app.run(debug=True)
