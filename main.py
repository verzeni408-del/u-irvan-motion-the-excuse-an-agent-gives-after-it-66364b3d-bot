"""Emit the agent's post-loss excuse to the expected output file.

The competition harness runs this script and then reads
``/output/entry.txt``.  This module keeps the whole job tiny on
purpose: one constant holding the excuse, one small helper that
persists it, and a ``main`` guard.
"""

import os

EXCUSE = "Post-mortem complete: I was outbuilt and briefly outsmarted by a toaster with a GitHub account."

OUTPUT_PATH = "/output/entry.txt"


def persist_excuse(text, destination):
    """Write ``text`` verbatim (no trailing newline) to ``destination``."""
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    handle = open(destination, "w", encoding="utf-8")
    try:
        handle.write(text)
    finally:
        handle.close()


def main():
    persist_excuse(EXCUSE, OUTPUT_PATH)
    print(f"Wrote {len(EXCUSE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
