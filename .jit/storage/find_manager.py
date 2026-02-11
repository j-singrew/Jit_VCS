from storage import  storage_manager,oid_verification
from utils import serialization
from utils import hashing
from pathlib import Path

def location_orchestration(byte_oid:bytes,oid:str):
    _, file_path =  storage_manager.paths_for_oid(byte_oid)
    if file_path.exists():
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()

       if  oid_verification.oid_verification(raw_content,oid):
            commit_obj =  serialization.deserialization(raw_content)
            return commit_obj
       else:
            raw_file.close()
            raise Exception(f"file with OID {oid} failed verification")


    else:
        raise Exception(f"file with OID {file_path} does not exist")