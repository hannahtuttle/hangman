import os
import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import random

print(os.environ.get('APP_SETTINGS'))
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())


    def __repr__(self):
        return '<id {}>'.format(self.id)

class Phrase(db.Model):
    __tablename__ = 'phrases'

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String())
 
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    player_1 = db.Column(db.Integer, db.ForeignKey('users.id'))
    player_2 = db.Column(db.Integer, db.ForeignKey('users.id'))
    phrase_id_1 = db.Column(db.Integer, db.ForeignKey('phrases.id'))
    phrase_id_2 = db.Column(db.Integer, db.ForeignKey('phrases.id'))


    def __repr__(self):
        return '<id {}>'.format(self.id)


@app.route('/sign_up', methods=['POST'])
def sign_up():
    body = request.get_json()
    user = User(username =body['username'], password = body['password'])
    db.session.add(user)
    db.session.commit()
    new_user_id = db.session.query(User).filter_by(username=body['username']).first()
    return "New User created"

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    user = db.session.query(User).filter_by(username = body['username']).first()
    if user is not None:
        return 'id: {}!'.format(user.id)

@app.route('/give_phrase', methods=['POST'])
def give_phrase():
    body = request.get_json()
    phrase = Phrase(phrase = body['phrase'])
    db.session.add(phrase)
    db.session.commit()
    new_phrase = db.session.query(Phrase).filter_by(phrase = phrase.phrase).first()
    game = db.session.query(Game).filter_by(id = body['game_id']).first()
    player = db.session.query(User).filter_by(id = body['player_id']).first()
    if player.id is game.player_1:
        game.phrase_id_1 = new_phrase.id
        db.session.commit()
    elif player.id is game.player_2:
        game.phrase_id_2 = new_phrase.id
        db.session.commit()
    # add pusher to push the phrase to the other player.
    return 'phrase id:{}'.format(new_phrase.id)

# this route is for playing against a random generator
@app.route('/guess_phrase/<id>', methods=['GET'])
def guess_phrase(id):
    game = db.session.query(Game).get(id)
    if game.player_2 is 9:
        phrase = db.session.query(Phrase).all()
        choice = random.choice(phrase)
    return '{}'.format(choice.phrase)

@app.route('/start_game', methods=['POST'])
def start_game():
    body = request.get_json()
    game = Game(player_1 = body['player_1'], player_2 = body['player_2'])
    db.session.add(game)
    db.session.commit()
    new_game = db.session.query(Game).filter_by(player_1 = body['player_1']).first()

    return 'game id: {}'.format(new_game.id)

@app.route('/end_game/<id>', methods=['DELETE'])
def end_game(id):
    delete = db.session.query(Game).get(id)
    db.session.delete(delete)
    db.session.commit()
    print('delete', delete.id)
    return 'deleted succesfully'


if __name__ == '__main__':
    app.run() 
