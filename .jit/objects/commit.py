#Each commit represents a snapshot of the project at a specific time.
#Git records metadata like author, timestamp, commit message, and parent commit.

class Commit:
    parent_reference = None
    state = None
    message = None
    timestamps = None
    authorship_data = None
