from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This code Creates:

# a SQLAlchemy Engine that will interact with our dockerized PostgreSQL database,
# a SQLAlchemy ORM session factory bound to this engine,
# and a base class for our classes definitions.


engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()



