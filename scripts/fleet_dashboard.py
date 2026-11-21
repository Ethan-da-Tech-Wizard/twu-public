# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Owner-only Fleet page, command reference, and interactive terminal assets.

Architecture:
    The personal Yggdrasil dashboard serves these in-memory HTML/CSS/JavaScript
    assets on Linux/example_host/macOS. The browser has no direct SSH, filesystem,
    model, or command-execution capability: all operations use the existing
    same-origin, owner-authenticated ``/api/control`` handler. ``asset`` is the
    only Python entrypoint; DashboardController supplies authorization.

Invariants:
    Search, documentation, explanation, selection, and filling a form NEVER run
    a command. Only the existing confirmed execute/PTY flows can do that.
    Reference replies must name the currently selected computer; stale or
    wrong-host replies are discarded instead of reusing another host's index.
    Documentation coverage, observed executable availability, and deterministic
    syntax explanations are different facts and remain separately labelled.
    Unknown/offline inventory is never represented as a successful local scan.

Dependencies and concurrency:
    Command-reference data comes from FleetAPI's command-catalog and
    explain-command operations. Existing access policy, pairing, phone routing,
    and terminal state are preserved. Browser request generations isolate
    overlapping reference reads; no automatic command retries are introduced.
"""

def asset(path):
    """Resolve one exact local Fleet asset without filesystem traversal.

    Args:
        path (str): Exact allowlisted /fleet or static asset route.
    Returns:
        tuple[bytes, str]: Content and MIME type, including bundled xterm assets.
    Raises:
        ValueError: The route is unknown, external, or a traversal attempt.
    Side effects:
        Imports the installed local terminal asset module only when requested;
        performs no network request, command execution, or authorization change.
    """
    raise NotImplementedError('TODO: implement')
