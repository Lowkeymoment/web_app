from package import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"User('{self.username}', '{self.score}' '{self.image_file}')"