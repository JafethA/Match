import pandas as pd
import sqlite3 as sq3
from database import SessionLocal
from sqlalchemy import select
import models


con=sq3.connect("Match.db")


#se carga el excel
df=pd.read_excel('Crosswalk_Matched.xlsx')
#el data frame se carga a la base de datos
df.to_sql("CrossM",con,index=False,if_exists="replace")


