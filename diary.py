import os
import os.path
from datetime import datetime

current_file: str = f"/home/vanillin/.diary/{datetime.today().strftime("%Y-%m-%d")}.txt"
if not os.path.exists(current_file):
    with open("/home/vanillin/.local/diaryscript/header.txt", "r") as f:
        header = f.read()
    with open(current_file, "w") as f:
        f.write(header)
os.system(f"nvim {current_file}")
