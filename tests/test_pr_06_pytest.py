"""
Autograder: PR 6 — First Tests: Make 5 Failing Tests Pass
Phase 3 — Engineering Practices
"""

import importlib.util
import pathlib

import pytest

REPO_ROOT = pathlib.Path(__file__).parent.parent


def _load_functions():
    """Import the learner's functions.py from the repo root."""
    path = REPO_ROOT / "functions.py"
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location("student_functions", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestFunctionsFileExists:
    def test_functions_file_exists(self):
        path = REPO_ROOT / "functions.py"
        assert path.exists(), (
            "functions.py not found at the repo root. "
            "Run the curl commands from the assignment to fetch the starter files, "
            "then fix the bugs and commit functions.py."
        )


class TestAdd:
    def test_add(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.add(2, 3) == 5, (
            "add(2, 3) returned the wrong value. "
            "Fix the bug in functions.py — add() should return a + b."
        )


class TestIsEven:
    def test_is_even_even_number(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.is_even(4) is True, (
            "is_even(4) should return True. "
            "Fix the bug — is_even() should return True when n % 2 == 0."
        )

    def test_is_even_odd_number(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.is_even(7) is False, (
            "is_even(7) should return False. "
            "Fix the bug — is_even() should return False for odd numbers."
        )


class TestCelsiusToFahrenheit:
    def test_celsius_to_fahrenheit_freezing(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.celsius_to_fahrenheit(0) == 32, (
            "celsius_to_fahrenheit(0) should return 32. "
            "Fix the bug — the formula is (celsius × 9/5) + 32. "
            "The + 32 is missing."
        )

    def test_celsius_to_fahrenheit_boiling(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.celsius_to_fahrenheit(100) == 212, (
            "celsius_to_fahrenheit(100) should return 212. "
            "Fix the bug — the formula is (celsius × 9/5) + 32."
        )


class TestCountVowels:
    def test_count_vowels_word(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.count_vowels("hello") == 2, (
            "count_vowels('hello') should return 2 (e, o). "
            "Fix the bug — make sure all five vowels a, e, i, o, u are counted."
        )

    def test_count_vowels_all_vowels(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.count_vowels("aeiou") == 5, (
            "count_vowels('aeiou') should return 5. "
            "Fix the bug — 'a' is missing from the vowel string."
        )


class TestFirstWord:
    def test_first_word(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.first_word("hello world") == "hello", (
            "first_word('hello world') should return 'hello'. "
            "Fix the bug — use index 0, not 1."
        )

    def test_first_word_longer(self):
        mod = _load_functions()
        if mod is None:
            pytest.skip("functions.py missing — skipping")
        assert mod.first_word("pytest is great") == "pytest", (
            "first_word('pytest is great') should return 'pytest'. "
            "Fix the bug — return sentence.split()[0]."
        )
