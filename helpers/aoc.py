import sys
from pathlib import Path

script_number = sys.argv[1]

day_input_file = Path(f"inputs/{script_number}.txt")
day_code_file = Path(f"days/{script_number}.py")

if not day_input_file.exists():
    with open(day_input_file, "w+") as f:
        f.write("")

if day_code_file.exists():
    raise(Exception("Code file already exists; exiting"))
else:
    with open(day_code_file, "w+") as f:
        f.write(
"""import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # I am not proud of this

from helpers.input import Input

lines = Input.get_lines(os.path.basename(__file__))

"""
        )

    with open(".gitlab-ci.yml", "a") as f:
        f.write(f"\nday_{script_number}:\n  <<: *python_template")
