from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class NGOs(UserMixin,db.Model):
    __tablename__ = 'ngos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True,
                    index=True, nullable=False)
    email = db.Column(db.String(64), unique=True,
                    nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    password_hash = db.Column(db.String(128))
    
    available_beds = db.relationship('AvailableBeds', 
                    backref='ngo')

    def __repr__(self):
        return f'<NGO {self.name}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

class AvailableBeds(db.Model):
    __tablename__ = 'AvailableBeds'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    #hospital = db.Column(db.String(64), nullable=False)
    room_no = db.Column(db.String(8), nullable=False)
    with_oxygen = db.Column(db.Boolean, nullable=False)
    is_icu = db.Column(db.Boolean, nullable=False)
    with_ventilators = db.Column(db.Boolean, nullable=False)
    ngo_id = db.Column(db.Integer, db.ForeignKey('ngos.id'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('Hospital.id'))

    def __repr__(self):
        return f'<AvailableBeds {self.number}>'

class Hospital(db.Model):
    __tablename__ = 'Hospital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    available_beds = db.relationship('AvailableBeds', backref='hospital', lazy = 'dynamic')

    def __repr__(self):
        return f'<Hospital {self.name}>'

@login_manager.user_loader
def load_hospital(ngo_id):
    return NGOs.query.get(int(ngo_id))
