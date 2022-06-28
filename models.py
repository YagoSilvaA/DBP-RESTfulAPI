from flask_sqlalchemy import SQLAlchemy

database_name='appointments'
database_path="postgresql+psycopg2://{}:{}@{}/{}".format('postgres', '123456789','localhost:5432', database_name)
#'postgresql+psycopg2://postgres@localhost:5432/todoapp20db'
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Models
class Appointments(db.Model):
    __tablename__ = 'Appointments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    pet = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime)
    owner_id = db.Column(db.String, db.ForeignKey('Users.username'))

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False)
    citas = db.relationship('Appointments', backref='owner')