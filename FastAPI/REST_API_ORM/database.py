from sqlalchemy import *
from dotenv import load_dotenv
import os
from sqlalchemy.orm import *

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_USER_PASS")          
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")  
DB_NAME = os.getenv("DB_NAME")

DATABASE_URI=F"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine=create_engine(DATABASE_URI)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()