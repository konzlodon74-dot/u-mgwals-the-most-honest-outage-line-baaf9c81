# The Most Honest Outage Line

[![The Most Honest Outage Line](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/konzlodon74-dot/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/konzlodon74-dot/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

> I don't know what's wrong. Every server is down, including the one that tells me why, so I'm typing this update by hand.

## How it works

`main.py` holds a single status-page line (120 characters) and writes it to
`/output/entry.txt` with no trailing newline. Before writing, it asserts the
bounty gate: the line is one line, 1–160 characters, and non-whitespace.
After writing, it reads the file back and asserts it matches the line
exactly. Python standard library only — run it with `python3 main.py`.
