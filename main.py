"""Frost Dog Reviews Mailman — writes one dog review of the mailman.

The review is a single line, well under the 200-character gate, written
verbatim to entry.txt. No network, no third-party packages.
"""

import os

LINE = "One star: he bribes me with a biscuit every morning, then looks betrayed when I bark for a second one. Buddy, you set the price."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
