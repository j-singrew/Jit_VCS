from utils import hashing,serialization,find_test
from dag import dag_manager
from HEAD import current_HEAD
from storage import storage_manager

from objects import commit


# For a first commit, no parents


def main_commit(CommitData):


    Current_Head = current_HEAD.read_head()

    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)
    byte_oid =  bytes(f"{oid}", "utf-8")


    commit_object = {"oid":oid,"parents":[Current_Head] if Current_Head else [],"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}


    DAG_creation =  dag_manager.Dag(oid,serialised_data)


    storage_manager.storage(byte_oid,serialised_data)
    current_HEAD.write_head(byte_oid)

    return byte_oid,serialised_data,oid







if __name__ == "__main__":
    import time
    from objects import commit
    
    p = commit.Commit(
        parents=[],                 # root commit
        stateHash="testhash",     # placeholder state
        timeStamp=int(time.time()), # current unix time
        message="Initial commit"    # optional
    )
    
    byte_oid,serialised_data,oid = main_commit(p)

    t = find_test.test_find(byte_oid,oid)
    print(t)

    



