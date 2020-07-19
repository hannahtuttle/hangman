from app import db
# from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    # game = db.relationship('Game', backref = 'player', lazy='dynamic')

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Phrase(db.Model):
    __tablename__ = 'phrases'

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String())
    # game = db.relationship('Game', backref = 'phrase', lazy='dynamic')

    # def __init__(self, phrase, game):
    #    self.phrase = phrase
    #    self.game = game

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    player_1 = db.Column(db.Integer, db.ForeignKey('users.id'))
    player_2 = db.Column(db.Integer, db.ForeignKey('users.id'))
    phrase_id_1 = db.Column(db.Integer, db.ForeignKey('phrases.id'))
    phrase_id_2 = db.Column(db.Integer, db.ForeignKey('phrases.id'))

    # def __init__(self, player_1, player_2, phrase_id_1, phrase_id_2):
    #    self.player_1 = player_1
    #    self.player_2 = player_2
    #    self.phrase_id_1 = phrase_id_1
    #    self.phrase_id_2 = phrase_id_2

    def __repr__(self):
        return '<id {}>'.format(self.id)
