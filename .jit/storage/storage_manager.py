import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv() 

FILE_PATH= Path(os.getenv("FILE_PATH"))

def paths_for_oid(oid: bytes) -> tuple[Path, Path]:

    str_oid = str(oid, 'utf-8')
    shard_folder = FILE_PATH / str_oid[:2]          
    file_path    = shard_folder / str_oid[2:]       
    return shard_folder, file_path

def exist(oid:str) -> bool:
    b_oid = bytes(oid, 'utf-8')
    _, file_path = paths_for_oid(b_oid)
    return file_path.exists()
        


            

def storage(oid:bytes,oid_hash:str):

    shard_folder,file_path = paths_for_oid(oid)
    shard_folder.mkdir(parents=True, exist_ok=True) 

    if file_path.exists():
        raise Exception(f"Commit {oid} already exists")

    with open(file_path,"x") as file:
            file.write(oid_hash)





def read(oid: str) -> bytes:
    _, file_path = paths_for_oid(oid)
    if not file_path.exists():
        raise Exception(f"file with OID {oid} does not exist")

    return file_path.read_bytes()