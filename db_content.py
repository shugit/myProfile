#!env/bin/python
from app import db, models
import datetime

models.Company.query.delete()
models.Project.query.delete()


c1 = models.Company(name='that company')
c2 = models.Company(name='this company')
c3 = models.Company(name='another company')
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)

p1 = models.Project(name='a normal project',description='a very normal project',belongsTo=c1,end_time=datetime.datetime.utcnow())
p2 = models.Project(name='a second project',description='a very second project',belongsTo=c1)
p3 = models.Project(name='a third project',description='a very third project',belongsTo=c2,end_time=datetime.datetime.utcnow())
p4 = models.Project(name='a fourth project',description='a very fourth project',belongsTo=c2)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()


companies = models.Company.query.all()
for c in companies:
    print(c.id,c.name,c.projects.all())


posts = models.Project.query.all()
for p in posts:
    print(p.id,p.name,p.description,p.belongsTo.name)

