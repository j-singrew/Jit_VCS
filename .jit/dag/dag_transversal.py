from HEAD import current_HEAD
from  storage import find_manager
#DFS - later implementatio


def transverse(byte_oid,oid):
    curr_Head = current_HEAD.read_head()
    print(curr_Head)
    file1 = find_manager.location_orchestration(byte_oid,oid)
    #print(file1)


    