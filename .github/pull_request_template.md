## What changed
In this PR, I describe the specific change introduced in the repository. 
This includes which files were modified and what behavior or functionality was added, removed, or improved. 
The goal is to help the reviewer understand the scope without reading the entire diff.

## Why
This section explains the reason behind the change. 
What problem does this solve? 
Was there a bug, missing feature, or design improvement? 
Any important context or tradeoffs should be clearly stated here so future contributors understand the decision.

## How to test
To verify this PR on a clean way:

1. Activate the virtual environment.
2. Install dependencies if needed.
3. Run the relevant command (pytest tests).
4. Confirm that the output matches the expected behavior described above.

## Checklist
- [ ] The PR title clearly describes the change and uses imperative mood
- [ ] This PR contains only one logical change (no scope creep)
- [ ] All tests pass locally
- [ ] README updated if behavior changed
- [ ] No debug prints, breakpoints, or temporary code remain