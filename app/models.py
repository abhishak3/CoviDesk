from . import db

class Hospital(db.Model):
    __tablename__ = 'Hospital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True,
                    index=True, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    
    available_beds = db.relationship('AvailableBeds', 
                    backref='hospital')

    def __repr__(self):
        return f'<Hospital {self.name}>'

class AvailableBeds(db.Model):
    __tablename__ = 'AvailableBeds'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    room_no = db.Column(db.String(8), nullable=False)
    with_oxygen = db.Column(db.Boolean, nullable=False)
    is_icu = db.Column(db.Boolean, nullable=False)
    with_ventilators = db.Column(db.Boolean, nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('Hospital.id'))

    def __repr__(self):
        return f'<AvailableBeds {self.number}>'
