# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Lightweight, zero-cloud bridge allowing Gemini CLI to speak to local GGUF models.

Translates Google Gemini API requests (/v1beta/models/...:generateContent)
into standard OpenAI /v1/chat/completions for local llama-server / ModelBroker,
including tool calling (A7-BRIDGE-TOOLS-003): Gemini functionDeclarations become
OpenAI tools, model tool_calls come back as Gemini functionCall parts, and
Gemini functionResponse parts go to the model as role "tool" messages.
The backend must run with --jinja (the broker's jinja=True) for tool calls.

Usage:
  python3 scripts/gemini_broker_bridge.py --backend-port 18190 --listen-port 18195

Then point Gemini CLI to this local bridge:
  export GOOGLE_GEMINI_BASE_URL="http://127.0.0.1:18195"
  gemini -p "Hello from local model"
"""
import argparse
import ast
import builtins
import difflib
import hashlib
from http.client import IncompleteRead
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import io
import json
import keyword
import os
import platform
import re
import shlex
import select
import socket
from pathlib import Path
import sys
import symtable
import threading
import urllib.error
import urllib.parse
import urllib.request
import time
import copy
import model_context_trace
import ethan_adapter_routes as adapter_routes
import stat
from ethan_arithmetic_check import BINARY_OPERATOR_PATTERN as _BINARY_OPERATOR, ELEMENTARY_ARITHMETIC as _ELEMENTARY_ARITHMETIC, NUMBER_PATTERN as _NUMBER, is_numeric_reply, parse_arithmetic
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union

class TokenBucketLimiter:
    """Thread-safe token bucket rate limiter defending loopback brokers against flood/DoS."""

    def __init__(self, capacity: float=60.0, refill_rate: float=1.0) -> None:
        raise NotImplementedError('TODO: implement')

    def allow_request(self, cost: float=1.0) -> bool:
        raise NotImplementedError('TODO: implement')

def bridge_flag(name):
    raise NotImplementedError('TODO: implement')

def bridge_int(name):
    raise NotImplementedError('TODO: implement')

def active_flags():
    """Flag values in force right now, for run metrics (`GET /admin/flags`, startup line)."""
    raise NotImplementedError('TODO: implement')

def _bump(key, n=1):
    raise NotImplementedError('TODO: implement')

def bridge_metrics():
    raise NotImplementedError('TODO: implement')

def downstream_closed(sock):
    """Readiness plus MSG_PEEK detects EOF without consuming client bytes."""
    raise NotImplementedError('TODO: implement')

def response_socket(response):
    raise NotImplementedError('TODO: implement')

def stop_upstream_when_client_leaves(client, response, stop):
    """Event-driven stream owner: closes only this request's upstream response."""
    raise NotImplementedError('TODO: implement')

def admit_enki_request(request_path, payload, validator=None):
    """Bind canonical CLI generation to this turn's native hook receipt.

    Legacy API callers remain explicitly unmanaged. The witness uses a fixed,
    host-owned fixture path, never an arbitrary path supplied in HTTP data.
    """
    raise NotImplementedError('TODO: implement')

def to_json_schema(schema):
    """Gemini's OpenAPI-style schema (types like "OBJECT") to plain JSON Schema."""
    raise NotImplementedError('TODO: implement')

def gemini_tools_to_openai(tools):
    """Gemini tools[].functionDeclarations to OpenAI tools."""
    raise NotImplementedError('TODO: implement')

def tool_result_text(response):
    """Gemini functionResponse.response to the text a model reads; Gemini CLI wraps results as {"output": ...}."""
    raise NotImplementedError('TODO: implement')

def cap_tool_text(text, limit):
    """Keep head 60% + tail 40% of an oversized tool result with a visible, honest marker."""
    raise NotImplementedError('TODO: implement')

def dedupe_repeated_reads(messages, call_info):
    """Replace EARLIER identical read-only results (same tool, args and text) with a pointer to the later full copy.
    The latest copy stays intact, so context compaction never strands the content."""
    raise NotImplementedError('TODO: implement')

def add_knowledge(messages, block_for=None):
    """Put matching verified recipes (prompt_knowledge.py) into the system message when the last user question matches them."""
    raise NotImplementedError('TODO: implement')

def tuned_preamble():
    """Read a legacy tuning candidate; it must not replace incoming CLI instructions."""
    raise NotImplementedError('TODO: implement')

def omit_bootstrap_tree(text):
    """Remove only the recognizable CLI directory tree, before its tier-two memory."""
    raise NotImplementedError('TODO: implement')

def _normal_chat_stock_sections(text: str) -> str:
    """Keep active policies and caller context around the local everyday chat profile."""
    raise NotImplementedError('TODO: implement')

def omit_cli_inline_tool_guides(text: str, *, normal_chat=False) -> str:
    """Omit stock usage guides for unavailable tools, retaining all other bytes."""
    raise NotImplementedError('TODO: implement')

def _strip_cli_wrappers(text: str) -> str:
    """Strip Gemini CLI session/hook wrappers and evidence blocks to isolate the user's own prompt."""
    raise NotImplementedError('TODO: implement')

def local_project_request(text):
    """Scope only explicit implementation jobs that specify a local project or code file."""
    raise NotImplementedError('TODO: implement')

def local_project_followup(text, contents, current):
    """Use the coding toolset for an explicit same-file edit after one confirmed native write."""
    raise NotImplementedError('TODO: implement')

def local_project_view(payload, messages, tools):
    raise NotImplementedError('TODO: implement')

def first_project_write(payload, prompt, tools, workspace):
    """Pin only a new, explicit first file in a fresh stock coding turn."""
    raise NotImplementedError('TODO: implement')

def project_write_failure(payload):
    """Recognize a paired failed native writer receipt, keeping file contents out of status text."""
    raise NotImplementedError('TODO: implement')

def turn_tool_policy(prompt):
    """Classify the current human instruction before normalizing or attaching evidence."""
    raise NotImplementedError('TODO: implement')

def _is_inline_code_request(text: str) -> bool:
    """True when the user asks to write/show an inline code snippet, function, or algorithm in chat
    without naming any file path, script file, folder, repository, or generated artifact."""
    raise NotImplementedError('TODO: implement')

def simple_snippet_question(question):
    raise NotImplementedError('TODO: implement')

class StructuredReplyMismatch(ValueError):
    """A completed model response omitted a specific part of the authenticated request."""

def fresh_snippet_turn(contents, admitted_parts):
    """Accept a native bootstrap followed by its optional SessionStart notices."""
    raise NotImplementedError('TODO: implement')

def snippet_filter_values(question):
    raise NotImplementedError('TODO: implement')

def numeric_literals(tree):
    raise NotImplementedError('TODO: implement')

def render_snippet(data, required_values=None):
    raise NotImplementedError('TODO: implement')

def simple_teaching_question(question):
    raise NotImplementedError('TODO: implement')

def render_snippet_reply(response, required_values=None):
    """Validate a complete backend choice before exposing any of its wire format."""
    raise NotImplementedError('TODO: implement')

def _continues_lesson(question, history):
    raise NotImplementedError('TODO: implement')

def _is_chat_writing_request(text):
    """Recognize requests for text in chat; leave external actions and research to the agent."""
    raise NotImplementedError('TODO: implement')

def github_discovery_topic(prompt):
    raise NotImplementedError('TODO: implement')

def page_title_request(prompt):
    raise NotImplementedError('TODO: implement')

def page_summary_request(prompt):
    raise NotImplementedError('TODO: implement')

def cite_page_summary(completion, url, token_limit=None):
    """Attach the source to ordinary completed prose; preserve refusals, limits and errors."""
    raise NotImplementedError('TODO: implement')

def _single_public_source(prompt, pattern):
    raise NotImplementedError('TODO: implement')

def page_title_reply(payload, admission):
    """Dispatch one explicit page read. Titles come from metadata; summaries require the local model."""
    raise NotImplementedError('TODO: implement')

def github_discovery_reply(payload, admission):
    """For a simple public listing, dispatch one declared native tool and present its actual rows."""
    raise NotImplementedError('TODO: implement')

def format_public_repositories(data, topic):
    raise NotImplementedError('TODO: implement')

def visible_reader_url(prompt):
    raise NotImplementedError('TODO: implement')

def single_web_reply_url(prompt):
    raise NotImplementedError('TODO: implement')

def labeled_line_grammar(prompt):
    """Compile an explicitly requested numbered list of field labels to llama.cpp GBNF."""
    raise NotImplementedError('TODO: implement')

def arithmetic_equation(expression):
    raise NotImplementedError('TODO: implement')

def read_model_number(response):
    raise NotImplementedError('TODO: implement')

def verified_uuid_answer(response, expected):
    """Release only a model-produced UUID that agrees exactly with complete gateway evidence."""
    raise NotImplementedError('TODO: implement')

def paired_web_result(contents, names, url):
    """Match the native tool response to the exact reader operation on this turn."""
    raise NotImplementedError('TODO: implement')

def unpack_mcp_result(result):
    """Strip the native MCP envelope, retaining separately delivered hook text."""
    raise NotImplementedError('TODO: implement')

def fetched_web_evidence(result, name, url, result_cap, *, presentation=None):
    """Render the paired successful read as untrusted source text in the tool message."""
    raise NotImplementedError('TODO: implement')

def gemini_to_openai(gemini_payload, prune_preamble=False, prune_tools=False, inject_sysadmin_persona=False, allow_host_launch=False, bound_web_urls=None, presentation=None, admitted_tool_policy=None, admitted_arithmetic=None, count_only=False, admitted_inline_code=False, admitted_chat_writing=False, admitted_local_turn_parts=None, verified_page_summary=None, admitted_local_project=None, organization_preview=False):
    """Translate Gemini generateContent request body into OpenAI chat format."""
    raise NotImplementedError('TODO: implement')

def python_one_line_input(question):
    """Extract the existing input from an explicit, standalone Python one-line example."""
    raise NotImplementedError('TODO: implement')

def inline_filter_literals(action):
    """Return the explicitly requested item values, preserving quote case and order."""
    raise NotImplementedError('TODO: implement')

def delimited_fields_grammar(question, input_name):
    """Bind a declared delimiter and input type for simple per-field expressions."""
    raise NotImplementedError('TODO: implement')

def apply_inline_retry_grammar(request, input_name, question, generation_config, props):
    """Constrain only the second draft of an explicit, elementary list operation."""
    raise NotImplementedError('TODO: implement')

def bind_inline_filter_arguments(response, input_name, literals):
    """Bind only a complete, model-produced literal-membership expression."""
    raise NotImplementedError('TODO: implement')

def one_line_result_issue(statement, input_name, question):
    """Check the outer result only for simple, explicit per-item requests."""
    raise NotImplementedError('TODO: implement')

def unwrap_result_echo(response, input_name, question):
    """Keep the model's expression when a REPL-style answer binds and echoes it."""
    raise NotImplementedError('TODO: implement')

def one_line_issue(response, input_name, question, check_names=False):
    """Check only observable source constraints. Never execute a model response."""
    raise NotImplementedError('TODO: implement')

def apply_conversational_focus(openai_req, *, plain_lesson=False, chat_writing=False):
    """Append turn guidance while retaining instructions, evidence and conversation in their original roles."""
    raise NotImplementedError('TODO: implement')

def is_conversational_turn(text: str) -> bool:
    """Detect if a user turn is casual chat, greeting, identity question, inline code snippet, or explanation
    where tools should NOT be passed so the model responds naturally in English."""
    raise NotImplementedError('TODO: implement')

def clean_template_artifacts(text: str, preserve_whitespace=False) -> str:
    """Strips leaked Jinja/Qwen/Gemma chat-template tokens, thinking blocks, and preambles."""
    raise NotImplementedError('TODO: implement')

def unpack_chat_pseudo_call(text: str) -> Optional[str]:
    """If the model wrote a pseudo-tool call to 'chat' or 'reply' or 'say', extract the conversational message."""
    raise NotImplementedError('TODO: implement')

def strip_template_leak(value):
    """gpt-oss sometimes spills its own chat-template tokens (<|constrain|>, <|message|> ...) into text or tool
    arguments. Cut everything from the first such token, plus the stray JSON closers that precede it."""
    raise NotImplementedError('TODO: implement')

def _embedded_call_json(text, tool_names):
    """Prose followed by exactly one fenced/<tool_call> block (or one unambiguous standalone JSON call object)
    whose JSON is a call (or list of calls) to declared tools.
    Returns the parsed JSON or None. Zero or several blocks, other names, or non-call JSON -> None (never guess)."""
    raise NotImplementedError('TODO: implement')

def holds_embedded_call(text):
    """Streaming: with ETHAN_BRIDGE_RESCUE_EMBEDDED, keep back prose that carries a fenced/<tool_call> or single unfenced JSON call so the
    rescue can run on the whole turn (a failed rescue replays it as text, so nothing is lost)."""
    raise NotImplementedError('TODO: implement')

def _fileop_command(alias, args):
    """cp -a / mv command for a printed pseudo-call with source+destination arguments; "" when either is missing or has a '..' part."""
    raise NotImplementedError('TODO: implement')

def _repair_doubled_brace(body, tool_names):
    """The 7B sometimes opens a call with '{{"name":' (doubled brace). Drop exactly one leading brace (and one trailing
    brace if that makes it parse) and accept only a call to a declared tool; anything else -> None (never guess)."""
    raise NotImplementedError('TODO: implement')

def rescue_text_tool_calls(text, tool_names):
    """Small models often write a tool call as text (bare/fenced JSON or <tool_call>) instead of a native call.
    Translates pseudo-tool calls (e.g. make_new_folder -> run_shell_command mkdir) to valid declared tools.
    Return [{"name", "arguments"}] only if the text represents such call(s) to a declared tool; else None."""
    raise NotImplementedError('TODO: implement')

def repair_python_code(content: str, file_path: str=...) -> str:
    """If written Python code has minor formatting flaws (like decorator unindent or missing stdlib imports), repair safely."""
    raise NotImplementedError('TODO: implement')

def repair_call_args(name, args, tool_schemas, *, preserve_python_source=False):
    """Rename a wrongly-named argument to the declared one (e.g. path -> file_path) when it is unambiguous.
    Anything unclear is left as the model wrote it, so Gemini's own schema check rejects it."""
    raise NotImplementedError('TODO: implement')

def declared_tool_schemas(openai_req):
    raise NotImplementedError('TODO: implement')

def declared_tool_names(openai_req):
    raise NotImplementedError('TODO: implement')

def ensure_tool_system_prompt(openai_req, native_tools=None):
    """When tools are declared, ensure the system prompt explains the tools so models
    whose jinja template does not render tools natively (or has supports_tools=False)
    still see the exact tools and call format."""
    raise NotImplementedError('TODO: implement')

def slim_tool_rule():
    """Single-line tool rule (no leading newline). ETHAN_BRIDGE_SLIM_CALL_RULE appends the native-call sentence."""
    raise NotImplementedError('TODO: implement')

def _slim_name(header):
    raise NotImplementedError('TODO: implement')

def slim_system_prompt(text, level=1):
    """Remove prompt text the 5-tool read/edit CLI cannot use. level 0 returns text unchanged."""
    raise NotImplementedError('TODO: implement')

def _first_sentence(s, limit):
    raise NotImplementedError('TODO: implement')

def slim_tools(tools, level=2):
    """level >= 2: keep every tool name, parameter and `required`; shorten prose descriptions (never the schema)."""
    raise NotImplementedError('TODO: implement')

def _tuned_schema(schema, tool=None, path=...):
    """Shorten descriptions without removing schema constraints or reference definitions."""
    raise NotImplementedError('TODO: implement')

def tuned_tools(tools):
    """Compact tool schemas for slim level 3; names, parameter names, types and `required` are kept exactly."""
    raise NotImplementedError('TODO: implement')

def tuned_serve_view(messages, tools):
    """Use supplied governance for this session, or the tuned default for a bare request."""
    raise NotImplementedError('TODO: implement')

def apply_slim_prompt(openai_req, level=None):
    """Compact tool prose. The caller owns its system instructions, including every Markdown section."""
    raise NotImplementedError('TODO: implement')

def local_clock_now():
    """Local wall-clock time for the machine receiving this model request."""
    raise NotImplementedError('TODO: implement')

def apply_local_clock_context(openai_req, now=None):
    """Add the current host clock to system context; never change user/tool data."""
    raise NotImplementedError('TODO: implement')

def _message_text(message):
    raise NotImplementedError('TODO: implement')

def apply_user_conventions(openai_req):
    """ETHAN_BRIDGE_NORMALIZE: make the model conform to Ethan without touching what he typed.

    Runs ONLY on the OpenAI request built AFTER admit_enki_request has validated the exact Gemini prompt text and
    stripped the admission marker, so the admitted/validated text can never be altered. The user's message is never
    rewritten; a conventions line and (for the latest user turn only) a typo interpretation note are appended to
    the system message. Fail-open: any error leaves the request unchanged.
    """
    raise NotImplementedError('TODO: implement')

def apply_application_contract(openai_req):
    """Pin app identities independently of optional knowledge/host grounding."""
    raise NotImplementedError('TODO: implement')

def apply_preflight_grounding(openai_req):
    """Directly and deterministically inject host pre-flight grounding into system prompt when ETHAN_BRIDGE_GROUND=1.
    Runs after Enki admission; system message updates never invalidate prompt tokens."""
    raise NotImplementedError('TODO: implement')

def _extract_jev_user_tasks(openai_req: Dict[str, Any]) -> Tuple[str, Optional[str]]:
    """Extract (latest_user_task, prior_user_task) only when the final message is a user turn."""
    raise NotImplementedError('TODO: implement')

def cached_jev_turn(key):
    raise NotImplementedError('TODO: implement')

def reserve_jev_turn(key):
    """One judge request per admission, even with overlapping tool follow-ups."""
    raise NotImplementedError('TODO: implement')

def record_jev_turn(key, receipt):
    raise NotImplementedError('TODO: implement')

def open_local_jev(req, timeout):
    raise NotImplementedError('TODO: implement')

def apply_jev_routing(openai_req: Dict[str, Any], jev_url: Optional[str]=None, authenticated_task=None) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    """Query local Jev decision agent (`127.0.0.1:18196/v1/jev-route`) fail-open and steer deterministic sampling."""
    raise NotImplementedError('TODO: implement')

class ContextBudgetError(ValueError):
    pass

def compact_openai_context(request, token_budget, count_tokens):
    """Keep the task anchor and newest work while trimming old turns/tool output.

    System instructions and tool schemas are never removed. This is a deterministic
    recovery path for local backends whose real context is smaller than the CLI's
    advertised model limit; project files remain the durable work checkpoint.
    """
    raise NotImplementedError('TODO: implement')

def start_backend():
    """Refuse invisible model revival from a bridge request.

    A bridge request has no reliable visible user witness.  It must never turn
    a connection failure into a detached inference launch; the owner starts a
    model explicitly in a visible terminal after reviewing preflight status.
    ``MODEL_STANDBY`` remains an additional, durable stop latch.
    """
    raise NotImplementedError('TODO: implement')

def _refused(exc):
    raise NotImplementedError('TODO: implement')

def open_with_retry(req, timeout, attempts=5, start=None, wait=None):
    """gpt-oss occasionally writes a reply llama-server's parser rejects (HTTP 500 'peg-native format'). The failure is
    random, so retrying the identical request usually succeeds. Also: a model that is still loading answers 503 'Loading
    model' (wait and retry), and a model that is not running (connection refused) is started once and waited for, so the
    CLI does not have to be restarted by hand (104 'No local model answered' replies were saved before this). Any other error is raised untouched."""
    raise NotImplementedError('TODO: implement')

def call_problem(message, tool_names, tool_schemas, validate=False):
    """Exact, model-readable error text when the model's tool call cannot be used; None when it is fine.
    Always checks syntax (unparseable arguments, or a reply that is a call written as broken JSON text).
    With validate=True also checks declared name, required arguments and top-level argument types."""
    raise NotImplementedError('TODO: implement')

def tool_call_schema(openai_tools):
    """JSON schema accepting exactly one call to one declared tool: {"name": <const>, "arguments": <that tool's schema>}."""
    raise NotImplementedError('TODO: implement')

def build_reask_request(openai_req, message, error, constrained=False):
    """Original request + the bad output + the exact error; never mutates the original. Tools stay native unless
    constrained: llama-server rejects a custom grammar/json_schema together with tools ('Cannot use custom grammar
    constraints with tools.'), so the constrained variant drops tools and forces the call shape with json_schema."""
    raise NotImplementedError('TODO: implement')

def _strip_hook_context(text):
    """Exclude complete alarm blocks from intent classification; preserve other user text."""
    raise NotImplementedError('TODO: implement')

def _explanation_only(text):
    """A code example or a no-change request must not become a forced action."""
    raise NotImplementedError('TODO: implement')

def looks_like_plain_chat(openai_req, reply):
    """True when this turn is plain conversation and the text reply must be returned as-is, with NO re-ask (each re-ask costs a full
    5-12k token prompt re-process, about 75-185 s on the Mac). Decision rule, all must hold:
      1. ETHAN_BRIDGE_REASK_PLAIN is off (set it to 1 to restore the old behaviour);
      2. the reply has non-empty text and no tool call;
      3. no tool result exists anywhere in the request (a turn mid-task is never plain chat);
      4. the user's OWN words (injected <tag>...</tag> context blocks such as hook_context removed, so words like "files" or "report"
         inside them cannot fake an action) are 1-200 chars with no action/build/write/destructive verb, no file or folder noun,
         and nothing path-like (a slash, tilde, backslash or .ext).
    Anything else (read/edit/run/make something, tools in play) keeps the existing re-ask safety net. Never raises."""
    raise NotImplementedError('TODO: implement')

def message_has_call(message):
    raise NotImplementedError('TODO: implement')

def no_tool_problem(openai_req, message, tool_names):
    """Dogfood fix (flag ETHAN_BRIDGE_REASK_NO_TOOL, default off): the model answered a file/folder task from memory with no tool call and no
    tool result exists yet in the conversation. Returns the re-ask text, or None. Destructive requests are never nudged (a refusal needs no tool)."""
    raise NotImplementedError('TODO: implement')

def partial_reads_problem(openai_req, message, tool_names):
    """Flag ETHAN_BRIDGE_REASK_PARTIAL_READS (default off): the user named 2+ distinct files, the model replies in text (no tool call)
    after reading only some. Returns the re-ask text naming the unread files, or None. Never for write/delete requests."""
    raise NotImplementedError('TODO: implement')

def refusal_problem(openai_req, message, tool_names):
    """Flag ETHAN_BRIDGE_REASK_REFUSAL (default off). A buildable job (code/write/make/spreadsheets/presentation ...) got a reply with NO tool call that is
    (a) a canned refusal, (b) a how-to walkthrough before any tool ran, (c) "Let's ..." prose mid-job, (d) any text right after a script was written but
    never run (so "done" would be invented), or (e) "done" after one file for a request that names a second deliverable.
    Returns the re-ask text or None. Destructive requests are never nudged; a reply with a tool call is never a problem."""
    raise NotImplementedError('TODO: implement')

def _toolcall_rescue(openai_req, response_json, tool_names, tool_schemas):
    """Flag ETHAN_BRIDGE_TOOLCALL_RESCUE: a deterministic repair of a reply that has no valid tool call. Returns a corrected
    response (message.tool_calls set) or None. Never raises; every decision is logged by ethan_toolcall_rescue itself."""
    raise NotImplementedError('TODO: implement')

def is_inline_xml_call(openai_req, message):
    """Recognize malformed model markup for a chat-only inline-code request."""
    raise NotImplementedError('TODO: implement')

def retry_inline_xml_call(openai_req, response_json, tool_names, post):
    """Recover a malformed pseudo-call once; never execute model-printed text."""
    raise NotImplementedError('TODO: implement')

def reask_once(openai_req, response_json, tool_names, tool_schemas, post):
    """At most ONE re-ask. `post(request_dict)` returns a parsed OpenAI response or raises. Returns the response to use:
    the corrected one when it is free of problems, otherwise the original (the caller then reports as before)."""
    raise NotImplementedError('TODO: implement')

def openai_to_gemini(openai_response, model_name=..., tool_names=None, tool_schemas=None, bound_web_urls=None, *, literal_text=False, preserve_python_source=False):
    """Translate OpenAI chat completion result back into Gemini candidate format."""
    raise NotImplementedError('TODO: implement')

def is_router_classifier(gemini_payload):
    """Gemini CLI's model-routing classifier: the bridge answers it itself, since one local model serves all routes."""
    raise NotImplementedError('TODO: implement')

def text_reply(text, model_name):
    raise NotImplementedError('TODO: implement')

class _NoMetadataRedirect(urllib.request.HTTPRedirectHandler):

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise NotImplementedError('TODO: implement')

def observe_backend_identity(backend_url, api_key=...):
    """Read running llama-server metadata; saved profiles are never runtime evidence."""
    raise NotImplementedError('TODO: implement')

def cached_file_sha256(path):
    """Return (sha256|None, status). Hashing runs once per (path, mtime, size) in a background thread so /health
    never blocks on a multi-GB model; status is measured | hashing | unreadable."""
    raise NotImplementedError('TODO: implement')

def routing_file_hash(path, deadline=None):
    raise NotImplementedError('TODO: implement')

def observe_backend_adapters(backend_url, api_key=...):
    """Read GET /lora-adapters (read-only). status: observed_none | observed_active | unobservable.
    Anything that is not a clean list is 'unobservable', never 'none'."""
    raise NotImplementedError('TODO: implement')

def adapter_health_fields(observed):
    """Health fields for adapter identity. adapter_name is null only when observed none; 'unobservable' otherwise."""
    raise NotImplementedError('TODO: implement')

def refresh_identity_cache(backend_url, api_key=...):
    """Called by /health and a background refresher (never from the request path)."""
    raise NotImplementedError('TODO: implement')

def identity_headers(max_age=60.0):
    """Response headers naming the model and adapter that serve this bridge. Cache only; no network per request."""
    raise NotImplementedError('TODO: implement')

def _identity_refresher(backend_url, api_key, period=5.0):
    raise NotImplementedError('TODO: implement')

class GeminiBridgeHandler(BaseHTTPRequestHandler):

    @classmethod
    def set_backend_port(cls, port: int):
        raise NotImplementedError('TODO: implement')

    @classmethod
    def get_backend_port(cls) -> int:
        raise NotImplementedError('TODO: implement')

    @classmethod
    def get_backend_url(cls) -> str:
        raise NotImplementedError('TODO: implement')

    def response_identity(self):
        raise NotImplementedError('TODO: implement')

    def reask_post(self, request):
        """Bounded one-shot upstream call for a re-ask; the caller already holds MODEL_REQUEST_GATE."""
        raise NotImplementedError('TODO: implement')

    def setup(self):
        raise NotImplementedError('TODO: implement')

    def send_json(self, status, payload, stream=False):
        raise NotImplementedError('TODO: implement')

    def do_GET(self):
        """Handle health check or model discovery."""
        raise NotImplementedError('TODO: implement')

    def do_POST(self):
        """Translate generateContent/streamGenerateContent call to backend and return Gemini response."""
        raise NotImplementedError('TODO: implement')

    def count_tokens(self, gemini_req):
        """Count the supplied prompt with the active local template and tokenizer."""
        raise NotImplementedError('TODO: implement')

    def backend_template_api(self, path, payload=None):
        raise NotImplementedError('TODO: implement')

    def compact_for_backend(self, openai_req, props=None):
        """Fit the rendered input and a bounded reply in the same model slot."""
        raise NotImplementedError('TODO: implement')

    def handle_one_request(self):
        raise NotImplementedError('TODO: implement')

    def log_message(self, format, *args):
        raise NotImplementedError('TODO: implement')

def run_bridge(listen_port=18195, backend_port=18190, api_key=..., prune_preamble=True, prune_tools=False, no_thinking=True, listener=None):
    raise NotImplementedError('TODO: implement')
