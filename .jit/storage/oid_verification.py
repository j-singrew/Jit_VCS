from utils import hashing
def oid_verification(raw_content:bytes,serialised_data:bytes) -> bool :
    

    try:
        if hashing.Hash_OID(raw_content) == serialised_data:
            return True

    
    except:
        raise Exception("Hash function does not match")
