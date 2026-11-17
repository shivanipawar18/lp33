import java.util.Scanner;

public class NQueens {

    int n;
    int board[][];

    // Initialization
    NQueens(int n) {
        this.n = n;
        board = new int[n][n];

        // Initialize all positions with 0
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = 0;
            }
        }
    }

    // Check whether queen can be placed safely
    boolean isSafe(int row, int col) {

        // Check upper column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper left diagonal
        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1)
                return false;
        }

        // Check upper right diagonal
        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Backtracking method
    boolean solve(int row) {

        // All queens are placed
        if (row == n)
            return true;

        for (int col = 0; col < n; col++) {

            if (isSafe(row, col)) {

                board[row][col] = 1;

                // Place queen in next row
                if (solve(row + 1))
                    return true;

                // Backtracking
                board[row][col] = 0;
            }
        }

        return false;
    }

    // Display chessboard
    void display() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1)
                    System.out.print("Q ");
                else
                    System.out.print("- ");
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter N: ");
        int n = sc.nextInt();

        NQueens obj = new NQueens(n);

        if (obj.solve(0)) {
            System.out.println("Solution:");
            obj.display();
        } else {
            System.out.println("No solution exists.");
        }

        sc.close();
    }
}


N-Queen
