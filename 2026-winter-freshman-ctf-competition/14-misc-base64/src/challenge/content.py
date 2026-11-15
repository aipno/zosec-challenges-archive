"""Attachment pool builder for the Base64 challenge (no image, no container)."""

from __future__ import annotations

import base64

FILENAME = "secret.txt"
MIMETYPE = "text/plain; charset=utf-8"

_LINE_1 = "SGVsbG8gd29ybGQhIFRoaXMgaXMganVzdCBhIHRlc3Qu"
_LINE_3 = "R29vZCBsdWNrIG9uIHlvdXIgQ1RGIHByYWN0aWNlIQ=="


def build(flag: str) -> bytes:
    """Return one pool file with its flag Base64-encoded."""

    middle = base64.b64encode(flag.encode("utf-8")).decode("ascii")
    lines = [_LINE_1, middle, _LINE_3]
    return ("\r\n".join(lines) + "\r\n").encode("utf-8")
