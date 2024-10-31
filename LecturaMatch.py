import pandas as pd
import sqlite3 as sq3

con=sq3.connect("Match.db")

#df=pd.read_excel('Crosswalk_Matched.xlsx')
#df.info()
#df.to_sql("Cross_Match",con,index=False)

df=pd.read_excel("Directory.xlsx")
#print(df)
df.to_sql("Directory",con,index=False)
