from utils import hashing,serialization,find_test
from dag import dag_manager,dag_transversal
from HEAD import current_HEAD
from storage import storage_manager, find_manager

from objects import commit


# For a first commit, no parents


def main_commit(CommitData):

    if CommitData.parents == []:
        Current_Head = None

    else:
        Current_Head = current_HEAD.read_head()
        
    print("Cur_head", Current_Head)
    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)
    byte_oid =  bytes(oid, "utf-8")


    commit_object = {"oid":oid,"parents":[Current_Head] if Current_Head else [],"state_hash":CommitData.stateHash,"timestamp":CommitData.timeStamp}


    DAG_creation =  dag_manager.Dag(oid,serialised_data)


    storage_manager.storage(byte_oid,serialised_data)
    current_HEAD.write_head(byte_oid)   
    c = current_HEAD.read_head()
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
    
    byte_oid,serialised_data,oid= main_commit(p)

    t = find_test.test_find(byte_oid,oid)
    Current_Head = current_HEAD.read_head()


    
    new_commit = commit.Commit(
    parents=[Current_Head],
    stateHash="hash2",
    timeStamp=int(time.time()),
    message="Second commit"
    )

    byte_oid, serialised_data, oid= main_commit(new_commit)
    print("byte oid",type(byte_oid))
    print("second coming ", type(Current_Head))
    m = dag_transversal.transverse(Current_Head)
    t = find_test.test_find(byte_oid,oid)
    print("Test find ",m)
    d = find_manager.DataExtraction(byte_oid,oid)

    



