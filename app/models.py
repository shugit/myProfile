from app import db

class Facility(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(140))
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    projects = db.relationship('Project', backref='belongsTo', lazy='dynamic')
    position = db.Column(db.String(140))
    location = db.Column(db.String(140))
    type = db.Column(db.String(50))

    def logo(self, size):
        return ''

    def __repr__(self):
        return '<name %r>' % (self.name)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    facility = db.Column(db.Integer,db.ForeignKey('facility.id'))

    def __repr__(self):
        return '<Description %r>' % self.description

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    password = db.Column(db.String(12))
    description=db.column(db.String(200))
    def get_auth_token(self):
        return self.password

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)