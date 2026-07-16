# Flashcard Quiz App

## About
A Python command-line study tool for tech-centric learners who prioritize efficiency, automation and full data ownership — software developers, system administrators, Computer Science students and data privacy advocates. Built for distraction-free focus, instant startup and offline functionality, with no reliance on a browser-based app like Anki or Quizlet.

## Features
- **Create Custom Decks** — build your own flashcard decks by entering questions and answers one at a time
- **Multiple Decks** — save as many decks as you want, each stored as its own JSON file
- **Sequential or Shuffled** — choose to go through cards in order or randomize them each time
- **Forgiving Answer Matching** — answers are checked with normalized capitalization and whitespace, so small formatting differences don't count against you
- **Score Tracking** — see your final score and percentage after every quiz
- **Missed Question Retry** — automatically tracks every question you get wrong and lets you retry just those, without redoing the ones you already know
- **Persistent Storage** — decks are saved locally in JSON and reload every time you run the program

## How to Run

**Requirements:** Python 3 installed on your machine.

**Clone the repository:**
```bash
git clone https://github.com/GeekOryan/Flashcard-Quiz-App.git
```

**Navigate into the folder:**
```bash
cd Flashcard-Quiz-App
```

**Run the program:**
```bash
python flashcard_quiz.py
```

## Tech Used
- Python 3
- `json` module — deck persistence
- `os` module — listing available deck files
- `random` module — shuffling card order
