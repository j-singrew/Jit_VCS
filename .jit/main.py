from utils import hashing,serialization
from dag import dag_manager
from HEAD import current_HEAD

from objects import commit
#import pdb; pdb.set_trace()


# For a first commit, no parents


def main_commit(CommitData):


    Current_Head = current_HEAD.read_head()

    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)


    commit_object = {"oid":oid,"parents":[Current_Head] if Current_Head else [],"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}


    DAG_creation =  dag_manager.Dag(commit_object,serialised_data )



if __name__ == "__main__":
    import time
    from objects import commit
    
    p = commit.Commit(
        parents=[],                 # root commit
        state_hash=b"testhash",     # placeholder state
        timestamp=int(time.time()), # current unix time
        message="Initial commit"    # optional
    )
    
    main_commit(p)


