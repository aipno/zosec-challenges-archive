"""Attachment pool builder for the XOR challenge (no image, no container)."""

from __future__ import annotations

FILENAME = "encrypted.bin"
MIMETYPE = "application/octet-stream"
KEY = 0x2A


def build(flag: str) -> bytes:
    """XOR one pool flag with the same single-byte key as the original."""

    return bytes(byte ^ KEY for byte in flag.encode("utf-8"))
