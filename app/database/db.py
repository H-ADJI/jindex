from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils.setting import env_vars

# Provides connection with the database
engine = create_engine(env_vars.DB_URL)

# Session factory used to create an instance session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all model, holds metadata to create table and map them to objects
Base = declarative_base()



def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
