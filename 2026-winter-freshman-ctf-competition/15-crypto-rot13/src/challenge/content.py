"""Attachment pool builder for the ROT13 challenge (no image, no container)."""

from __future__ import annotations

import codecs

FILENAME = "note.txt"
MIMETYPE = "text/plain; charset=utf-8"

_LINE_1 = "Gurfr pvcuref ner $< Nice today?"
_LINE_3 = "Hint: the ancient roman general loved shifting letters."


def build(flag: str) -> bytes:
    """Return one pool note with its flag ROT13-encoded."""

    secret = codecs.encode(f"The secret code is {flag}", "rot_13")
    return ("\r\n".join([_LINE_1, secret, _LINE_3]) + "\r\n").encode("utf-8")
