from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .db import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=True, unique=True)


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, nullable=False, unique=True)
    jobs = relationship("Job", back_populates="search_keywords")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text("now()"), nullable=False)
    jobs = relationship("Job", back_populates="owner")


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    linkedin_id = Column(String, index=True)
    title = Column(String)
    url = Column(String)
    location = Column(String)
    date = Column(String)
    company = Column(String)
    company_url = Column(String)
    search_keyword_id = Column(Integer, ForeignKey("keywords.id"))
    search_keywords = relationship("Keyword", back_populates="jobs")
    owner = relationship("User", back_populates="jobs")
