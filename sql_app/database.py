from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/postgres'
# postgres
# first_data
# "postgresql://first_data_user:UVe8dmDcPWz3vPgUtAwDodBR9RLaMU0n@dpg-chb32fqk728tp9apj7k0-a.singapore-postgres.render.com/first_data"
# ,echo=True
# 'postgresql://postgres:1234@localhost/first_data'
# 'postgresql://postgres:admin@localhost/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URL,max_overflow=-1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # inherit from this class to create ORM models