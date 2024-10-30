import models
from database import engine

def create_database():
    models.BaseModel.metadata.create_all(bind=engine)

if __name__=='__main__':
    create_database()