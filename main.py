"""One Line, No Deadline Met — a single-line joke excusing a missed deadline.

The excuse: the alarms meant to wake the narrator for the deadline
unionised and went on strike, so the deadline was missed through no
fault of the narrator's own — at least, that is the story.
"""

import os

ENTRY = "I set three alarms for the deadline, and all three of them unionised and went on strike at midnight."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
