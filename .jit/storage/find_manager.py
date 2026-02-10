from storage import  storage_manager
from utils import serialization
from pathlib import Path

def location_orchestration(oid:str):
    b_oid = bytes(oid, 'utf-8')
    _, file_path =  storage_manager.paths_for_oid(b_oid)
    if file_path.exists():
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()
       commit_obj =  serialization.deserialization(raw_content)
       return commit_obj


    else:
        raise Exception(f"file with OID {file_path} does not exist")