from pathlib2 import Path
from typing import Optional

FILE = Path("./HEAD/.HEAD")


def read_head() -> Optional[bytes]:
    if not FILE.exists():
        return None
    content = FILE.read_text().strip()
    if not content:  
        return None
    return bytes.fromhex(content)

def write_head(oid: bytes) -> None:
    FILE.parent.mkdir(parents=True, exist_ok=True)
    print("This is current head in hea",(oid.hex().lower()))
    FILE.write_text(oid.hex().lower())




















