#!env/bin/python
from app import db, models
import datetime

models.Facility.query.delete()
models.Project.query.delete()


f1 = models.Facility(name='that company',type='company')
f2 = models.Facility(name='this company',type='company')
f3 = models.Facility(name='another company',type='company')
f4 = models.Facility(name='this school',type='school')
f5 = models.Facility(name='that school',type='school')

db.session.add(f1)
db.session.add(f2)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)

p1 = models.Project(name='a normal project',description='a very normal project',belongsTo=f1,end_time=datetime.datetime.utcnow())
p2 = models.Project(name='a second project',description='a very second project',belongsTo=f1)
p3 = models.Project(name='a third project',description='a very third project',belongsTo=f2,end_time=datetime.datetime.utcnow())
p4 = models.Project(name='a fourth project',description='a very fourth project',belongsTo=f4)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()




print("==Facility==")
facilities = models.Facility.query.all()
for f in facilities:
    print(f.id,f.name,f.type, f.projects.all())

print("==Project==")
projects = models.Project.query.all()
for p in projects:
    print(p.id,p.name,p.description,p.belongsTo.name)

