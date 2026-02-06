from persistant_storage import *
from storage_manager import  exists, paths_for_oid


def location_orchestration(oid: bool):

    if exists(oid):
       shard_folder, file_path =  paths_for_oid(oid)
       raw_file = open("{file_path}","rb")
       raw_content = raw_file.read_bytes()

    else:
        raise Exception(f"file with OID {oid} does not exist")