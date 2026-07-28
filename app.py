# app.py

from PROGRAM import solve_n_queens, display_board


def main():
    print("========== N-Queens Solver ==========")

    n = int(input("Enter the value of N: "))

    solutions, backtracks = solve_n_queens(n)

    print("\nResults")
    print("-------")
    print(f"N = {n}")
    print(f"Total Solutions = {len(solutions)}")
    print(f"Backtracks = {backtracks}")

    if len(solutions) == 0:
        print("\nNo solution exists.")
        return

    choice = input("\nDisplay all solutions? (y/n): ").lower()

    if choice == "y":
        for i, solution in enumerate(solutions, start=1):
            print(f"\nSolution {i}")
            display_board(solution, n)


if __name__ == "__main__":
    main()
