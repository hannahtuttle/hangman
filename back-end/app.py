import os
import requests
from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
# import pusher
# from flask_pusher import Pusher
import socketio
import random


app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
sio = socketio.Server()
sio_app = socketio.WSGIApp(sio)

# presence_pusher = Pusher(app, app_id = os.environ.get('PRESENCE_APP_ID'), key = os.environ.get('PRESENCE_KEY'), secret = os.environ.get('PRESENCE_KEY'), cluster = os.environ.get('PRESENCE_CLUSTER'))
# private_pusher = pusher_client = pusher.Pusher(
#     app_id = os.environ.get('PUSHER_APP_ID'),
#     key = os.environ.get('PUSHER_APP_KEY'),
#     secret = os.environ.get('PUSHER_APP_SECRET'),
#     cluser = os.environ.get('PUSHER_APP_CLUSTER'),
#     ssl = True
# )
# print(os.environ.get('PRESENCE_APP_ID'))
# pusher = pusher_client = pusher.Pusher(
#     app_id = os.environ.get('PRESENCE_APP_ID'),
#     key = os.environ.get('PRESENCE_KEY'),
#     secret = os.environ.get('PRESENCE_SECRET'),
#     cluster = os.environ.get('PRESENCE_CLUSTER'),
#     # ssl = True
# )

# pusher_client.trigger(u'multiplayer-hangman', u'my-event', {u'message': u'It works!'})


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
@cross_origin()
def sign_up():
    body = request.get_json()
    user = User(username =body['user']['username'], password = body['user']['password'])
    db.session.add(user)
    db.session.commit()
    new_user_id = db.session.query(User).filter_by(username=body['user']['username']).first()
    return {'user_id': new_user_id.id}

# @app.route('/login', methods=['POST'])
# @cross_origin()
# def login():
#     body = request.get_json()
#     user = db.session.query(User).filter_by(username = body['login']['username']).first()
#     if user is not None:
#         return '{}'.format(user.id)

# @app.route("/pusher/auth/<id>", methods=['POST'])
# @cross_origin()
# def pusher_authentication(id):
#     user = db.session.query(User).filter_by(id = id).first()
#     auth = pusher_client.authenticate(
#         channel=request.form['channel_name'],
#         socket_id=request.form['socket_id'],
#         custom_data={
#         u'user_id': user.username,
#         u'user_info': {
#             u'role': u'player'
#         }
#         }
#     )
#     print('auth', auth)
#     return json.dumps(auth)


@app.route('/give_phrase', methods=['POST'])
@cross_origin()
def give_phrase():
    body = request.get_json()
    phrase = Phrase(phrase = body['send_phrase']['phrase'])
    db.session.add(phrase)
    db.session.commit()
    new_phrase = db.session.query(Phrase).filter_by(phrase = phrase.phrase).first()
    game = db.session.query(Game).filter_by(id = body['send_phrase']['game_id']).first()
    player = db.session.query(User).filter_by(id = body['send_phrase']['player_id']).first()
    if player.id is game.player_1:
        game.phrase_id_1 = new_phrase.id
        db.session.commit()
    elif player.id is game.player_2:
        game.phrase_id_2 = new_phrase.id
        db.session.commit()
    # add pusher to push the phrase to the other player.
    return {'game_id':game.id, 'player1':game.player_1, 'player2':game.player_2, 'phrase1': game.phrase_id_1, 'phrase2':game.phrase_id_2}


# this route is for playing against a random generator
@app.route('/guess_phrase/<id>', methods=['GET'])
@cross_origin()
def guess_phrase(id):
    print('*********************id************************', id)
    game = db.session.query(Game).get(id)
    print('***************************************************************')
    print('player 2 id check', game.player_2)
    print('***************************************************************')

    if game.player_2 is 9:
        phrase = db.session.query(Phrase).all()
        choice = random.choice(phrase)
        return {'random_phrase': choice.phrase}
    else:
        print('checking end')
        phrase_1 = db.session.query(Phrase).filter_by(id = game.phrase_id_1).first()
        phrase_2 = db.session.query(Phrase).filter_by(id = game.phrase_id_2).first()
        return {'phrase1' : phrase_1.phrase}


@app.route('/start_game', methods=['POST'])
@cross_origin()
def start_game():
    body = request.get_json()
    game = Game(player_1 = body['player_1'], player_2 = body['player_2'])
    db.session.add(game)
    db.session.commit()
    new_game = db.session.query(Game).filter_by(player_1 = body['player_1']).first()

    return {'game_id': new_game.id, 'player1_id': new_game.player_1, 'player2_id': new_game.player_2}

@app.route('/end_game/<id>', methods=['DELETE'])
@cross_origin()
def end_game(id):
    delete = db.session.query(Game).get(id)
    db.session.delete(delete)
    db.session.commit()
    print('delete', delete.id)
    return 'deleted succesfully'

# @app.route('/players_list', methods=['GET'])
# @cross_origin()
# def get_players():
#     player_list = db.session.query(User).all()
#     players = {"players": []}
#     for player in player_list:
#         players['players'].append({"id": player.id, "username": player.username}.copy())
#     return players


if __name__ == '__main__':
    app.run() 
