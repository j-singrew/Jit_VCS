import shutil
from pathlib import Path
import os
from pathlib import Path

FILE_PATH = Path(os.getenv("FILE_PATH"))
shutil.rmtree(FILE_PATH)  # deletes folder completely
FILE_PATH.mkdir(parents=True, exist_ok=True)  # recreate empty folder
