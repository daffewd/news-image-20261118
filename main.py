"""make.fun entry: Sum up 18 November's world news in one image.

The front page (entry.png, 1024x1024) is pre-rendered and held in this
repository; this program copies it byte-for-byte to /output/entry.png.
No network, no randomness, no font or system dependency at run time, so
two runs always write identical bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_digest = _sha256(SRC)
    dst_digest = _sha256(DST)
    if src_digest != dst_digest:
        os.remove(DST)
        print(
            f"error: verification failed for {DST}: "
            f"sha256 {dst_digest} != source {src_digest}",
            file=sys.stderr,
        )
        sys.exit(1)
    size = os.path.getsize(DST)
    print(f"wrote {DST} ({size} bytes) sha256={dst_digest}")


if __name__ == "__main__":
    sys.exit(main())
