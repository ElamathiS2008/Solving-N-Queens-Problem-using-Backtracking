# N-Queens Solver using Backtracking

## Project Description

This project solves the N-Queens problem using the Backtracking algorithm.

The objective is to place N queens on an N×N chessboard so that no two queens attack each other.

A queen can attack:
- Horizontally
- Vertically
- Diagonally

The algorithm places queens one row at a time and backtracks whenever it encounters an invalid placement.

---

## Files

### PROGRAM.py
Contains:
- is_safe()
- solve_n_queens()
- display_board()

### app.py
Main program that:
- Takes user input
- Calls the algorithm
- Displays results

---

## Algorithm

1. Start from row 0.
2. Try placing a queen in every column.
3. Check whether the position is safe.
4. If safe, place the queen.
5. Move to the next row.
6. If no safe position exists, backtrack.
7. Continue until all solutions are found.

---

## Time Complexity

Worst Case:

O(N!)

Space Complexity:

O(N)

---

## Sample Output

```
========== N-Queens Solver ==========

Enter the value of N: 4

Results
-------
N = 4
Total Solutions = 2
Backtracks = 16

Display all solutions? (y/n): y

Solution 1

 +---+---+---+---+
 | . | Q | . | . |
 +---+---+---+---+
 | . | . | . | Q |
 +---+---+---+---+
 | Q | . | . | . |
 +---+---+---+---+
 | . | . | Q | . |
 +---+---+---+---+

Solution 2

 +---+---+---+---+
 | . | . | Q | . |
 +---+---+---+---+
 | Q | . | . | . |
 +---+---+---+---+
 | . | . | . | Q |
 +---+---+---+---+
 | . | Q | . | . |
 +---+---+---+---+
```

---

## Requirements

- Python 3.x

---

## How to Run

```
python app.py
```

---

## Author
ELAMATHI S

N-Queens Solver using Backtracking Algorithm.
