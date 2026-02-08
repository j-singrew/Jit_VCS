from persistant_storage import *
from storage_manager import  exists, paths_for_oid
from utils import serialization

def location_orchestration(oid: bytes):

    if exists(oid):
       _, file_path =  paths_for_oid(oid)
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()
       commit_obj =  serialization.deserialization(raw_content)
       return commit_obj


    else:
        raise Exception(f"file with OID {oid} does not exist")