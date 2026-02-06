from utils import hashing,serialization
from dag import dag_manager
from HEAD import current_HEAD
def main_commit(CommitData):

    #Pass commit 
    Current_Head = current_HEAD.read_head()

    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)

    commit_object = {"oid":oid,"parents":Current_Head,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}

    DAG_creation =  dag_manager.Dag(commit_object)



