from storage import  storage_manager,oid_verification
from utils import serialization
from utils import hashing
from pathlib import Path

def DataExtraction(oid: bytes):
    visited = set()
    path = []

    while True:
        if oid in visited:
            raise Exception("Cycle detected in DAG")

        visited.add(oid)

        hex_oid = oid

        print("current oid:", hex_oid)

        commit_obj = location_orchestration(oid)

        path.append((oid, commit_obj))

        if not commit_obj.parents:
            print("We found root")
            break

        oid = commit_obj.parents[0]   # already bytes

    return path
 

def location_orchestration(current_byte_oid:bytes):


    shard_folder, file_path = storage_manager.paths_for_oid(current_byte_oid)

    if file_path.exists():
       raw_file = open(file_path,"rb")
       raw_content = raw_file.read()
       oid = current_byte_oid.decode('utf-8')
       if  oid_verification.oid_verification(raw_content,oid):
            commit_obj =  serialization.deserialization(raw_content)
            return commit_obj
       else:
            raw_file.close()
            raise Exception("file with OID ",oid," failed verification")


    else:
        raise Exception("file with OID", file_path ," does not exist")
    

    