# Game Statistics Analyzer

## Project Description

Game Statistics Analyzer is a Python-based application designed to analyze player performance in games.  
The system stores match statistics, calculates rankings, generates leaderboards, and provides detailed analytics about player performance.

This project was developed as a final group project for demonstrating:
- Python programming skills
- Object-Oriented Programming
- Algorithm design
- File handling
- Data structures
- Testing and modular architecture

---

# Features

## Core Features
- Store player statistics
- Analyze player performance
- Generate leaderboards
- Calculate average scores
- Find best daily and overall performance
- Search and filter player data
- Export reports

---

# Advanced Features

## Implemented Advanced Python Concepts
- Object-Oriented Programming
- Inheritance and polymorphism
- Generators
- Decorators
- Lambda functions
- Regular expressions
- Exception handling

---

# Technologies Used

- Python 3
- JSON
- CSV
- unittest

---

# Project Structure

```txt
game_statistics_analyzer/
│
├── data/
│   ├── players.json
│   └── reports.csv
│
├── models/
│   ├── player.py
│   ├── match.py
│   └── leaderboard.py
│
├── services/
│   ├── analytics_service.py
│   ├── file_service.py
│   ├── ranking_service.py
│   └── report_service.py
│
├── utils/
│   ├── validators.py
│   ├── decorators.py
│   └── generators.py
│
├── tests/
│   └── test_analytics.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Functionalities

## Leaderboard
The system generates:
- Global leaderboard
- Daily leaderboard
- Top players by score
- Top players by average score

---

## Analytics
The application calculates:
- Average score
- Best performance
- Worst performance
- Win rate
- Score trends

---

## File Handling
The system supports:
- Reading JSON files
- Writing JSON files
- CSV report export

---

# OOP Architecture

## Main Classes

### Person
Base class for all users.

### Player(Person)
Stores player information and statistics.

### Match
Represents one game session.

### Leaderboard
Handles ranking generation and sorting.

### AnalyticsEngine
Processes performance analytics.

---

# Algorithms and Efficiency

The project uses:
- Dictionaries for fast lookup O(1)
- Efficient sorting with lambda functions
- Generators for memory optimization

Example:
```python
sorted(players, key=lambda x: x.average_score, reverse=True)
```

---

# Error Handling

The application validates:
- Incorrect dates
- Empty files
- Negative scores
- Invalid player names

Example:
```python
try:
    load_file()
except FileNotFoundError:
    print("File not found")
```

---

# Testing

The project includes unit testing for:
- Analytics calculations
- Leaderboard generation
- Edge cases
- Validation

Run tests:
```bash
python -m unittest
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-repository/game_statistics_analyzer.git
```

## Open Project

```bash
cd game_statistics_analyzer
```

## Run Application

```bash
python main.py
```

---

# Example Input

```json
[
  {
    "player": "Alice",
    "score": 120,
    "date": "2026-01-01"
  },
  {
    "player": "Bob",
    "score": 150,
    "date": "2026-01-01"
  },
  {
    "player": "Alice",
    "score": 180,
    "date": "2026-01-02"
  }
]
```

---

# Example Output

```txt
Leaderboard:
1. Alice - 300
2. Bob - 150

Average Scores:
Alice - 150
Bob - 150

Best Daily Performance:
Alice - 180
```

---

# Team Members

- Student 1 — OOP & Models
- Student 2 — Analytics & Algorithms
- Student 3 — File Handling & Validation
- Student 4 — Testing & CLI

---

# Future Improvements

Possible future upgrades:
- SQLite database integration
- GUI interface
- Flask API
- Real-time analytics
- Graph visualization

---

# Conclusion

Game Statistics Analyzer demonstrates practical usage of Python programming concepts including:
- OOP
- algorithms
- modular architecture
- testing
- data structures
- file handling

The project simulates a real-world analytics system and provides scalable architecture for future improvements.
