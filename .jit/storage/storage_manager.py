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
        raise Exception(f'file with OID {oid} already exists')
    else:
        with open(p/f"{oid}","xb") as file:
            file .write(byte)

