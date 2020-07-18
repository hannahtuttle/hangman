from app import db
from sqlalchemy.dialects.postgresql import JSON

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