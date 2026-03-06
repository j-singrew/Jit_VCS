from HEAD import current_HEAD
from  storage import find_manager
#DFS - later implementatio


def transverse(curr_Head:bytes):
    
    file1 = find_manager.location_orchestration(curr_Head ,curr_Head.decode('utf-8'))
    print(file1)
    parent = file1.parents

    if parent == []:
        return f"We found root ,{curr_Head}"
    if parent[0] ==  curr_Head:
        raise Exception("Node cannot reference itself")
    else:
        curr_Head = parent[0]
        return transverse(curr_Head)




    