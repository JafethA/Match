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

