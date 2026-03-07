from storage import  storage_manager,oid_verification
from utils import serialization
from utils import hashing
from pathlib import Path

def DataExtraction(current_byte_oid: bytes, oid: str):
    visited = set()
    path = []

    while True:
        if oid in visited:
            raise Exception("Cycle detected in DAG")
        visited.add(oid)

        if isinstance(oid, bytes):
            oid = oid.decode() 

        current_byte_oid = oid.encode('utf-8').hex()
        print("cur cur",current_byte_oid)
        commit_obj = location_orchestration(current_byte_oid, oid)
        path.append((current_byte_oid, commit_obj))

        if not commit_obj.parents:   
            print("We found root")
            break


        oid = commit_obj.parents[0].strip()       
    

    return path
 

def location_orchestration(current_byte_oid:bytes,oid:str):


    shard_folder, file_path = storage_manager.paths_for_oid(current_byte_oid)

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
    

    