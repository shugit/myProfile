from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
company = Table('company', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
)

school = Table('school', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('fullname', String(length=50)),
    Column('password', String(length=12)),
)

facility = Table('facility', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('start_time', Date),
    Column('end_time', Date),
    Column('type', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['company'].drop()
    pre_meta.tables['school'].drop()
    post_meta.tables['user'].create()
    post_meta.tables['facility'].columns['type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['company'].create()
    pre_meta.tables['school'].create()
    post_meta.tables['user'].drop()
    post_meta.tables['facility'].columns['type'].drop()
