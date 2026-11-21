# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Build, check and open the private company document library."""
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import quote

def load_catalog(root=...):
    raise NotImplementedError('TODO: implement')

def validate(catalog, root=...):
    raise NotImplementedError('TODO: implement')

def library_href(relative):
    raise NotImplementedError('TODO: implement')

def render_markdown(catalog):
    raise NotImplementedError('TODO: implement')

def render_html(catalog):
    raise NotImplementedError('TODO: implement')

def generated_outputs(catalog, root=...):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
