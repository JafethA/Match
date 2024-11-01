from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    company_name = Column(String(50), nullable = False, index = True)
    website = Column(String(50), nullable = True)
    addres = Column(String(100), nullable = False)
    phone_number =Column(String(15), nullable=False )
    contact_person = Column(String(15), nullable = False)
    email = Column(String(30),nullable = False)
    linkedln_profile = Column(String(30), nullable=True)
    industry_types= Column(String(30), nullable= False)
    naics_codes=Column(String(30), nullable=False)

    def __repr__(self):
        return f"<Company Name: {self.company_name}, {self.website}, Phone Number: {self.phone_number}>"


class Vendor (BaseModel):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cetifications = Column(String(30), nullable=False)
    ethnicity=Column(String(30), nullable=False)
    projects_undertaken=Column(String(100), nullable=False)
    certified = Column(String(30), nullable=False)
    vendor_company=Column(String(50), ForeignKey('users.id')) 


class supplier(BaseModel):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    technical_assistance = Column(String(30), nullable=False)
    agency_name = Column(String(30), nullable=False)
    project_name = Column(String(30), nullable=False)
    budget = Column(String(30), nullable=False)
    scope_of_work = Column(String(50), nullable=False)
    keywords = Column(String(50), nullable=False)
    required_xp= Column(String(50))
    matching_criteria = Column(String(50), nullable=False)
    agency_id=Column(String(30))
    gateway_inf=Column(String(30), nullable=True)
    supplier_company=Column(String(30), ForeignKey('users.id'))

class Cross_Match(BaseModel):
    __tablename__='CrossM'
    id = Column(Integer, primary_key=True,index=True)
    RecordID = Column(Integer, primary_key=True)
    NAICS = Column(Integer, nullable=False)
    DESCRIPTION = Column(String(100))
    Core18=Column(String(20))
    Core4=Column(String(5))
    ENSequence=Column(Integer)
    ECodingS=Column(String(20))
    KeywordED=Column(String(50))

class Directory(BaseModel):
    __tablename__="Directory"
    id = Column(Integer, primary_key=True)
    CName = Column(String(50), nullable=False)
    DBAName = Column(String(50), nullable=True)
    OwnerFirst = Column(String(20),nullable=False)
    OwnerLast = Column(String(20), nullable=False)
    Address = Column(String(50), nullable=False)
    City = Column(String(30),nullable=False)
    State = Column(String(10),nullable=False)
    Zip = Column(String(10),nullable=False)
    mail_Adress = Column(String(50),nullable=False)
    City_1 = Column(String(30),nullable=False)
    State_1 = Column(String(10),nullable=False)
    Zip_1 = Column(String(10),nullable=False)
    Phone = Column(String(15), nullable=False)
    Fax = Column(String(15),nullable=True)
    email = Column(String(30),nullable=False)
    Website = Column(String(40),nullable=False)
    Agency = Column(String(10), nullable=False)
    Certification_type = Column(String(10), nullable=False)
    Certified = Column(String(20), nullable=False)
    Keywords = Column(String(100), nullable=False)
    Work_Districs_Regions = Column(String(40), nullable=False)
    Industry = Column(String(50),nullable=False)
    Business_size = Column(String(30), nullable=False)
    General_Location = Column(String(30),nullable=False)
    Location = Column(String(30), nullable=False)


