import os
import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

print(os.environ.get('APP_SETTINGS'))
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from models import User, Game, Phrase

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    body = request.data
    user = User(body.username, body.password)
    db.session.add(user)
    db.session.commit()
    new_user_id = db.session.query(User).filter_by(username=body.username).first()
    return new_user_id.id

@app.route('/login', methods=['POST'])
def login(name):
    return 'Hello {}!'.format(name)

@app.route('/give_phrase', methods=['POST'])
def give_phrase():
    return ''

@app.route('/guess_phrase', methods=['GET'])
def guess_phrase():
    return ''

@app.route('/start_game', methods=['POST'])
def start_game():
    return ''

@app.route('/end_game', methods=['DELETE'])
def end_game():
    return ''


if __name__ == '__main__':
    app.run() 
