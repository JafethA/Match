import models
from database import SessionLocal
from sqlalchemy import select
from fastapi import Depends, FastAPI, HTTPException, Query, Response
import pandas as pd

db = SessionLocal()

app = FastAPI()

@app.get("/User")
def read_CM( ):
    CM=db.query(models.User).all()
    return CM



@app.get("/NAICS")
def read_CM( ):
    NDF=db.execute(select(models.Cross_Match.NAICS)).all()
    return (NDF)

@app.get("/supplier")
def read_CM( ):
    CM=db.query(models.supplier).all()
    return CM
