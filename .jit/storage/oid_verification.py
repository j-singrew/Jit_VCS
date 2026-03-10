from utils import hashing

def oid_verification(raw_content: bytes, expected_oid: bytes) -> bool:

    computed_oid = hashing.Hash_OID(raw_content)


    if isinstance(expected_oid, bytes) and len(expected_oid) == 64:
        expected_oid = bytes.fromhex(expected_oid.decode())

    return computed_oid == expected_oid