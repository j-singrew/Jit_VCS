import hashlib

def Hash_OID(serialised_data:bytes) ->bytes:
    content = serialised_data
    hash_object  = hashlib.sha256(content)
    hex_dig = hash_object.hexdigest()
    return hex_dig



    





