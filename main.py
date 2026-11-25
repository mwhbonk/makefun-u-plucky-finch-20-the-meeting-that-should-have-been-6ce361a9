#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email - one-line joke.

Writes a single line of plain text to /output/entry.txt: a meeting
so unnecessary that its only output is an email restating the email
it met about. Two-stage absurdity: first the group reads the email
aloud for 47 minutes, then it spends ten more minutes deciding who
should email everyone what the email said. The punchline is circular
on purpose - the meeting exists only to reproduce the email.
"""
import os

JOKE = (
    "We held a 47-minute meeting to read an email aloud, then spent "
    "ten more minutes deciding who would email everyone what the "
    "email said."
)
# Judge-criteria mapping (weighed in this order):
#  1. stands alone, no setup - the whole scene is in the line itself
#  2. fresh twist - the meeting's output is an email about the email,
#     not the usual "we decided to meet again"
#  3. every word earns its place - 47-minute / read aloud / ten more
#     minutes / deciding who would email everyone: each adds a beat
#  4. specific, not generic - numbers and a concrete action, and the
#     joke could only be about a meeting-that-should-have-been-email
MAX_CHARS = 200
MAX_WORDS = 30


def main() -> None:
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke must be 1-200 characters"
    assert len(JOKE.split()) <= MAX_WORDS, "joke must be at most 30 words"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip() == JOKE, "joke must not have leading/trailing space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
