import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

FILE_PATH = Path(os.getenv("FILE_PATH"))


def normalize_oid(oid):

    if isinstance(oid, str):
        return bytes.fromhex(oid)

    if isinstance(oid, bytes) and len(oid) == 64:
        return bytes.fromhex(oid.decode())

    return oid


def paths_for_oid(oid) -> tuple[Path, Path]:

    oid = normalize_oid(oid)

    oid_hex = oid.hex()

    shard_folder = FILE_PATH / oid_hex[:2]
    file_path = shard_folder / oid_hex[2:]

    return shard_folder, file_path


def exist(oid) -> bool:

    _, file_path = paths_for_oid(oid)

    return file_path.exists()


def storage(oid: bytes, serialised_data: bytes):

    shard_folder, file_path = paths_for_oid(oid)

    shard_folder.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        raise Exception(f"Commit {oid.hex()} already exists")

    with open(file_path, "xb") as file:
        file.write(serialised_data)


def read(oid) -> bytes:

    _, file_path = paths_for_oid(oid)

    if not file_path.exists():
        raise Exception(f"file with OID {oid} does not exist")

    return file_path.read_bytes()