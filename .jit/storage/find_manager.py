from storage import  storage_manager
from utils import serialization

def location_orchestration(oid: bytes):

    if storage_manager.exists(oid):
       _, file_path =  storage_manager.paths_for_oid(oid)
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()
       commit_obj =  serialization.deserialization(raw_content)
       return commit_obj


    else:
        raise Exception(f"file with OID {oid} does not exist")