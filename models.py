from fastapi import FastAPI
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

# The "Holiday" class defines a table named "holidays" with columns for location, start and end dates,
# city, country, and creation timestamp.
class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    city = Column(String)
    country = Column(String)
    created_when = Column(DateTime, default=datetime.now)

# These lines of code are setting up a connection to a SQLite database named "holidays.db" and
# creating a table named "holidays" with columns for location, start and end dates, city, country, and
# creation timestamp using SQLAlchemy's declarative_base() method. The sessionmaker() function is also
# being used to create a session factory that will be used to interact with the database.
engine = create_engine("sqlite:///holidays.db")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
