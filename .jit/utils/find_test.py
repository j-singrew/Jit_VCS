from storage import find_manager

def test_find(byte_oid:bytes,oid:str):
    return  find_manager.location_orchestration(byte_oid,oid)