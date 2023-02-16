from faker import Faker
import os
import pathlib
import secrets
import random
import string
import datetime
from datetime import datetime, timedelta

fake = Faker()

def fakewrite(no,cop,mth,nm):
    fp=f"Airplane/{cop}/2021/{mth.upper()}/{nm}.txt"
    file=open(fp, "w")
    for r in range(no):
        fd=fake.date(pattern='%Y/%m/%d')
        oid=fake.random_number(digits=9, fix_len=True)
        pr=fake.random_int(0,99999)
        cm=fake.sentence()
        file.write(f"{fd}:{oid}:{pr}:{cm} \r")

def fakewrite(file,no):
    file=open(file, "w")
    for r in range(no):
        fd=fake.date(pattern='%Y/%m/%d')
        oid=fake.random_number(digits=9, fix_len=True)
        pr=fake.random_int(0,99999)
        cm=fake.sentence()
        file.write(f"{fd}:{oid}:{pr}:{cm} \r")

def test():
    cop= input("\nPlease enter Components or Operations (That EXACT spelling please): ")
    mth = input("\nPlease enter the Month: ")
    nm = input("\nPlease enter the Name of Component or Operation (.txt NOT needed): ")
    no = int(input("\nPlease enter number of records to add :"))
    fakewrite(no,cop,mth,nm)

if __name__ == "__main__":
    here = os.path.dirname(__file__)
    cop= input("\nPlease enter Components or Operations (That EXACT spelling please): ")
    no = int(input("\nPlease enter number of records to add to each file :"))
    cop="Airplane/"+cop
    path = os.path.join(here,cop)
    path = os.path.join(path,"2021")
    
    for dire,sub,files in os.walk(path):
        for filenm in files:
            reldir=os.path.relpath(dire,here)
            relfile=os.path.join(reldir,filenm)
            fakewrite(relfile,no)
            
            

    


