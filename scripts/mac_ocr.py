# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Mac Local OCR Engine (Tesseract 5.5.2 & PDFKit Vision Integration).

Provides hermetic local OCR capabilities for the Mac Model Collective (Ethan, 2026-10-19):
  1. Scans images (PNG, JPG, TIFF, BMP, WebP) using local Tesseract 5.5.2.
  2. Extracts text from PDF receipts and invoices using macOS native PDFKit / Vision.
  3. Parses structured receipt metadata (vendor, date, total amount, category).
  4. Scans for privacy invariant leaks via cloud_guard before emitting data.

Runs locally with zero cloud spend ($0.00, zero cloud tokens).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

def is_tesseract_available():
    raise NotImplementedError('TODO: implement')

def ocr_image(image_path, lang=...):
    """Runs Tesseract OCR on an image file and returns the extracted text."""
    raise NotImplementedError('TODO: implement')

def extract_pdf_text(pdf_path):
    """Extracts text from a PDF file using macOS native PDFKit (receipt_ocr.js)."""
    raise NotImplementedError('TODO: implement')

def parse_receipt_text(text):
    """Extracts vendor, date, total amount, and keywords from OCR text."""
    raise NotImplementedError('TODO: implement')

def scan_file(file_path):
    """Auto-detects image vs PDF and runs appropriate OCR/extraction pipeline."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
