from utils import hashing,serialization
from dag import dag_manager
def main_commit(CommitData):

    #Pass commit 

    serialised_data = serialization.serialization(CommitData)
    oid        = hashing.Hash_OID(serialised_data)
    commit_object = {"oid":oid,"parents":CommitData.parents,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}

    DAG_creation =  dag_manager.DAG(commit_object)