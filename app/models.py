from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(64), index=True, unique=True)
    # TODO: Change email length in production
    email = db.Column(db.String(120), index=True, unique=True)
    
    def __repr__(self):
        return "<User %r>" % (self.nick)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140)) # #twitter
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"))
    
    def __repr__(self):
        return "<Post %r>" % (self.body)
