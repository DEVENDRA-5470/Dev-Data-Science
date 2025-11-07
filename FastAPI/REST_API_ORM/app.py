from fastapi import *
from database import *
from models import *
from sqlalchemy.orm import *

app=FastAPI(title="CRUD APPLICATION")




@app.get("/")
def root():
    return {"Messsage":"Your app is running"}

def get_db():
    db=SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Error:",e)
    finally:
        db.close()
