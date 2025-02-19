from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# loads the environment variables
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(str(DATABASE_URL), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
