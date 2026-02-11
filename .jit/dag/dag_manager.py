from dataclasses import dataclass 
from typing import List    
from HEAD import current_HEAD
from storage import storage_manager
import os
from objects import commit
from utils import serialization
from dotenv import load_dotenv
from pathlib import Path

DAG_FOLDER_PATH = Path(os.getenv("DAG_Folder"))
#kay are node 
#commit_object = {"oid":oid,"parens":CommitData.parents,"state_hash":CommitData.state_hash,"timestamp":CommitData.timestamp}
#values are iterables of all predecessors of that node in the graph
#https://gist.github.com/notexactlyawe/606734bcffdaa7d0c091dfbe55f09baa
#https://www.geeksforgeeks.org/python/topological-sorting-using-graphlib-python-module/

#@dataclass
#class Node:
#    oid: bytes
#   depends_on: List[bytes]


def Dag(oid:str ,serialised_data:bytes):



    str_oid = str(oid, 'utf-8')

    shard_folder = DAG_FOLDER_PATH / str_oid[:2]          
    file_path    = shard_folder / str_oid[2:]  

    shard_folder.mkdir(parents=True, exist_ok=True)  


    if file_path.exists():
          raise Exception(f"file with name {oid} already exists")
        
    
    with open(file_path,"wb") as file:
            file.write(serialised_data)