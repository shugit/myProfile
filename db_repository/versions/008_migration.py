from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
facility = Table('facility', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('start_time', Date),
    Column('end_time', Date),
)

project = Table('project', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('description', TEXT),
    Column('start_time', DATE),
    Column('end_time', DATE),
    Column('company', INTEGER),
    Column('name', VARCHAR(length=140)),
)

project = Table('project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('description', Text),
    Column('start_time', Date),
    Column('end_time', Date),
    Column('facility', Integer),
)

company = Table('company', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=140)),
    Column('start_time', DATE),
    Column('end_time', DATE),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['facility'].create()
    pre_meta.tables['project'].columns['company'].drop()
    post_meta.tables['project'].columns['facility'].create()
    pre_meta.tables['company'].columns['end_time'].drop()
    pre_meta.tables['company'].columns['name'].drop()
    pre_meta.tables['company'].columns['start_time'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['facility'].drop()
    pre_meta.tables['project'].columns['company'].create()
    post_meta.tables['project'].columns['facility'].drop()
    pre_meta.tables['company'].columns['end_time'].create()
    pre_meta.tables['company'].columns['name'].create()
    pre_meta.tables['company'].columns['start_time'].create()
