from utils import hashing,serialization
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


    DAG_creation =  dag_manager.Dag(commit_object)


    storage_manager.storage(byte_oid,oid)
    current_HEAD.write_head(byte_oid)

def test_fine(commit):

    f = find_manager(commit)
    print(f)





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
    #test_fine(63623663616637613039613365396462383637653637323163376561626164313662323663316632373361306238656261613533383164353737303462323062)



