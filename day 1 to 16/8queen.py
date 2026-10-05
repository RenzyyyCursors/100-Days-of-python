#%%
def is_safe(row, col, board_state):
    """
    Checks if it is safe to place a queen at (row, col).
    board_state holds the column position for each queen in previous rows.
    """
    for previous_row in range(row):
        previous_col = board_state[previous_row]
        
        # Check if the column is already occupied
        if previous_col == col:
            return False
        
        # Check both the major and minor diagonals
        if abs(previous_col - col) == abs(previous_row - row):
            return False
            
    return True

def solve_8_queens(row, board_state, solutions):
    """
    Recursively attempts to place queens using backtracking.
    """
    # Base case: All 8 queens are successfully placed
    if row == 8:
        solutions.append(list(board_state))
        return

    # Try placing a queen in each column of the current row
    for col in range(8):
        if is_safe(row, col, board_state):
            board_state[row] = col          # Place the queen
            solve_8_queens(row + 1, board_state, solutions)  # Recurse to next row
            board_state[row] = -1         # Backtrack (reset)

def print_board(solution):
    """
    Renders the 8x8 board in a readable format.
    """
    for col in solution:
        row_string = [" . "] * 8
        row_string[col] = " Q "
        print("".join(row_string))
    print("\n" + "="*24 + "\n")

# Main execution loop
if __name__ == "__main__":
    all_solutions = []
    # Initialize the board with -1 (indicating no queen placed yet)
    initial_board = [-1] * 8
    
    solve_8_queens(0, initial_board, all_solutions)
    
    print(f"Total unique solutions found: {len(all_solutions)}\n")
    
    # Display the first 3 configurations as a preview
    for i, sol in enumerate(all_solutions[:3]):
        print(f"--- Solution {i + 1} ---")
        print_board(sol)

# %%
