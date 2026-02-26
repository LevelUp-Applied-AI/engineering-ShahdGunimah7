"""
Autograder — PR 8: Docker + Postgres Container Validation

Checks that docs/docker-notes.md exists, is non-empty,
and contains evidence of the required validation steps.
"""

import pathlib
import pytest

NOTES_FILE = pathlib.Path("docs/docker-notes.md")


def _read_notes() -> str:
    return NOTES_FILE.read_text(encoding="utf-8")


def test_docker_notes_exists():
    """docs/docker-notes.md must exist."""
    assert NOTES_FILE.exists(), (
        "docs/docker-notes.md not found. "
        "Create this file and document your Docker validation steps."
    )


def test_docker_notes_nonempty():
    """docs/docker-notes.md must be non-empty (> 100 bytes)."""
    size = NOTES_FILE.stat().st_size
    assert size > 100, (
        f"docs/docker-notes.md is only {size} bytes — it appears to be empty or nearly empty. "
        "Document each step of the Docker validation workflow."
    )


def test_hello_world_documented():
    """File must contain 'hello-world' — smoke test must be documented."""
    content = _read_notes()
    assert "hello-world" in content, (
        "'hello-world' not found in docs/docker-notes.md. "
        "Document the output of 'docker run hello-world' in your notes."
    )


def test_postgres_container_documented():
    """File must contain 'postgres' — Postgres container step must be documented."""
    content = _read_notes()
    assert "postgres" in content.lower(), (
        "'postgres' not found in docs/docker-notes.md. "
        "Document the Postgres container run command and output."
    )


def test_startup_log_confirmed():
    """File must contain the Postgres startup confirmation log line."""
    content = _read_notes()
    assert "ready to accept connections" in content, (
        "'ready to accept connections' not found in docs/docker-notes.md. "
        "Paste the output of 'docker logs pg-prework' — look for the line "
        "'LOG:  database system is ready to accept connections' and include it in your notes."
    )


def test_stop_documented():
    """File must contain 'stop' — docker stop step must be documented."""
    content = _read_notes()
    assert "stop" in content.lower(), (
        "'stop' not found in docs/docker-notes.md. "
        "Document the 'docker stop' command in your notes."
    )


def test_restart_documented():
    """File must contain 'restart' — docker restart step must be documented."""
    content = _read_notes()
    assert "restart" in content.lower(), (
        "'restart' not found in docs/docker-notes.md. "
        "Document the 'docker restart' command in your notes."
    )
