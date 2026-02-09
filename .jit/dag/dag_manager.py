from dataclasses import dataclass 
from typing import List    
from HEAD import current_HEAD
from storage import storage_manager
#kay are node 
#commit_object = {"oid":oid,"parens":CommitData.parents,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}
#values are iterables of all predecessors of that node in the graph
#https://gist.github.com/notexactlyawe/606734bcffdaa7d0c091dfbe55f09baa
#https://www.geeksforgeeks.org/python/topological-sorting-using-graphlib-python-module/

@dataclass
class Node:
    oid: bytes
    depends_on: List[bytes]

DAG = {} 

def Dag(commit_object):

    dag_commit = Node(commit_object["oid"],commit_object["parents"])

    DAG[dag_commit.oid] = dag_commit
    storage_manager.storage(dag_commit.oid)
    current_HEAD.write_head(dag_commit.oid)
    return DAG


