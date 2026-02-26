"""
Autograder — PR 7: SQLite Queries

Checks that docs/sql_read_results.md exists, is non-empty,
and contains all required section headings.
"""

import os
import pathlib
import pytest

RESULTS_FILE = pathlib.Path("docs/sql_read_results.md")


def _read_results() -> str:
    return RESULTS_FILE.read_text(encoding="utf-8")


def test_sql_read_results_exists():
    """docs/sql_read_results.md must exist."""
    assert RESULTS_FILE.exists(), (
        "docs/sql_read_results.md not found. "
        "Create this file and paste your query results into it."
    )


def test_sql_read_results_nonempty():
    """docs/sql_read_results.md must be non-empty (> 50 bytes)."""
    size = RESULTS_FILE.stat().st_size
    assert size > 50, (
        f"docs/sql_read_results.md is only {size} bytes — it appears to be empty or nearly empty. "
        "Paste your query results and interpretation answers into it."
    )


def test_query_1_heading():
    """File must contain a 'Query 1' section."""
    content = _read_results()
    assert "Query 1" in content, (
        "'Query 1' heading not found in docs/sql_read_results.md. "
        "Add a section for each query result."
    )


def test_query_2_heading():
    """File must contain a 'Query 2' section."""
    content = _read_results()
    assert "Query 2" in content, (
        "'Query 2' heading not found in docs/sql_read_results.md."
    )


def test_query_3_heading():
    """File must contain a 'Query 3' section."""
    content = _read_results()
    assert "Query 3" in content, (
        "'Query 3' heading not found in docs/sql_read_results.md."
    )


def test_query_4_heading():
    """File must contain a 'Query 4' section."""
    content = _read_results()
    assert "Query 4" in content, (
        "'Query 4' heading not found in docs/sql_read_results.md."
    )


def test_interpretation_heading():
    """File must contain an 'Interpretation' section."""
    content = _read_results()
    assert "Interpretation" in content, (
        "'Interpretation' heading not found in docs/sql_read_results.md. "
        "Add your answers to the three interpretation questions."
    )
