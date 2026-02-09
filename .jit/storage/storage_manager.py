import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv() 

FILE_PATH= Path(os.getenv("FILE_PATH"))

def paths_for_oid(oid: str) -> tuple[Path, Path]:

    shard_folder = FILE_PATH / oid[:2]          
    file_path    = shard_folder / oid[2:]       
    return shard_folder, file_path

def exists(oid:str) -> bool:
    _, file_path = paths_for_oid(oid)
    return file_path.exists()
        


            

def storage(oid:bytes ):

    shard_folder,_ = paths_for_oid(oid)
    shard_folder.mkdir(parents=True, exist_ok=True) 

    if FILE_PATH.exists():
        with open(FILE_PATH/f"{oid}","xb") as file:
            file .write(oid)
    else:      
        raise Exception(f'file path does not exists')




def read(oid: str) -> bytes:
    _, file_path = paths_for_oid(oid)
    if not file_path.exists():
        raise Exception(f"file with OID {oid} does not exist")

    return file_path.read_bytes()