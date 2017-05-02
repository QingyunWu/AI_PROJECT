import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * Created by qingyun on 5/2/17.
 */
public class Auxiliary {

    public static void drawInitBoard() {
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + String.valueOf(1) + "  |  " + String.valueOf(2) + "  |  " + String.valueOf(3) + "  |  " + String.valueOf(4) + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + String.valueOf(5) + "  |  " + String.valueOf(6) + "  |  " + String.valueOf(7) + "  |  " + String.valueOf(8) + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + String.valueOf(9) + "  | " + String.valueOf(10) + "  | " + String.valueOf(11) + "  | " + String.valueOf(12) + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("| " + String.valueOf(13) + "  | " + String.valueOf(14) + "  | " + String.valueOf(15) + "  | " + String.valueOf(16) + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
    }

    public static void drawBoard(String[] board) {
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  |  " + board[4] + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + board[5] + "  |  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + board[9] + "  |  " + board[10] + "  |  " + board[11] + "  |  " + board[12] + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
        System.out.println("|     |     |     |     |");
        System.out.println("|  " + board[13] + "  |  " + board[14] + "  |  " + board[15] + "  |  " + board[16] + "  | ");
        System.out.println("|     |     |     |     |");
        System.out.println("-------------------------");
    }

    public static boolean checkIfFull(String[] board) {
        for (String str : board) {
            if (str.equals(" ")) {
                return false;
            }
        }
        return true;
    }

    public static List<Integer> actions(String[] board) {
        List<Integer> actions = new ArrayList<>();
        for (int i = 1; i < board.length; i++) {
            if (board[i].equals(" ")) {
                actions.add(i);
            }
        }
        return actions;
    }

    public static String[] result(String[] board, int move, String symbol) {
        String[] result = board.clone();
        result[move] = symbol;
        return result;
    }

    public static TerminateResult checkTerminate(String[] board, int move) {
        String lastSymbol = board[move];
        boolean ifWin = checkIfWin(board, move);
        if (ifWin && lastSymbol.equals("X")) {
            return new TerminateResult(true, 1000);
        }
        if (ifWin && lastSymbol.equals("O")) {
            return new TerminateResult(true, -1000);
        }
        if (checkIfFull(board)) {
            return new TerminateResult(true, 0);
        }
        return new TerminateResult(false, 1234);

    }

    public static boolean checkIfWin(String[] board, int lastMove) {
        String lastSymbol = board[lastMove];
        int lineCount = 0;
        for (int i = 1; i < board.length; i++) {
            if (i % 4 == lastMove % 4) {
                if (board[i].equals(lastSymbol)) {
                    lineCount++;
                } else {
                    lineCount = 0;
                    break;
                }
            }
        }
        if (lineCount == 4) return true;

        for (int i = 1; i < board.length; i++) {
            if ((i - 1) / 4 == (lastMove - 1) / 4) {
                if (board[i].equals(lastSymbol)) {
                    lineCount++;
                } else {
                    lineCount = 0;
                    break;
                }
            }
        }
        if (lineCount == 4) return true;

        if (lastMove == 4 || lastMove == 7 || lastMove == 10 || lastMove == 13) {
            int[] nums = new int[]{4,7,10,13};
            for (int num : nums) {
                if (board[num].equals(lastSymbol)) {
                    lineCount++;
                } else {
                    lineCount = 0;
                    break;
                }
            }
        }
        if (lineCount == 4) return true;

        if (lastMove == 1|| lastMove == 6 || lastMove == 11 || lastMove == 16) {
            int[] nums = new int[]{1,6,11,16};
            for (int num : nums) {
                if (board[num].equals(lastSymbol)) {
                    lineCount++;
                } else {
                    lineCount = 0;
                    break;
                }
            }
        }
        if (lineCount == 4) return true;

        return false;
    }

    public static int playerMakeMove(String[] board) {
        List<Integer> availableMoves = actions(board);
        Scanner sc = new Scanner(System.in);
        System.out.println("Now it's your turn, pick a cell to place your SYMBOL 'O'. (1 ~ 16 starts at left top) ");
        int move = sc.nextInt();
        if (!availableMoves.contains(move)) {
            System.out.println("The square has already been taken! Try another square!");
            return playerMakeMove(board);
        }
        return move;
    }


}


class TerminateResult {
    boolean ifTerminated;
    int val;

    public TerminateResult(boolean ifTerminated, int val) {
        this.ifTerminated = ifTerminated;
        this.val = val;
    }
}
