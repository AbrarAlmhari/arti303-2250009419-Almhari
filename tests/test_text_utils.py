"""Tests for src/text_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import text_utils


def test_clean_name_whitespace():
    assert text_utils.clean_name("  sara   alotaibi  ") == "Sara Alotaibi"
    assert text_utils.clean_name("  faisal    alharbi ") == "Faisal Alharbi"


def test_clean_name_capitalisation():
    assert text_utils.clean_name("SARA ALOTAIBI") == "Sara Alotaibi"
    assert text_utils.clean_name("lama alqahtani") == "Lama Alqahtani"
