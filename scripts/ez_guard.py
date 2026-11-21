# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ez_guard.py: Dual-Sovereignty Engine & Multi-Signature Gatekeeper.

PROGRAM: scripts/ez_guard.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE: Owns the 2-of-2 signing gate for destructive actions. Keys are generated
  per installation (random, mode 0600, outside the repo; see guard_key_dir) so the
  open-source code contains nothing that can forge a signature. Upstream: none;
  downstream: scripts/test_ez_guard.py, scripts/test_ez_guard_keys.py.
  Layers, bottom to top: key storage -> sign/verify helpers -> destructive-action
  classifier -> MultiSigGate (2-of-2 decision) -> DualSovereigntyEngine (revocation
  rules) -> CensusValidator (peer allow-list) -> EZGuard facade -> small CLI.
  Invariants: both sovereign ids are fixed; a sovereign key can never be revoked;
  a destructive action is allowed only with valid signatures from both sovereigns
  over the exact action bytes (plus nonce, when given); nonces are single-use.
  Side effects: first use creates key files in guard_key_dir(); logging to stderr.
  Ed25519 (via `cryptography`) is used when installed; otherwise an HMAC-SHA256
  fallback keyed by the secret seed is used (same call surface, symmetric).
CHANGE HISTORY: 2026-11-21 replaced fixed public genesis seeds (EZ_AUDIT item 3).

Production dual-sovereignty enforcement engine for both sovereigns.

Invariants & Core Features:
1. Permanent Genesis Keys: Cryptographically anchored genesis keys for First sovereign
   and Second sovereign.
2. Mathematical Enforcement: Absolute mathematical rejection of unilateral revocation of
   either sovereign key (anti-lockout invariant).
3. 2-of-2 Multi-Signature Gate: Intercepts destructive actions (e.g. `rm -rf`, `wipe`, `format`,
   `dd if=`, `delete_repo`) requiring cryptographic verification from BOTH sovereigns.
4. Census Validator: Cryptographically verifies peer identities; drops and rejects all
   unverified peer keys from the network and execution pipelines.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import hmac
import json
import logging
import os
from pathlib import Path
import re
import stat
import sys
from typing import Any, Dict, List, Optional, Set, Tuple, Union

class EZGuardError(Exception):
    """Base exception for EZ Guard dual-sovereignty enforcement."""

class UnilateralRevocationError(EZGuardError):
    """Raised when unilateral revocation of a sovereign genesis key is attempted."""

class SovereignImmutableError(EZGuardError):
    """Raised when any revocation of an immutable genesis key is attempted."""

class DestructiveActionBlockedError(EZGuardError):
    """Raised when a destructive action is blocked due to missing or invalid 2-of-2 signatures."""

class UnverifiedPeerError(EZGuardError):
    """Raised when an unverified peer key is rejected or dropped."""

class InvalidSignatureError(EZGuardError):
    """Raised when cryptographic signature verification fails."""

def guard_key_dir() -> Path:
    """Return the directory holding the per-install seeds (never inside the repo).

    Returns:
        Path from $EZ_GUARD_KEY_DIR if set, else ~/.local/state/ez-guard.
    """
    raise NotImplementedError('TODO: implement')

def _load_or_create_seed(identity: str) -> bytes:
    """Load (or on first use create) the secret seed for one sovereign.

    Args:
        identity: canonical sovereign id (FIRST_ID or SECOND_ID).

    Returns:
        32 secret bytes.

    Raises:
        EZGuardError: the key file is not owner-only (0600), is not a regular
            file, or has the wrong length; refusing is safer than trusting it.
    """
    raise NotImplementedError('TODO: implement')

def _seed_for(identity: str) -> bytes:
    """Secret seed for a canonical sovereign id (lazy; see _load_or_create_seed).

    Args:
        identity: canonical sovereign id.

    Returns:
        32 secret bytes.

    Raises:
        EZGuardError: propagated from _load_or_create_seed on a bad key file.
    """
    raise NotImplementedError('TODO: implement')

def _privkey_for(identity: str):
    """Ed25519 private key object for a sovereign (None when `cryptography` is absent).

    Args:
        identity: canonical sovereign id.

    Returns:
        An Ed25519PrivateKey built from the stored seed, or None in fallback mode.
    """
    raise NotImplementedError('TODO: implement')

def _pubkey_hex_for(identity: str) -> str:
    """Public key hex for a sovereign; a one-way hash of the secret seed in fallback mode.

    Args:
        identity: canonical sovereign id.

    Returns:
        64 hex characters. In fallback mode this is only an identifier (HMAC has
        no real public key), not something that can verify signatures.
    """
    raise NotImplementedError('TODO: implement')

def _genesis_keys() -> Dict[str, str]:
    """Map of sovereign id -> public key hex for this installation.

    Returns:
        Dict with exactly FIRST_ID and SECOND_ID keys. Creates seeds on first call.
    """
    raise NotImplementedError('TODO: implement')

def __getattr__(name: str):
    """Lazy module attributes (PEP 562): genesis public keys exist only once asked for.

    Keeps `from ez_guard import FIRST_GENESIS_PUBKEY` working without generating
    or reading keys at import time.

    Args:
        name: attribute being looked up on the module.

    Returns:
        The public key hex (FIRST/SECOND_GENESIS_PUBKEY) or the GENESIS_KEYS dict.

    Raises:
        AttributeError: for any other name, as Python expects from __getattr__.
    """
    raise NotImplementedError('TODO: implement')

def normalize_identity(identifier: str) -> str:
    """Normalizes aliases to canonical sovereign ID or returns raw peer identifier.

    Args:
        identifier: any id or alias (case-insensitive for the alias match).

    Returns:
        FIRST_ID or SECOND_ID for a known alias, else the stripped input unchanged
        (case preserved, since ordinary peer ids are case-sensitive).
    """
    raise NotImplementedError('TODO: implement')

def is_sovereign_identity(identifier: str) -> bool:
    """Checks if an identity maps to either sovereign.

    Args:
        identifier: id or alias.

    Returns:
        True when normalize_identity() yields a member of SOVEREIGN_IDS.
    """
    raise NotImplementedError('TODO: implement')

def canonical_action_bytes(action: Union[str, Dict[str, Any]], nonce: Optional[str]=None) -> bytes:
    """Converts command string or structured action payload into deterministic bytes.

    Signer and verifier must produce identical bytes, so dicts are serialised with
    sorted keys and compact separators; strings are stripped. The nonce is folded
    into the signed bytes, which is what makes a signature single-purpose.

    Args:
        action: shell command string or structured action dict.
        nonce: optional single-use token bound into the bytes.

    Returns:
        UTF-8 bytes to sign or verify.
    """
    raise NotImplementedError('TODO: implement')

def sign_payload(identity: str, action: Union[str, Dict[str, Any]], nonce: Optional[str]=None) -> str:
    """Signs an action payload using the sovereign private key.

    Args:
        identity: sovereign id or alias.
        action: command string or action dict (see canonical_action_bytes).
        nonce: optional single-use token bound into the signature.

    Returns:
        Signature hex (Ed25519, or HMAC-SHA256 hex in fallback mode).

    Raises:
        ValueError: identity is not a sovereign.
        EZGuardError: seed file unsafe (from key loading).
    Side effects: may create the seed file on first use.
    """
    raise NotImplementedError('TODO: implement')

def verify_signature(identity: str, action: Union[str, Dict[str, Any]], signature_hex: str, nonce: Optional[str]=None, pubkey_hex: Optional[str]=None) -> bool:
    """Verifies cryptographic signature against sovereign genesis key or specified public key.

    Args:
        identity: sovereign id/alias (or a peer id when pubkey_hex is given).
        action: the exact command/dict that was signed.
        signature_hex: hex signature to check.
        nonce: nonce that was bound at signing time, if any.
        pubkey_hex: explicit public key; default is the sovereign's own key.

    Returns:
        True only when the signature is valid; every failure returns False
        (this function does not raise on malformed input).
    """
    raise NotImplementedError('TODO: implement')

def is_destructive_action(action: Union[str, Dict[str, Any]]) -> Tuple[bool, str]:
    """Detects whether an action or shell command represents a destructive operation.

    Args:
        action: shell command string or structured action dict.

    Returns:
        (is_destructive: bool, reason: str)
    """
    raise NotImplementedError('TODO: implement')

@dataclass
class GateResult:
    """Outcome of one MultiSigGate evaluation.

    Attributes:
        allowed: True if the action may proceed.
        requires_multisig: True if the action was classified destructive.
        reason: human-readable explanation (tests match on some of this text).
        first_verified / second_verified: whether each sovereign's signature checked out.
        timestamp: UTC ISO time the result was created.
    """

class MultiSigGate:
    """2-of-2 Multi-Signature Gate intercepting destructive actions."""

    def __init__(self, replay_cache_size: int=1000):
        """Create a gate with an empty in-memory replay (used-nonce) set.

        Args:
            replay_cache_size: max remembered nonces before the set is cleared.
        """
        raise NotImplementedError('TODO: implement')

    def evaluate(self, action: Union[str, Dict[str, Any]], signatures: Optional[Dict[str, str]]=None, nonce: Optional[str]=None) -> GateResult:
        """Evaluates an action against the 2-of-2 dual-sovereignty gate.

        Args:
            action: command string or action dict.
            signatures: map of sovereign id or alias -> signature hex.
            nonce: optional single-use token; must match what was signed.

        Returns:
            GateResult. Non-destructive actions are allowed immediately. Destructive
            ones are allowed only when both signatures verify and the nonce is unused.

        Side effects: on success with a nonce, records it (not thread-safe; no lock).
        """
        raise NotImplementedError('TODO: implement')

    def enforce(self, action: Union[str, Dict[str, Any]], signatures: Optional[Dict[str, str]]=None, nonce: Optional[str]=None) -> GateResult:
        """Enforces 2-of-2 gate and raises DestructiveActionBlockedError if blocked.

        Args:
            action, signatures, nonce: as for evaluate().

        Returns:
            The allowed GateResult.

        Raises:
            DestructiveActionBlockedError: the gate did not allow the action.
        """
        raise NotImplementedError('TODO: implement')

class DualSovereigntyEngine:
    """Production Dual-Sovereignty Engine.

    Guarantees mathematical parity between both sovereigns:
    - Sovereign keys are permanent genesis anchors.
    - Mathematical enforcement strictly rejects unilateral revocation of either sovereign.
    - Prevents single-party lockout or rogue host takeover.
    """

    def __init__(self):
        """Snapshot this install's genesis public keys and create its own MultiSigGate.

        Side effects: may create seed files on first use.
        """
        raise NotImplementedError('TODO: implement')

    def get_sovereign_pubkey(self, identity: str) -> str:
        """Return a sovereign's public key hex.

        Args:
            identity: sovereign id or alias.

        Returns:
            Public key hex from the genesis snapshot.

        Raises:
            KeyError: identity is not a sovereign.
        """
        raise NotImplementedError('TODO: implement')

    def is_sovereign(self, identity: str) -> bool:
        """Return True if identity (or alias) is one of this engine's sovereigns."""
        raise NotImplementedError('TODO: implement')

    def attempt_revocation(self, target_id: str, initiator_id: str, signatures: Optional[Dict[str, str]]=None) -> None:
        """Enforces revocation rules.

        Mathematical Invariant:
        Unilateral revocation of either First sovereign or Second sovereign is
        categorically rejected. Genesis sovereign keys are permanent and immutable.

        Args:
            target_id: key/identity someone wants revoked.
            initiator_id: who is asking.
            signatures: map of sovereign id/alias -> signature. Only the presence of
                both keys is checked here; the values are not cryptographically
                verified because the outcome is a refusal either way.

        Returns:
            None, and only for a non-sovereign target (logged as handled).

        Raises:
            UnilateralRevocationError: initiator is not a sovereign, or both
                sovereigns did not sign.
            SovereignImmutableError: target is a sovereign even with both signatures.
        """
        raise NotImplementedError('TODO: implement')

@dataclass
class CensusRecord:
    """One enrolled peer: id, public key hex, ISO enrolment time, who authorised it
    ("GENESIS" for the sovereigns), and whether it is currently verified."""

class CensusValidator:
    """Census Validator: Validates peer keys and drops/rejects unverified peers."""

    def __init__(self, engine: DualSovereigntyEngine):
        """Create a census containing only the two genesis sovereigns.

        Args:
            engine: the DualSovereigntyEngine this census belongs to.
        """
        raise NotImplementedError('TODO: implement')

    def _init_genesis_census(self):
        """Pre-enrol both sovereigns as verified, authorised by "GENESIS"."""
        raise NotImplementedError('TODO: implement')

    def enroll_peer(self, peer_id: str, pubkey: str, authorized_by: str, authorization_signature: str) -> bool:
        """Enrolls a new peer key into the census with sovereign cryptographic authorization.

        Args:
            peer_id: id to enrol.
            pubkey: the peer's public key hex.
            authorized_by: sovereign id/alias vouching for the peer.
            authorization_signature: that sovereign's signature over
                {"action": "enroll_peer", "peer_id": ..., "pubkey": ...}.

        Returns:
            True on success.

        Raises:
            UnverifiedPeerError: authorizer is not a sovereign.
            InvalidSignatureError: signature does not verify.
        Side effects: mutates the census and logs.
        """
        raise NotImplementedError('TODO: implement')

    def is_verified_peer(self, peer_id: str, pubkey: Optional[str]=None) -> bool:
        """Checks if peer_id is enrolled and verified in the census.

        Args:
            peer_id: id or sovereign alias.
            pubkey: if given, must equal the enrolled key.

        Returns:
            True only for an enrolled, verified peer whose key matches (when given).
        """
        raise NotImplementedError('TODO: implement')

    def validate_peer_message(self, message: Dict[str, Any], strict: bool=False) -> Optional[Dict[str, Any]]:
        """Validates incoming message against census.

        If sender is unverified:
        - In non-strict mode: logs warning and returns None (packet dropped).
        - In strict mode: raises UnverifiedPeerError.

        Args:
            message: incoming message dict; sender is read from producer, sender,
                from or seat (first present wins).
            strict: raise instead of dropping.

        Returns:
            The message if the sender is verified, else None.

        Raises:
            UnverifiedPeerError: strict mode and sender missing/unverified.
        """
        raise NotImplementedError('TODO: implement')

    def filter_peer_stream(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters an incoming stream of messages, dropping any from unverified peers.

        Args:
            messages: messages in arrival order.

        Returns:
            The verified subset, order preserved. Never raises (non-strict).
        """
        raise NotImplementedError('TODO: implement')

class EZGuard:
    """Top-level facade coordinating Dual-Sovereignty, Multi-Sig Gate, and Census."""

    def __init__(self):
        """Build the engine, share its gate, and create a census bound to it."""
        raise NotImplementedError('TODO: implement')

    def evaluate_command(self, cmd: str, signatures: Optional[Dict[str, str]]=None) -> GateResult:
        """Evaluate a shell command string through the gate (no raise; see GateResult)."""
        raise NotImplementedError('TODO: implement')

    def enforce_command(self, cmd: str, signatures: Optional[Dict[str, str]]=None) -> GateResult:
        """Like evaluate_command but raises DestructiveActionBlockedError when blocked."""
        raise NotImplementedError('TODO: implement')

    def evaluate_action(self, action: Dict[str, Any], signatures: Optional[Dict[str, str]]=None) -> GateResult:
        """Evaluate a structured action dict through the gate (no raise)."""
        raise NotImplementedError('TODO: implement')

    def enforce_action(self, action: Dict[str, Any], signatures: Optional[Dict[str, str]]=None) -> GateResult:
        """Like evaluate_action but raises DestructiveActionBlockedError when blocked."""
        raise NotImplementedError('TODO: implement')

    def is_peer_verified(self, peer_id: str) -> bool:
        """Return True if peer_id is an enrolled, verified census peer."""
        raise NotImplementedError('TODO: implement')

def main():
    """CLI entry point: `status` prints sovereign key prefixes and census peers;
    `check-cmd <command>` reports whether a command would need 2-of-2 signatures.

    Returns:
        None. Prints to stdout; with no subcommand prints argparse help.
    Side effects: building EZGuard may create key files on first run. Only the
    first 24 hex characters of public keys are shown; secrets are never printed.
    """
    raise NotImplementedError('TODO: implement')
