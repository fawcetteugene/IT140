# IT140 — Text-Based Games

This repository contains two simple Python text-based game assignments created for IT-140.

Files

- ModuleSixAssignment.py — Simplified Dragon Text Game (small 3-room demo).
- TextBasedGame.py — Tech-Hacker Adventure Game: collect tools and defeat the Villain Hacker.

Requirements

- Python 3.6+

How to run

From the project root run:

```bash
python ModuleSixAssignment.py
# or
python TextBasedGame.py
```

Gameplay

- Movement commands: `go North`, `go South`, `go East`, `go West`.
- Item pickup (TextBasedGame): `get [item]`.
- Quit: `exit`.

Notes

- No external dependencies are required.
- Preserve the repository structure; scripts are standalone and runnable as-is.

Push to GitHub (example commands)

1. Initialize local repo and commit:

```bash
cd /home/fawcett/Desktop/MyWork/IT140
git init
git add README.md ModuleSixAssignment.py TextBasedGame.py
git commit -m "Add README and text-based games" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

2. Create a GitHub repository named `IT140-games` and add remote, then push (replace <username> and <repo> as appropriate):

```bash
# Replace with your GitHub repo URL
git remote add origin https://github.com/<username>/IT140-games.git
git branch -M main
git push -u origin main
```

If you want the assistant to create the GitHub repo and push it, provide a GitHub personal access token with repo scope and the exact repository name/visibility.

License

This code is provided as-is for educational purposes.
