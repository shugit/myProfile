#!env/bin/python
from app import db, models
import datetime
from app.models import *
from datetime import date

Facility.query.delete()

f1 = Facility(name='Expedia Inc.', type='company', start_time=date(year=2014, month=12, day=8),
                     location='Beijing, China', position='Associate Software Enginneer')
f2 = Facility(name='7k7k.com', type='company', start_time=date(year=2014, month=5, day=8),
                     end_time=date(year=2014, month=7, day=10), location='Beijing, China')
f3 = Facility(name='Crystal CG', type='company', start_time=date(year=2013, month=11, day=1),
                     end_time=date(year=2013, month=12, day=24), location='Beijing, China')
f4 = Facility(name='The University of New South Wales', type='school',
                     start_time=date(year=2011, month=2, day=1),
                     end_time=date(year=2014, month=11, day=26), location='Sydney, Australia',
                     position='Bachelor of Computer Science')
f5 = Facility(name='The University of Pittsburgh', type='school', start_time=date(year=2014, month=1, day=6),
                     end_time=date(year=2014, month=4, day=30), location='Pittsburgh, USA',
                     position='Exchange of Computer Science')

db.session.add(f1)
db.session.add(f2)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)

Project.query.delete()
p1 = Project(name='Natual Language Processing',
                    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel ullamcorper urna. Ut convallis tortor in elit dapibus ullamcorper. Suspendisse iaculis ipsum egestas elit molestie, non vestibulum eros egestas. Curabitur.',
                    belongsTo=f1,
                    end_time=datetime.datetime.utcnow())
p2 = Project(name='Python Resume',
                    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel ullamcorper urna. Ut convallis tortor in elit dapibus ullamcorper. Suspendisse iaculis ipsum egestas elit molestie, non vestibulum eros egestas. Curabitur.',
                    belongsTo=f1)
p3 = Project(name='a third project',
                    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel ullamcorper urna. Ut convallis tortor in elit dapibus ullamcorper. Suspendisse iaculis ipsum egestas elit molestie, non vestibulum eros egestas. Curabitur.',
                    belongsTo=f2,
                    end_time=datetime.datetime.utcnow())
p4 = Project(name='a fourth project',
                    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus vel ullamcorper urna. Ut convallis tortor in elit dapibus ullamcorper. Suspendisse iaculis ipsum egestas elit molestie, non vestibulum eros egestas. Curabitur.',
                    belongsTo=f4)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

User.query.delete()
user = User(name='sephy', fullname='Shuwen Zhou', password='password', description='smart me')
db.session.add(user)



Skill.query.delete()
s1 = Skill(name='Java', scale=10, description='use 4 yrs')
s2 = Skill(name='Python', scale=5, description='use 2 yrs')
s3 = Skill(name='PHP', scale=4, description='use 3 yrs')
s4 = Skill(name='English', scale=9, description='GRE 161/143')
db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)


db.session.commit()

print("==Facility==")
facilities = models.Facility.query.all()
for f in facilities:
    print(f.id, f.name, f.type, f.projects.all())

print("==Project==")
projects = models.Project.query.all()
for p in projects:
    print(p.id, p.name, p.description, p.belongsTo.name)

print("==Skill==")
skill = Skill.query.all()
for s in skill:
    print(s.id, s.name, s.description, s.scale)

print("==User==")
user = User.query.all()
for u in user:
    print(u.id, u.name, u.description, u.fullname)

