# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Generator for the allowlist section of scripts/ethan_gemini_policy.toml.

Why a generator: Gemini CLI 0.65.0 compiles every argsPattern with JS RegExp and rejects any pattern that
matches /\\([^)]*[*+?{].*\\)[*+?{]/ (isSafeRegExp) or is longer than 2048 chars, so a quantified group such as
(...)* or (?:...)? is impossible.  The allowlist is therefore written as DENY-ONLY rules ("deny unless the
command is inside the grammar", i.e. a negative lookahead) built from unrolled optional groups with empty
alternatives.  The `ethan` launcher (scripts/ethan: ethan_guard_snapshot) copies only `deny` rules into the
admin tier, so an allowlist expressed as deny rules is the only form that survives that snapshot.

What the engine shows the rules (checked in gemini-cli 0.65.0 policy-engine):
  stableStringify(args) = {\\0"command":"<JSON text>"\\0[,\\0"dir_path":"..."\\0]}   (keys sorted, each top-level
  pair wrapped in NUL).  A raw NUL can never occur inside a JSON string value, so  "\\0  is the unambiguous end
  of the command value.  Quotes inside the command show up as  \\"  (backslash + quote), a literal backslash
  as  \\\\ , newline as  \\n .
  An `allow` rule that carries an argsPattern makes checkShellCommand() split the command with the bundled
  tree-sitter bash parser and re-check every sub-command against ALL rules (and a parse error becomes DENY in
  yolo mode).  That allow-all rule (allowRedirection = true) is emitted last.

Run:  python3 scripts/ethan_policy_gen.py --write     (splice into the toml)   |   --check   (CI: toml is current)
"""
import re
import sys
from pathlib import Path

def ci(word):
    """Case-insensitive literal (macOS volumes are case-insensitive by default)."""
    raise NotImplementedError('TODO: implement')

def lone(*alts):
    raise NotImplementedError('TODO: implement')

def opt(*alts):
    """An optional group with an empty alternative (no quantifier, so Gemini's isSafeRegExp accepts it)."""
    raise NotImplementedError('TODO: implement')

def rule(comment, pattern, message, tool=...):
    raise NotImplementedError('TODO: implement')

def pygroups(q, nl):
    """Python-source regex groups {selector: alternatives}; q is the regex for ONE python quote character, nl for a python '\\n'.
    One deny rule per group keeps every pattern under Gemini's 2048-character limit."""
    raise NotImplementedError('TODO: implement')

def build_block():
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
