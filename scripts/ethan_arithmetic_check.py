# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Recognize standalone arithmetic and check the model's complete numeric reply."""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
import re

def is_numeric_reply(value: str) -> bool:
    """True when the entire bounded reply consists of a signed decimal."""
    raise NotImplementedError('TODO: implement')

class ArithmeticExpression:

    def matches_reply(self, reply: str) -> bool:
        """Check the entire reply exactly, accepting surrounding whitespace."""
        raise NotImplementedError('TODO: implement')

def parse_arithmetic(prompt: str, *, generation_config=None) -> ArithmeticExpression | None:
    """Return exact operands in evaluation order for a finite decimal task."""
    raise NotImplementedError('TODO: implement')
