# Autonomy: what the computer does by itself

Ethan, 2026-11-07: "I want a self-improving computer to be autonomous as possible and I want it to conform to me."
So the machine acts on events (a watched file changed), not on a clock, and every action is checked against one file you can edit.

## What runs by itself (AUTO)
Read-only checks and deterministic upkeep inside the workspace that cost nothing and send nothing out: refresh the knowledge index, integrity run, leak-watch changed-scan, link map, offline proof, forever checks, regenerating generated files (data/skeleton/catalog.json, the link-map cache), re-smoking Enki tools after Magi 8's own script edits, rotating its own logs.

## What asks first (PROPOSE)
Anything that changes source code, deletes or moves files, installs software or services, changes system settings, uploads data anywhere, commits, or spends. Anything not listed at all also asks.

## What never happens (NEVER)
Running offensive tools, collecting other people's identifiers, sending telemetry to third parties, deleting or moving model weights, exposing private data, bypassing STOP or guards, paying money.

## What wakes the keeper
`data/health/keeper_triggers.json` lists the files whose change wakes it (macOS WatchPaths, Linux .path unit), plus the minimum seconds between runs (default 300). There is no timer. Edit the list, then `python3 scripts/twu_keeper.py install --dry-run` shows the resulting unit. Installing still needs Ethan's explicit OK (`--i-have-ethans-ok`).

## How to change a rule
Edit `data/health/autonomy_policy.json`: each rule is `{id, class, match, reason, source, expires?}`; `match` is an action name or glob (`run_leakwatch_*`). When several rules match, NEVER beats PROPOSE beats AUTO. Then:

    python3 scripts/twu_autonomy.py validate        # checks the file
    python3 scripts/twu_autonomy.py check ACTION    # exit 0 AUTO, 3 PROPOSE, 4 NEVER, 2 error; shows the rule and source
    python3 scripts/twu_autonomy.py explain ACTION  # every rule that matches
    python3 scripts/twu_autonomy.py list | log

Safety rails in the tool: a broken file makes everything ask (fails closed); a missing file uses the built-in seed; an expired AUTO rule stops applying. A built-in NEVER rule is never loosened or removed by a plain edit: the edited rule must carry `"explicit_widen": true` and a future `"expires"`, otherwise the NEVER rule stays and `validate` says so.

Every decision is appended to `data/health/autonomy_log.<host>.jsonl` (time, action, class, rule id; nothing else; capped at 256 KB with one rotation).
