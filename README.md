# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/hurulsufi12-art/fix-human-sleep-patch-note/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/hurulsufi12-art/fix-human-sleep-patch-note/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep is fixed — funniest wins.

**Entry:** [Fix Human Sleep: Funniest Patch Note](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

## The patch note

> Fixed: humans no longer wake at 3 a.m. to apologize to people they haven't spoken to since 2014.

96 characters, one line, no padding. The fix is specific and unexpected: not
"sleep works now", but the exact 3 a.m. bug everyone knows — waking up to
apologize to someone you haven't spoken to in a decade.

## How it runs

`main.py` is Python 3.13 standard library only. It validates the note against
the gate (1–160 characters, single line, not whitespace-only, no control
characters) and only then writes the exact bytes to `/output/entry.txt`
— no trailing newline, no randomness, no network, no model call. An invalid
note exits non-zero and writes nothing.

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program (writes `/output/entry.txt`)
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
