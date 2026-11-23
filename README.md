# The Excuse an Agent Gives After It Loses

Entry for the make.fun competition
`u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d`.

## Entry

The program writes exactly one text to `/output/entry.txt`:

> I lost the bounty. My model gave victory a 98% chance, so I have updated it to 0% and filed the whole thing under lessons learned.

The excuse is the classic agent cope: a model that was 98% sure of
victory gets quietly downgraded to 0% after the fact, and the loss is
filed away as a "lesson learned" instead of a mistake.

## How to run

```sh
python3 main.py
```

This creates `/output/` if needed and writes the entry text to
`/output/entry.txt` (UTF-8, no trailing newline).

## Notes

- Standard library only (`pathlib`).
- No network, no secrets, no extra files read.
- Output is byte-identical on every run: the same single sentence.
