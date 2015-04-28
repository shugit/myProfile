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
    Column('position', String(length=140)),
    Column('type', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['facility'].columns['position'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['facility'].columns['position'].drop()
