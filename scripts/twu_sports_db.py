# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_sports_db.py - local SQLite sports analytics store (NEED-007), fully offline.

The tool never touches the network. You obtain data yourself and feed it CSV/JSON files:
  nflreadpy (MIT), nba_api (MIT), sportsdataverse-py (MIT) export frames/JSON that map
  onto the four kinds below; StatsBomb open data is JSON you download yourself.

DATA LICENSES (the code libraries being MIT does not license the data):
  - nflverse data: CC-BY-4.0 - attribute nflverse when publishing derived work.
  - StatsBomb open data: free for non-commercial research/learning; you must credit
    StatsBomb and show their logo when you publish analysis, and it must not be used
    commercially or redistributed as a product without their agreement. Check
    https://github.com/statsbomb/open-data/blob/master/LICENSE.pdf before any release.
  - NBA stats via nba_api come from stats.nba.com, whose terms restrict commercial reuse.
  Keep a `source` tag on every row (--source) so provenance survives.

Schema (natural keys are (sport, ext id); re-importing the same file is idempotent):
  teams(sport, team_id, name, abbr, extra)
  players(sport, player_id, name, team_id, position, extra)
  games(sport, game_id, season, game_date, home_team_id, away_team_id, home_score, away_score, extra)
  stats(sport, game_id, player_id, stat, value)   long format, one row per stat

Usage:
  twu_sports_db.py import KIND FILE [--db PATH] [--sport nfl] [--source TAG]
  twu_sports_db.py teams|players|games [--sport S] [--team T] [--season Y]
  twu_sports_db.py standings --sport S [--season Y]
  twu_sports_db.py leaders --sport S --stat NAME [--season Y] [--limit 10]
"""
from __future__ import annotations
import argparse
import csv
import json
import sqlite3
import sys
from pathlib import Path

def connect(path) -> sqlite3.Connection:
    raise NotImplementedError('TODO: implement')

def read_rows(path: Path) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def _clean(col, val):
    raise NotImplementedError('TODO: implement')

def import_rows(con, kind: str, rows: list[dict], sport: str | None=None, source: str | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def standings(con, sport, season=None) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def leaders(con, sport, stat, season=None, limit=10) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def list_rows(con, table, sport=None, team=None, season=None) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
