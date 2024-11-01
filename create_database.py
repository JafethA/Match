import models
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query

def create_database():
    models.BaseModel.metadata.create_all(bind=engine)


if __name__=='__main__':

    create_database()