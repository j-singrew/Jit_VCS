import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv() 

p = Path(os.getenv("FILE_PATH"))



def exists(oid) -> bool:
    for f in p.iterdir():
        if f.name == oid:
           return  True 
    return False
        


            

def storage(oid,byte):

    if exists(oid):
        raise Exception('file with OID f"{oid}" already exists')
    else:
        with open(f"{oid}","xb") as file:
            file .write(byte)

