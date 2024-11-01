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
    con=sq3.connect("Match.db")
    NDF=pd.read_sql("SELECT NAICS FROM CrossM",con)
    R=NDF.to_json(orient="records")    
    return (R)


@app.get("/supplier")
def read_CM( ):
    CM=db.query(models.supplier).all()
    return CM
