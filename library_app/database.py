from sqlalchemy import create_emgine
from sqlalchemy.orm import sessionmarker, declaratiove_base

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declaratiove_base()