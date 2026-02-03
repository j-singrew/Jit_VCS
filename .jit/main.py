from utils import hashing,serialization

def main_commit(command):

    #Pass commit 

    serialised_data = serialization.serialization(command)
    commit          = hashing.Hash_OID(serialised_data)
    