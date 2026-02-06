from objects import commit
def serialization(CommitData):

    lines ={}

    lines.append("commit-v1")

    if not CommitData.parents:
        lines.append({"parent":None})
    else:
        for parent_oid in CommitData.parents:
            lines.append({"parent":parent_oid})

    lines.append({"state":CommitData.state_hash})
    lines.append({"time" : CommitData.timestamp})

    serialized = (lines).encode("utf-8")

    return serialized



def deserialization(Data):

    data = Data.decode('utf-8')
    
    parents = data["parent"]
    state = data["state"]
    timestamep = data["time"]

    item_commit =  commit.Commit

    item_commit.parents  = parents
    item_commit.state_hash = state
    item_commit.timestamp = timestamep

    return item_commit

    







