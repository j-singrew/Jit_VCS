import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv() 

p = Path(os.getenv("FILE_PATH"))

"""
These must ALWAYS hold:

Same input bytes → same object ID

Same object ID → same bytes

Stored objects are immutable

If something goes wrong, fail loudly

store(oid, bytes)

creates a new file

fails if the file exists

load(oid) -> bytes

returns exact bytes

fails if object does not exist

exists(oid) -> bool

convenience only

must not modify state
"""

def exists(oid) -> bool:
    for f in p.iterdir():
        if f.name == oid:
           return  True 
    return False
        


            

def storage(oid,byte):
