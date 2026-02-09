from pathlib2 import Path

FILE = Path(".HEAD")


def read_head() -> bytes | None:
    if not FILE.exists():
        return None
    return bytes.fromhex(FILE.read_text().strip())


def write_head(oid: bytes) -> None:
    FILE.parent.touch(exist_ok=True)
    FILE.write_text(oid.hex())




















