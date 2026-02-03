

def serialization(CommitData):

    lines =[]

    lines.append("commit-v1")

    if not CommitData.parents:
        lines.append("parent NONE")
    else:
        for parent_oid in CommitData.parents:
            lines.append(f"parent {parent_oid}")

    lines.append(f"state {CommitData.state_hash}")
    lines.append(f"time {CommitData.timestamp}")

    serialized = "\n".join(lines).encode("utf-8")

    return serialized




