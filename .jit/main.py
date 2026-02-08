from utils import hashing,serialization
from dag import dag_manager
from HEAD import current_HEAD
import time
import logging
from objects import commit
from pathlib import Path

# For a first commit, no parents
p = commit.Commit(
    parents=[],                # root commit
    state_hash=b"testhash",    # placeholder state
    timestamp=int(time.time()), # current unix time
    message="Initial commit"    # optional
)


def main_commit(CommitData):

    log_file = Path(".jit") / "pipeline.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s"
)
    Current_Head = current_HEAD.read_head()
    logging.debug(f"Current_Head: {Current_Head}")
        
    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)


    commit_object = {"oid":oid,"parents":[Current_Head] if Current_Head else [],"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}


    DAG_creation =  dag_manager.Dag(commit_object,serialised_data )



def __main__(p): 
    main_commit(p)


