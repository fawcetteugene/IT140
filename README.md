# IT140 — Text-Based Games

A collection of simple Python text-based adventure games created for **IT-140** (Introduction to Scripting). Explore rooms, follow commands, and complete missions—all from the terminal with no external dependencies.

## 💰 Support the Project

If you find this project valuable, please consider supporting its continued development.

[![Donate-Paystack](https://img.shields.io/badge/Donate-Paystack-00BFFF?style=for-the-badge&logo=paystack&logoColor=white)](https://paystack.shop/pay/fawcettdonations)

**Contact:**

- **WhatsApp:** +254794689731
- **LinkedIn:** [fawcetteugene](https://www.linkedin.com/in/fawcetteugene/)

## Overview

This repository contains two standalone Python scripts that demonstrate core scripting concepts: dictionaries for room layouts, user input handling, conditional logic, and game loops. Both games run entirely in the console and are suitable for learning or coursework demonstrations.

## Features

### ModuleSixAssignment.py — Dragon Text Game (Simplified)

- A compact 3-room adventure (`Great Hall`, `Bedroom`, `Cellar`)
- Direction-based movement with simple validation
- IT-140 Module Six milestone project

### TextBasedGame.py — Tech-Hacker Adventure Game

- An 8-room cyber-themed adventure with hints per room
- Collect **6 cyber tools** before confronting the Villain Hacker
- Inventory tracking and win/lose conditions
- Emoji-enhanced terminal output for a richer player experience

**Tools to collect:** Laptop, Firewall Token, USB Drive, Encrypted Key, Toolkit, Admin Badge

## Tech Stack

| Component   | Technology        |
| ----------- | ----------------- |
| Language    | Python 3.6+       |
| Runtime     | CPython (stdlib)  |
| Dependencies| None              |
| Interface   | Terminal / CLI    |

## Requirements

- Python 3.6 or newer

## Installation

Clone the repository:

```bash
git clone https://github.com/fawcetteugene/IT140.git
cd IT140
```

No package installation is required—both scripts use only the Python standard library.

## How to Run

From the project root, run either game:

```bash
python ModuleSixAssignment.py
```

```bash
python TextBasedGame.py
```

On some systems you may need `python3` instead of `python`:

```bash
python3 TextBasedGame.py
```

## Gameplay

### Movement

- `go North`, `go South`, `go East`, `go West`

### Items (TextBasedGame only)

- `get [item]` — pick up an item in the current room (e.g., `get Laptop`)

### Quit

- `exit` — leave the game

## Project Structure

```
IT140/
├── ModuleSixAssignment.py   # Simplified 3-room Dragon Text Game
├── TextBasedGame.py         # Tech-Hacker Adventure (6 tools + boss fight)
└── README.md
```

## Notes

- Scripts are standalone and runnable as-is—preserve the flat repository structure.
- No database, web server, or build step is required.
- Author credit appears in source file headers (Trevon Mathis).

## License

This code is provided as-is for **educational purposes**.
