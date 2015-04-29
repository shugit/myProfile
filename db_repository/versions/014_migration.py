from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
publication = Table('publication', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('description', String(length=500)),
    Column('publisher', String(length=140)),
    Column('publish_date', DateTime),
)

reward = Table('reward', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('description', String(length=500)),
)

skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=140)),
    Column('description', String(length=200)),
    Column('scale', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['publication'].create()
    post_meta.tables['reward'].create()
    post_meta.tables['skill'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['publication'].drop()
    post_meta.tables['reward'].drop()
    post_meta.tables['skill'].drop()
