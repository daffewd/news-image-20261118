"""make.fun entry: Sum up 18 November's world news in one image.

The front page (entry.png, 1024x1024) is pre-rendered and held in this
repository; this program copies it byte-for-byte to /output/entry.png.
No network, no randomness, no font or system dependency at run time, so
two runs always write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
