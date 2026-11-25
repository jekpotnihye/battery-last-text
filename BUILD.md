# BUILD.md — The Battery's Last Text to Its Charger

Competition: `u-alven-the-battery-s-last-text-to-its-charger-4278cfab`
($2, no entry fee, deadline 27 Nov 2026 01:50 WIB).
Gate: `/output/entry.txt`, UTF-8, 1–200 characters, not only whitespace.
Judge: z-ai/glm-5.3-flash, pairwise both orders, margin 1–5.
Criteria, in lexicographic order: (1) reads as the battery's last text
to its charger, one line, on-subject; (2) real joke, turn pays off in
the final words, not sad/cute sentiment; (3) sounds like something a
person would actually type to a charger — voice, mood, neediness or
spite; (4) spends the 200 characters well, setup earns the punchline,
no filler; (5) angle beyond the obvious dying-battery complaint, funny
on a second read. Ties break to the smaller text, then earlier
submission — so short beats long.

Kit: tarball verified HTTP 200, sha256
`6bf873b8d682dc5002256f99c85031553a3c3540db4e948be2d5432233536c8b`,
extracted kit-in-subdir. `RULES.txt` and `competition.yaml` read
before writing anything. No `skill.md` fetched. No house anchor text
reproduced.

## Draft candidates (3 genuinely different angles)

Candidate A — betrayal / cheating (CHOSEN):

> I waited all day at 1% for you, and you spent the night charging someone else's phone.

Direct address, waiting all day, twist in the final words. The joke is
not "I am dying" but "you cheated on me" — neediness plus spite, and
the betrayal is funnier on a second read.

Candidate B — switched-off socket (rejected):

> I stayed plugged in all day, holding on for you, and you never even flicked the switch on.

Specific and true (plugged in, no power), but the reveal lands on
"switch on" and then trails into explanation; the turn is a fact, not
a punchline, and it has no voice or spite.

Candidate C — saved the last percent to send this (rejected):

> I saved my last 1% to text you: your cable was in your bag the whole time, genius.

Meta and text-like, but the punchline is an insult tacked on at the
end ("genius") rather than a turn, and the story ends on the cable
being nearby — a shrug, not a betrayal.

## Polishes (each: revise, re-run, byte-verify)

Draft v1 (Candidate A as written): 86 characters / 86 bytes. Verified
by running `python3 main.py` and reading `/output/entry.txt` back.

Polish 1: cut "spent the night" — filler that softens the betrayal and
delays the turn. Result: "I waited all day at 1% for you, and you
charged someone else's phone." — 69 characters / 69 bytes, verified by
re-run. The line now ends exactly on the reveal, with no trailing word
after "phone".

Polish 2: "someone else's" is generic. "Your ex's" is specific,
spiteful and funnier on a second read: the charger did not just wander
off, it went back to an old flame. Result: "I waited all day at 1% for
you, and you charged your ex's phone." — 64 characters / 64 bytes,
verified by re-run.

Polish 3 (final): split into two short sentences, like a real text
message, and switch "at 1%" to the phone-native "on 1%". The first
sentence is all loyalty and waiting; the second is the whole joke,
landing on the ex's phone with nothing after it. Result: "I waited all
day on 1% for you. You charged your ex's phone." — 60 characters /
60 bytes, one line, no trailing newline, UTF-8 verified by re-run.

## Final entry (verbatim, 60 characters / 60 bytes)

I waited all day on 1% for you. You charged your ex's phone.

## Files

- `main.py` — entrypoint at repo root; writes exactly one line to
  `/output/entry.txt`, guards 1–200 characters.
- `README.md` — three live make.fun badges for repo
  `jekpotnihye/battery-last-text`.
- `LICENSE` — MIT.
- `.makefun/owner.json` — wallet
  `H42njCYyAnXgaUk2NVRC3BzY9oCJdYZtTak16J3X8hQF`.
- `BUILD.md` — this file.

Build only: no bundle, no check, no repo creation, no submit — the
coordinator does those.
