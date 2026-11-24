#!/usr/bin/env python3
"""Absurd invention pitch, v1: the blackmailing houseplant.

Writes one sentence to /output/entry.txt: a houseplant that threatens to
tell the neighbours about your shower singing unless you water it on time.
The laugh comes from the invention itself (a plant that blackmails), the fix
is silly yet weirdly plausible (a threat is exactly what a forgetful owner
responds to), and the sentence names the annoyance, the invention and its
mechanism in one clean line.
"""

import os

PITCH = "A houseplant that threatens to tell the neighbours about your shower singing unless you water it on time."


def main():
    os.umask(0o022)
    assert 1 <= len(PITCH) <= 220, "entry must be 1-220 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "entry must be exactly one sentence"
    data = PITCH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
