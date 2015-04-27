from app import db


class Company(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(140))
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    projects = db.relationship('Project', backref='belongsTo', lazy='dynamic')

    def logo(self, size):
        return ''

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    company = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Description %r>' % self.description

