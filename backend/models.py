from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class PDF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
