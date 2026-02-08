from objects import commit

def serialization(CommitData:commit) ->bytes:
    lines = []

    lines.append("commit-v1")

    if CommitData.parents:
        for parent in CommitData.parents:
            lines.append(f"parent={parent}")
    else:
        lines.append("parent=")

    lines.append(f"state={CommitData.state_hash}")
    lines.append(f"time={CommitData.timestamp}")

    return "\n".join(lines).encode("utf-8")


def deserialization(data: bytes) -> commit:
    text = data.decode("utf-8")
    lines = text.splitlines()

    parents = []
    state = None
    timestamp = None

    for line in lines:
        if line.startswith("parent="):
            value = line.split("=", 1)[1]
            if value:
                parents.append(value)
        elif line.startswith("state="):
            state = line.split("=", 1)[1]
        elif line.startswith("time="):
            timestamp = int(line.split("=", 1)[1])

    item_commit = commit.Commit(
        parents=parents,
        state_hash=state,
        timestamp=timestamp
    )

    return item_commit

    







