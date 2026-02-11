from storage import  storage_manager,oid_verify
from utils import serialization
from pathlib import Path

def location_orchestration(serialised_data:bytes):
    _, file_path =  storage_manager.paths_for_oid(serialised_data)
    if file_path.exists():
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()
       commit_obj =  serialization.deserialization(raw_content)
       return commit_obj


    else:
        raise Exception(f"file with OID {file_path} does not exist")