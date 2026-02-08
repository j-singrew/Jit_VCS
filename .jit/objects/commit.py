#Each commit represents a snapshot of the project at a specific time.
#Git records metadata like author, timestamp, commit message, and parent commit.
from dataclasses import dataclass
from typing import List, Optional
@dataclass(frozen=True)
class Commit:
    parents: List[bytes]        
    state_hash: bytes             
    timestamp: int                
    message: Optional[str] = None