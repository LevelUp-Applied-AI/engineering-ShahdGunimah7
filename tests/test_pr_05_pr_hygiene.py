"""
Autograder: PR 5 — PR Hygiene: Template + Self-Review Checklist
Phase 3 — Engineering Practices
"""

import pathlib

import pytest

REPO_ROOT = pathlib.Path(__file__).parent.parent


class TestPRTemplate:
    def test_pr_template_exists(self):
        path = REPO_ROOT / ".github" / "pull_request_template.md"
        assert path.exists(), (
            ".github/pull_request_template.md not found. "
            "Create this file following the instructions in today's assignment."
        )

    def test_pr_template_has_content(self):
        path = REPO_ROOT / ".github" / "pull_request_template.md"
        if not path.exists():
            pytest.skip(".github/pull_request_template.md missing — skipping content check")
        content = path.read_text(encoding="utf-8")
        assert len(content) >= 100, (
            f".github/pull_request_template.md has only {len(content)} characters. "
            "A meaningful PR template should describe What/Why/How/Test sections. "
            "Write more content."
        )

    def test_pr_template_has_checklist(self):
        path = REPO_ROOT / ".github" / "pull_request_template.md"
        if not path.exists():
            pytest.skip(".github/pull_request_template.md missing — skipping checklist check")
        content = path.read_text(encoding="utf-8")
        assert "- [ ]" in content, (
            ".github/pull_request_template.md does not contain any checklist items. "
            "Add at least one '- [ ]' item (e.g. '- [ ] Tests added or updated')."
        )


class TestPRChecklist:
    def test_pr_checklist_exists(self):
        path = REPO_ROOT / "docs" / "pr-checklist.md"
        assert path.exists(), (
            "docs/pr-checklist.md not found. "
            "Create this file with your self-review checklist (at least 5 items)."
        )

    def test_pr_checklist_has_items(self):
        path = REPO_ROOT / "docs" / "pr-checklist.md"
        if not path.exists():
            pytest.skip("docs/pr-checklist.md missing — skipping item count check")
        content = path.read_text(encoding="utf-8")
        item_count = content.count("- [ ]")
        assert item_count >= 5, (
            f"docs/pr-checklist.md has only {item_count} checklist item(s). "
            "A useful self-review checklist has at least 5 items. "
            "Add more '- [ ]' items covering what you check before opening a PR."
        )


class TestReadme:
    def test_readme_has_how_to_run(self):
        path = REPO_ROOT / "README.md"
        assert path.exists(), (
            "README.md not found. This file should already exist in your repo."
        )
        content = path.read_text(encoding="utf-8").lower()
        assert "how to run" in content, (
            "README.md does not contain a 'How to run' section. "
            "Add a '## How to run' heading with at least 3 steps explaining "
            "how a reviewer can set up and run the code."
        )
