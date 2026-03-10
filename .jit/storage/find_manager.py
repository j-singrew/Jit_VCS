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

def location_orchestration(current_byte_oid: bytes):

    print("location oid", current_byte_oid)

    shard_folder, file_path = storage_manager.paths_for_oid(current_byte_oid)

    print("file path", file_path)
    print("shard folder", shard_folder)

    if not file_path.exists():
        raise Exception("file with OID", file_path, "does not exist")

    with open(file_path, "rb") as raw_file:
        raw_content = raw_file.read()

    oid_hex = current_byte_oid.hex()

    if oid_verification.oid_verification(raw_content, oid_hex):
        commit_obj = serialization.deserialization(raw_content)
        return commit_obj
    else:
        raise Exception("file with OID", oid_hex, "failed verification")