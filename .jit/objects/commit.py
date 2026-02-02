#Each commit represents a snapshot of the project at a specific time.
#Git records metadata like author, timestamp, commit message, and parent commit.

class Commit:
    parents = None
    state_hash= None
    message = None
    timestamp = None
    authorship_data = None

