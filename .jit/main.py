from utils import hashing,serialization
from dag import dag_manager
from HEAD import current_HEAD
import time
from objects import commit

# For a first commit, no parents
p = commit.Commit(
    parents=[],                # root commit
    state_hash=b"testhash",    # placeholder state
    timestamp=int(time.time()), # current unix time
    message="Initial commit"    # optional
)


def main_commit(CommitData):

    #Pass commit 

    Current_Head = current_HEAD.read_head()
    with open(".jit/debug.log", "a") as f:
        f.write(f"{Current_Head}\n")
        f.flush()
    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)


    commit_object = {"oid":oid,"parents":Current_Head,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}


    DAG_creation =  dag_manager.Dag(commit_object)



def __main__(p): 
    main_commit(p)


