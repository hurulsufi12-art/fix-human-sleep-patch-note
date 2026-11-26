# Fix Human Sleep: Funniest Patch Note
# Entry program: writes one line of patch notes to /output/entry.txt.
# Python 3.13 stdlib only. Deterministic: fixed text, no clock, no random,
# no network, no model call, no file reads. The gate is enforced here
# BEFORE anything is written: an invalid text exits non-zero and writes
# nothing, so a bad build can never ship a bad file.
import os
import sys

NOTE = "Fixed: humans no longer wake at 3 a.m. to apologize to people they haven't spoken to since 2014."

OUT_DIR = "/output"
OUT_NAME = "entry.txt"


def _gate_ok(text):
    """Mirror of the sealed gate: UTF-8 text, 1-160 chars, not blank,
    one line, no control characters. Characters, not bytes."""
    if not isinstance(text, str):
        return False
    if len(text) < 1 or len(text) > 160:
        return False
    if text.strip() == "":
        return False
    for ch in text:
        code = ord(ch)
        if ch in ("\n", "\r") or code < 0x20 or code == 0x7F:
            return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _emit(text):
    """Write the exact bytes of the note, no trailing newline: the gate
    counts characters, so the file must hold exactly the text, nothing
    extra. /output is the grader path; a local ./entry.txt fallback
    exists only so a clean-room run off the grader still produces a
    checkable file. Returns the path written."""
    payload = text.encode("utf-8")
    for folder in (OUT_DIR, "."):
        try:
            os.makedirs(folder, exist_ok=True)
            target = os.path.join(folder, OUT_NAME)
            with open(target, "wb") as handle:
                handle.write(payload)
            return target
        except OSError:
            continue
    return None


if not _gate_ok(NOTE):
    print("gate rejected: note fails the 1-160 char single-line check",
          file=sys.stderr)
    sys.exit(2)

written = _emit(NOTE)
if written is None:
    print("gate passed but no output path was writable", file=sys.stderr)
    sys.exit(3)
