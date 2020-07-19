import os
import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

print(os.environ.get('APP_SETTINGS'))
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# import bug still needs fix
from models import User, Game, Phrase

@app.route('/sign_up', methods=['POST'])
def sign_up():
    body = request.data
    user = User(body.username, body.password)
    db.session.add(user)
    db.session.commit()
    new_user_id = db.session.query(User).filter_by(username=body.username).first()
    return "New User created"

@app.route('/login', methods=['POST'])
def login(name):
    body = request.data
    user = db.session.query(User).filter_by(username  = body.username).first()
    if user is not none:
        return 'id: {}!'.format(user.id)

@app.route('/give_phrase', methods=['POST'])
def give_phrase():
    body = request.data
    phrase = Phrase(phrase = body.phrase)
    db.session.add(phrase)
    db.session.commit()
    new_phrase = db.session.query(Phrase).filter_by(phrase = phrase.phrase).first()
    game = db.session.query(Game).filter_by(id = body.game_id).first()
    player = db.session.query(User).filter_by(id = body.player_id).first()
    if player.id is game.player_1:
        game.phrase_1 = new_phrase.phrase
        db.session.commit()
    elif player.id is game.player_2:
        game.phrase_2 = new_phrase.phrase
        db.session.commit()
    # add pusher to push the phrase to the other player.
    return 'phrase id:{}'.format(new_phrase.id)

# this route is for playing against a random generator
@app.route('/guess_phrase', methods=['POST'])
def guess_phrase():
    body = request.data
    game = db.session.query(Game).filter_by(id = body.id).first()
    if game.player_2 is 0:
        phrase = db.session.query(Phrase).all()
        choice = random.choice(phrase)
    return choice

@app.route('/start_game', methods=['POST'])
def start_game():
    body = request.data
    game = Game(player_1 = body.player_1, player_2 = body.player_2)
    db.session.add(game)
    db.session.commit()
    new_game = db.session.query(Game).filter_by(player_1 = body.player_1)
    return 'game id: {}'.format(new_game.id)

@app.route('/end_game', methods=['DELETE'])
def end_game():
    body = request.data
    db.session.query(Game).filter_by(id = body.id).delete()
    db.session.commit()
    return 'deleted succesfully'


if __name__ == '__main__':
    app.run() 
