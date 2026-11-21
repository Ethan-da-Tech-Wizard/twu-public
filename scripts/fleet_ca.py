# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""fleet_ca.py - thin, documented wrapper around ssh-keygen for an SSH certificate authority.

PHASE 1 PROTOTYPE (see docs/FLEET_SSH_CERTIFICATES_PHASE1.md). It only manages files inside
the directory given with --ca-dir. It never touches ~/.ssh, never edits any sshd config, never
uses sudo, never uses a shell (fixed argv lists only) and never prints private key material.

Layout under --ca-dir (created with mode 700):
  ca/NAME, ca/NAME.pub      CA keypairs (private key mode 600; unencrypted in the lab,
                            real CAs should be given a passphrase with ssh-keygen -p)
  hosts/HOST, HOST.pub, HOST-cert.pub
  users/NAME, NAME.pub, NAME-cert.pub
  issued/SERIAL-cert.pub    copy of every certificate (used by revoke)
  revoked.krl               key revocation list (sshd: RevokedKeys)
  serial                    last serial number used
  trusted_user_cas.pub      all CA public keys (sshd: TrustedUserCAKeys)

Subcommands: init-ca NAME | issue-host HOST | issue-user NAME | revoke SERIAL | list
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

class CaError(Exception):
    pass

def _name(value, what):
    raise NotImplementedError('TODO: implement')

def _valid(value):
    raise NotImplementedError('TODO: implement')

def _ssh_dir_ok(ca_dir: Path):
    """Refuse the real ~/.ssh (and anything inside it) as a CA dir."""
    raise NotImplementedError('TODO: implement')

class Ca:

    def __init__(self, ca_dir):
        raise NotImplementedError('TODO: implement')

    def path(self, *parts):
        """Every file path goes through here: it must stay inside the CA directory."""
        raise NotImplementedError('TODO: implement')

    def run(self, argv):
        """Fixed argv, no shell. Output is shown only for commands that cannot print secrets."""
        raise NotImplementedError('TODO: implement')

    def next_serial(self):
        raise NotImplementedError('TODO: implement')

    def rebuild_trust(self):
        raise NotImplementedError('TODO: implement')

    def signing_ca(self, name):
        raise NotImplementedError('TODO: implement')

    def init_ca(self, name):
        raise NotImplementedError('TODO: implement')

    def _issue(self, kind, name, ca, valid, principals):
        raise NotImplementedError('TODO: implement')

    def issue_host(self, host, ca=None, valid=..., principals=None):
        raise NotImplementedError('TODO: implement')

    def issue_user(self, name, ca=None, valid=..., principals=None):
        raise NotImplementedError('TODO: implement')

    def revoke(self, serial):
        raise NotImplementedError('TODO: implement')

    def list(self):
        raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
