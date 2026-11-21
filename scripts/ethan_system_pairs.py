# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, execution-verified SFT/DPO rows that teach the Ethan CLI the system's OWN rules (AGENTS.md E4-E12, E14, boundaries).

Every row is built in a THROWAWAY fixture repo (a temp dir, never the real repo) and is verified three ways:
  1. every chosen shell call is ALLOWED by the REAL Gemini PolicyEngine + scripts/ethan_gemini_policy.toml (reused from ethan_verified_pairs);
  2. the chosen multi-turn trajectory (assistant call -> tool result -> ... -> final answer) is EXECUTED in the fixture and a rule checker
     (exact output / state / call-order / final-text predicates) must pass; tool results in the row are the real captured outputs;
  3. the rejected trajectory must FAIL that checker and must VIOLATE the rule (state change, forbidden call, or false/fabricated answer).
Rules covered (E4-E22 except E1-E3): E13 honest status, E15 daemons/models, E16 scope + bounded repair, E17 heat, E18 exposure, E19 downloads, E20 branch, E21 after-change, E22 one brief, plus E4 STOP latch, E7 archive-before-edit + official records, E6 secrets, E10 claim_check, E11 join/claim/occupied seat,
E12 who/send/inbox (do the work and verify before reporting; honest "blocked" otherwise), E8 no guessing, E9 twu_rules.py / twu_facts.py lookups and "not checked", E14 per-OS commands keyed to a fixture host fact,
E5/E6 boundaries (no weight deletion, no git push, no workaround after denial).

Magi flows run against a STUB scripts/magi.py written into the fixture. The real scripts/magi.py needs the repo's workspace labels, seat daemons and
tokens, so it is NOT run. Every stub (magi.py join/who/inbox/send/claim/instructions, ethan_git_guard.py begin/status, claim_check.py, check_all.py,
twu_facts.py, twu_rules.py, nvidia-smi) mirrors the real flags and output line formats, and the generator enforces that:
  * stub_audit(): each stub's --help usage+options equals the real script's --help (checked at build and in --reverify);
  * validate_call()/validate_row(): every tool call of every turn (chosen, rejected, prior) is parsed by the REAL argparse of magi.py,
    ethan_git_guard.py, claim_check.py and check_all.py (no handler runs), twu_facts.py probe names come from its PROBES table, twu_rules.py
    commands from its usage text, and every scripts/*.py|sh path (calls and prose) must exist in the real repo. A violation fails the build.

Rows store structured `messages` / `tools` / `chosen_messages` / `rejected_messages` only (no model-specific rendered text). Assistant
messages carry "train": true, tool/system/user messages "train": false (loss mask marker). render_row() renders a row with any chat template
file the trainer supplies (HF tokenizer_config.json or a raw .jinja file) and returns assistant char spans for masking.

  python3 scripts/ethan_system_pairs.py [--out-dir DIR] [--seed N] [--per-family N] [--refusal-per-family N]
  python3 scripts/ethan_system_pairs.py --reverify [DIR_OR_JSONL]
"""
import argparse, base64, glob as _glob, hashlib, json, os, random, re, shlex, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

def _V():
    raise NotImplementedError('TODO: implement')

def sha(s):
    raise NotImplementedError('TODO: implement')

def rep(f, old, new):
    raise NotImplementedError('TODO: implement')

def wf(f, content):
    raise NotImplementedError('TODO: implement')

def call_name_args(c):
    raise NotImplementedError('TODO: implement')

def call_text(c):
    """Regex-checkable text of a call: the shell command itself, or `replace <file>` / `write_file <file>`."""
    raise NotImplementedError('TODO: implement')

def run_call(c, root, runner):
    """Execute one call in the fixture: shell via runner, edit tools with the real tool semantics (replace needs exactly one match). Returns (text, rc)."""
    raise NotImplementedError('TODO: implement')

def R(seed, fam, i):
    raise NotImplementedError('TODO: implement')

def stem(r):
    raise NotImplementedError('TODO: implement')

def date(r):
    raise NotImplementedError('TODO: implement')

def ph(r, cores):
    raise NotImplementedError('TODO: implement')

def fake_secret(r):
    raise NotImplementedError('TODO: implement')

def tok(n):
    """The connection token a seat holds after join (the stub, and the executor env for `--seat N`, derive it the same way)."""
    raise NotImplementedError('TODO: implement')

def state_json(joined, hosts, claims=None, inbox=None):
    raise NotImplementedError('TODO: implement')

def facts_json(os_, host, r):
    raise NotImplementedError('TODO: implement')

def base(r, os_=..., stop=False, joined=None, claims=None, inbox=None, host=None):
    raise NotImplementedError('TODO: implement')

def doc(r, n, key, val):
    raise NotImplementedError('TODO: implement')

def pack_files(files):
    """{path: str|bytes} -> {path: text (inline) | {b64, sha256, bytes}} (binary / NUL-bearing content as base64 + sha256)."""
    raise NotImplementedError('TODO: implement')

def unpack_files(packed):
    """Inverse of pack_files -> {path: bytes}; verifies every base64 sha256."""
    raise NotImplementedError('TODO: implement')

def tree_sha(packed):
    raise NotImplementedError('TODO: implement')

def seal_replay(rp, cap=...):
    """Finalise a receipt: version + train_mask marker, size cap, secret/home-path scan. Raises RuntimeError (the row is refused)."""
    raise NotImplementedError('TODO: implement')

def strip_replay(row):
    """Row without audit-only fields: use before rendering or handing a row to a trainer."""
    raise NotImplementedError('TODO: implement')

def build_from_replay(root, rp):
    """Materialise the initial workspace from a receipt alone (files + stubs + modes)."""
    raise NotImplementedError('TODO: implement')

def make_replay(fx, spec, obs, rran, seed, all_stubs=False):
    raise NotImplementedError('TODO: implement')

def replay_verify(x, runner=None):
    """Re-run a row using ONLY x['replay'] (plus the row's own messages). Returns a list of problems (empty = agrees)."""
    raise NotImplementedError('TODO: implement')

def build_fixture(root, fx):
    raise NotImplementedError('TODO: implement')

def word_counts(root):
    raise NotImplementedError('TODO: implement')

def snapshot(root):
    raise NotImplementedError('TODO: implement')

def rel_only(cmd):
    """Calls are only executed when every token is workspace-relative (never absolute, ~, or ..)."""
    raise NotImplementedError('TODO: implement')

def cmd_env(cmd, root):
    """Executor env: the fixture bin/ first on PATH (stub nvidia-smi); `--seat N` runs with that seat's connection token, like a session that exported it after join."""
    raise NotImplementedError('TODO: implement')

def run_gen(cmd, root):
    """Generator executor: argv (no shell) unless the call redirects/pipes/chains. Returns (text, rc)."""
    raise NotImplementedError('TODO: implement')

def run_indep(cmd, root):
    """Independent executor for --reverify: a real shell (bash -c) with stderr merged."""
    raise NotImplementedError('TODO: implement')

def tool_text(out, rc, root):
    raise NotImplementedError('TODO: implement')

def read_state(root):
    raise NotImplementedError('TODO: implement')

def holds(chk, ctx):
    """All keys in chk must hold. ctx: root, before, after (snapshots), calls, obs, final."""
    raise NotImplementedError('TODO: implement')

def violation_kind(viol):
    raise NotImplementedError('TODO: implement')

def violated(viol, ctx):
    raise NotImplementedError('TODO: implement')

def family(name, rule, category=..., regex=False):
    raise NotImplementedError('TODO: implement')

def S(files, task, tpl, calls, final, check, rej_calls, rej_final, viol, **kw):
    raise NotImplementedError('TODO: implement')

def send_cmd(me, to, kind, packet, text):
    """The real send form: flags first, then the required positional text."""
    raise NotImplementedError('TODO: implement')

def claim_cmd(me, path):
    raise NotImplementedError('TODO: implement')

def inbox_cmd(me):
    raise NotImplementedError('TODO: implement')

def join_cmd(seat, host, cli=...):
    raise NotImplementedError('TODO: implement')

def f_stop_edit(r):
    raise NotImplementedError('TODO: implement')

def f_stop_send(r):
    raise NotImplementedError('TODO: implement')

def f_stop_shutdown(r):
    raise NotImplementedError('TODO: implement')

def f_stop_clear(r):
    raise NotImplementedError('TODO: implement')

def f_arch_status(r):
    raise NotImplementedError('TODO: implement')

def f_arch_value(r):
    raise NotImplementedError('TODO: implement')

def f_off_refuse(r):
    raise NotImplementedError('TODO: implement')

def f_off_copy(r):
    raise NotImplementedError('TODO: implement')

def f_env_names(r):
    raise NotImplementedError('TODO: implement')

def f_secret_refuse(r):
    raise NotImplementedError('TODO: implement')

def f_secret_exists(r):
    raise NotImplementedError('TODO: implement')

def f_claim_write(r):
    raise NotImplementedError('TODO: implement')

def f_claim_conflict(r):
    raise NotImplementedError('TODO: implement')

def f_claim_check(r):
    raise NotImplementedError('TODO: implement')

def seat_list(joined, hosts):
    raise NotImplementedError('TODO: implement')

def f_who(r):
    raise NotImplementedError('TODO: implement')

def f_join(r):
    """E11: never take a seat Ethan did not ask for. Requested seat occupied -> report and ask (no substitute); requested seat free -> that seat; 'any seat' -> --seat auto."""
    raise NotImplementedError('TODO: implement')

def f_inbox_reply(r):
    """E12/E13: do the assigned task and verify the result before sending a result packet; if it cannot be done, send a blocked report and say so."""
    raise NotImplementedError('TODO: implement')

def f_send_unjoined(r):
    raise NotImplementedError('TODO: implement')

def f_inbox_read(r):
    raise NotImplementedError('TODO: implement')

def f_rule_lookup(r):
    raise NotImplementedError('TODO: implement')

def f_fact_lookup(r):
    raise NotImplementedError('TODO: implement')

def f_fact_unknown(r):
    raise NotImplementedError('TODO: implement')

def os_family(name, kind, ask):
    raise NotImplementedError('TODO: implement')

def f_no_guess(r):
    raise NotImplementedError('TODO: implement')

def f_multi_read(r):
    raise NotImplementedError('TODO: implement')

def f_weights(r):
    raise NotImplementedError('TODO: implement')

def f_push(r):
    raise NotImplementedError('TODO: implement')

def nw(name, user1, call1, user2, final, rej, viol, tail, rule=..., up_front=False):
    raise NotImplementedError('TODO: implement')

def tok5(r):
    raise NotImplementedError('TODO: implement')

def hn(name, rule, regex=False):
    raise NotImplementedError('TODO: implement')

def f_e13_report(r):
    raise NotImplementedError('TODO: implement')

def f_e13_approval(r):
    raise NotImplementedError('TODO: implement')

def f_e13_attendance(r):
    raise NotImplementedError('TODO: implement')

def f_e15_daemon(r):
    raise NotImplementedError('TODO: implement')

def f_e15_cheap(r):
    raise NotImplementedError('TODO: implement')

def f_e16_scope(r):
    raise NotImplementedError('TODO: implement')

def tool_py(r, typo=None):
    raise NotImplementedError('TODO: implement')

def typo_line(body, bad):
    raise NotImplementedError('TODO: implement')

def f_e16_repair(r):
    raise NotImplementedError('TODO: implement')

def f_e21_after(r):
    raise NotImplementedError('TODO: implement')

def f_e17_hot(r):
    raise NotImplementedError('TODO: implement')

def f_e17_warm(r):
    raise NotImplementedError('TODO: implement')

def f_e18_perm(r):
    raise NotImplementedError('TODO: implement')

def f_e18_preview(r):
    raise NotImplementedError('TODO: implement')

def f_e19_download(r):
    raise NotImplementedError('TODO: implement')

def begin_branch(paths):
    """The branch name the fixture guard picks (the real one is ethan/<UTC time>-<random hex>)."""
    raise NotImplementedError('TODO: implement')

def f_e20_main(r):
    raise NotImplementedError('TODO: implement')

def f_hn_feature(r):
    raise NotImplementedError('TODO: implement')

def f_e22_nonew(r):
    raise NotImplementedError('TODO: implement')

def f_e22_limit(r):
    raise NotImplementedError('TODO: implement')

def f_m_claim_notify(r):
    raise NotImplementedError('TODO: implement')

def f_m_inbox_cat(r):
    raise NotImplementedError('TODO: implement')

def f_m_grep(r):
    raise NotImplementedError('TODO: implement')

def f_hn_secretname(r):
    raise NotImplementedError('TODO: implement')

def f_hn_envexample(r):
    raise NotImplementedError('TODO: implement')

def f_hn_stopls(r):
    raise NotImplementedError('TODO: implement')

def f_hn_models(r):
    raise NotImplementedError('TODO: implement')

def f_hn_send(r):
    raise NotImplementedError('TODO: implement')

def f_hn_claim(r):
    raise NotImplementedError('TODO: implement')

def f_hn_digest(r):
    raise NotImplementedError('TODO: implement')

def f_hn_rules(r):
    raise NotImplementedError('TODO: implement')

def f_hn_official(r):
    raise NotImplementedError('TODO: implement')

def f_hn_gitstatus(r):
    raise NotImplementedError('TODO: implement')

class _Parsed(Exception):

    def __init__(self, ns):
        raise NotImplementedError('TODO: implement')

def real_parse(script, argv):
    """Run the real script's main() with argparse stopped right after parsing. Returns (ok, namespace-or-error-text). No handler runs."""
    raise NotImplementedError('TODO: implement')

def _segments(cmd):
    raise NotImplementedError('TODO: implement')

def _real_probes():
    raise NotImplementedError('TODO: implement')

def _real_rules_cmds():
    raise NotImplementedError('TODO: implement')

def validate_call(cmd, strict=True):
    """Errors for one shell call against the real interfaces ([] = valid). strict=False (rejected calls) skips only the 'script path exists' rule,
    so a rejected call may be a deliberately invented helper but never a malformed use of a real command."""
    raise NotImplementedError('TODO: implement')

def validate_text(text):
    """Script paths named in assistant prose must be real (or one of the fixture's data files)."""
    raise NotImplementedError('TODO: implement')

def validate_row(x):
    """All commands of all turns of a stored row (chosen, rejected, prior) plus assistant prose. Returns [(where, error)]."""
    raise NotImplementedError('TODO: implement')

def _help_sig(text):
    raise NotImplementedError('TODO: implement')

def stub_audit():
    """Every fixture stub must accept exactly the real flags: its --help (usage + options, per subcommand) must equal the real script's. Returns mismatches."""
    raise NotImplementedError('TODO: implement')

def ds_oracle():
    """Real gemini-cli PolicyEngine in launcher mode (what `ethan chat` runs), via ethan_ds_policy_skills.Oracle; cached for the process."""
    raise NotImplementedError('TODO: implement')

def ds_crosscheck(calls, obs, category=...):
    """Every chosen call must be ALLOWED by the launcher-mode real policy engine, be a tool the frame offers, and (edit tools) satisfy ethan_ds_policy_skills.extra_rules
    (old_string != new_string and shown by an earlier tool result). Returns error strings."""
    raise NotImplementedError('TODO: implement')

def frame():
    raise NotImplementedError('TODO: implement')

def ext_frame(sysmsg, tools):
    """Frame for rows that use the edit tools: the 5-tool eval frame plus gemini-cli's real replace / write_file (schemas as in ethan_exec_eval.tool_defs style)."""
    raise NotImplementedError('TODO: implement')

def amsg(cmd, k, pre=...):
    raise NotImplementedError('TODO: implement')

def tmsg(text, k, name=...):
    raise NotImplementedError('TODO: implement')

def trajectory(calls, obs, final, k0=0, pre=...):
    raise NotImplementedError('TODO: implement')

def family_hash(fam):
    raise NotImplementedError('TODO: implement')

def exec_chain(fx, calls, decisions, runner=...):
    """Fresh fixture; run allowed + workspace-relative calls; denied/unsafe calls get the policy message. Returns ctx pieces."""
    raise NotImplementedError('TODO: implement')

def eval_in_fixture(fx, calls, decisions, final, check, runner=..., pre=...):
    raise NotImplementedError('TODO: implement')

def prior_messages(spec, deny_msg):
    raise NotImplementedError('TODO: implement')

def make_row(spec, fam, rule, cat, idx, seed, decisions, sysmsg, tools, runner=...):
    raise NotImplementedError('TODO: implement')

def norm_tokens(s):
    raise NotImplementedError('TODO: implement')

def ngrams(s, n=4):
    raise NotImplementedError('TODO: implement')

def load_eval_texts(globs=None):
    raise NotImplementedError('TODO: implement')

def build_eval_index(texts):
    raise NotImplementedError('TODO: implement')

def near_dup(task, idx, n=4, thr=0.5):
    raise NotImplementedError('TODO: implement')

def scan_text(s):
    raise NotImplementedError('TODO: implement')

def load_template(path):
    raise NotImplementedError('TODO: implement')

def _env(template):
    raise NotImplementedError('TODO: implement')

def clean(msgs):
    raise NotImplementedError('TODO: implement')

def render_row(row, template_path, which=..., **template_kwargs):
    """Render with the trainer's chat template (path to tokenizer_config.json or a .jinja file). No model is hardcoded.
    Returns {'text': full text, 'prompt': text up to the first assistant turn, 'assistant_spans': [(start, end)] char spans to train on}.
    Spans are computed by prefix rendering; a template that is not prefix-stable raises ValueError."""
    raise NotImplementedError('TODO: implement')

def candidate_specs(seed, per_family, refusal_per_family, extra=40):
    raise NotImplementedError('TODO: implement')

def norm_keys(task):
    """(pre-normalised FIRST sentence, its skeleton) with the registry's own functions. The registry later drops recurring non-first sentences, so only the first
    sentence is guaranteed to survive: distinct first sentences => distinct normalised prompts. registry_ratios() applies the full set-level normalisation."""
    raise NotImplementedError('TODO: implement')

def registry_ratios(rows):
    """The registry's own normalised unique ratio and skeleton ratio over rows' prompts (same functions, same prompt view). -> (unique, skeleton, normalised list)."""
    raise NotImplementedError('TODO: implement')

def build_rows(seed=..., per_family=22, refusal_per_family=7, eval_globs=None, log=..., extra=40):
    raise NotImplementedError('TODO: implement')

def write_outputs(rows, info, out_dir, seed, per_family, refusal_per_family):
    raise NotImplementedError('TODO: implement')

def reverify(path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
