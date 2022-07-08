from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user,login_required, current_user,UserMixin


database_name='appointments'
database_path="postgresql://{}:{}@{}/{}".format('postgres', '123456789','localhost:5432', database_name)
#'postgresql+psycopg2://postgres@localhost:5432/todoapp20db'

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SECRET_KEY"] = "Super Secret Key"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    db.create_all()

# Models


class Users(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False)
    citas = db.relationship('Appointments', backref='usuarios')

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return f'User: id={self.id}, username={self.username}'

    def format(self):
        return {
            'id': self.id,
            'username': self.username
        }
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Appointments(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    pet = db.Column(db.String(100), nullable = False)
    date = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    
    def __init__(self,name, pet,date, owr):
        self.name=name
        self.pet=pet
        self.date=date
        
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'pet': self.pet,
            'date': self.date,
            'owner_id': self.owner_id
        }

    def __repr__(self):
        return f'Todo: id={self.id}, description={self.description}'

