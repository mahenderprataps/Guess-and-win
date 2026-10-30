# Guess and Win

A simple command-line number guessing game written in Python. The game randomly
chooses a number from 1 to 100, and you keep guessing until you find it.

## Requirements

- Python 3

The game uses Python's built-in `random` module, so no additional packages are
needed.

## Run the game

Open a terminal in the project folder and run:

```powershell
python game.py
```

If your system uses the `py` launcher, you can run:

```powershell
py game.py
```

## How to play

Enter a guess when prompted:

- If your guess is too high, the game says `lower`.
- If your guess is too low, the game says `higher`.
- When you guess correctly, the game displays the number of guesses you made.
