"""Helpers for cleaning up text, such as student names."""

def clean_name(raw):
    """Return the name with extra spaces removed, in title case."""
    return " ".join(raw.split()).title()
