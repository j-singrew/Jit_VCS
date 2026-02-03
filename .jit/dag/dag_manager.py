from dataclasses import dataclass 
from typing import List    
from dag import dag_manager

#kay are node 
#commit_object = {"oid":oid,"parens":CommitData.parents,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}
#values are iterables of all predecessors of that node in the graph
#https://gist.github.com/notexactlyawe/606734bcffdaa7d0c091dfbe55f09baa
#https://www.geeksforgeeks.org/python/topological-sorting-using-graphlib-python-module/

@dataclass
class Node:
    oid: bytes
    depends_on:List[str]


@dataclass
class HEAD:
    def __init__(self,oid):
        self.Head = oid


DAG = {} 

def DAG(commit_object):

    dag_commit = Node(commit_object["oid"],commit_object["parents"])

    DAG[dag_commit.oid] = dag_commit
    Head =  HEAD(dag_commit.oid)
    dag_manager.UpdateHead(Head)



    return DAG


