from utils import hashing,serialization

def main_commit(CommitData):

    #Pass commit 

    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)
    commit_object = {"oid":oid,"parens":CommitData.parents,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}

