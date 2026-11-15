"""Attachment pool builder for the fake-PNG challenge (no image, no container)."""

from __future__ import annotations

FILENAME = "image.png"
MIMETYPE = "image/png"

# A real PNG starts with this signature.  The rest is deliberately not a
# valid image: the flag is plain text after the signature.
_SIGNATURE = b"\x89PNG\r\n\x1a\n"
_PADDING = b"fake png data padding padding\n"
_TRAILER = b"\nmore padding data here\n"


def build(flag: str) -> bytes:
    """Return a fake PNG whose only useful content is the embedded flag."""

    return _SIGNATURE + _PADDING + flag.encode("utf-8") + _TRAILER
