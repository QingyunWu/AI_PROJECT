/**
 * Created by qingyun on 5/2/17.
 */
import java.util.*;

public class Main {

    static int nodeCount = 1;
    static int maxSearchPrunings = 0;
    static int minSearchPrunings = 0;
    static int maxLevel = 0;
    static boolean cutoffOccured = false;

    public static int alphaBetaSearch(String[] board, int difficulty) {
        long startTime = System.nanoTime();

        nodeCount = 1;
        maxSearchPrunings = 0;
        minSearchPrunings = 0;
        maxLevel = 0;
        cutoffOccured = false;
        List<Integer> availabelMoves = Auxiliary.actions(board);
        int resultValue = Integer.MIN_VALUE;
        Map<Integer, Integer> results = new HashMap<>();
        int alpha = -1000;
        int beta = 1000;
        for (int move : availabelMoves) {
            int minValue = minValueSearch(Auxiliary.result(board, move, "X"), alpha, beta, move, 1, difficulty);
            results.put(move, minValue);
            resultValue = Math.max(minValue, resultValue);
            if (resultValue >= beta) {
                maxSearchPrunings++;
                break;
            }
            alpha = Math.max(alpha, resultValue);
        }

        double timeElapsed = (double)((System.nanoTime() - startTime) / Math.pow(10,9));
        System.out.println("-------------------------------------------------");
        System.out.println("total elapsed time for the move is: " + String.valueOf(timeElapsed));
        System.out.println("-------------------------------------------------");
        System.out.println("If cutoff occured? " + String.valueOf(cutoffOccured));
        System.out.println("-------------------------------------------------");
        System.out.println("Max depth reached: " + String.valueOf(maxLevel));
        System.out.println("-------------------------------------------------");
        System.out.println("Total nodes generated: " + String.valueOf(nodeCount));
        System.out.println("-------------------------------------------------");
        System.out.println("Total max searching prunings: " + String.valueOf(maxSearchPrunings));
        System.out.println("-------------------------------------------------");
        System.out.println("Total min searching prunings: " + String.valueOf(minSearchPrunings));
        System.out.println("-------------------------------------------------");

        for (int move : results.keySet()) {
            if (results.get(move) == resultValue) {
                System.out.println("PC chose to go sqaure: " + String.valueOf(move));
                return move;
            }
        }
        return 0;
    }

    private static int minValueSearch(String[] board, int alpha, int beta, int lastMove, int level, int difficulty) {
        nodeCount++;
        TerminateResult ifTerminate = Auxiliary.checkTerminate(board, lastMove);
        if (ifTerminate.ifTerminated) {
            return ifTerminate.val;
        }
        int minValue = Integer.MAX_VALUE;
        List<Integer> availabelMoves = Auxiliary.actions(board);

        for (int move : availabelMoves) {
            if (level + 1 > maxLevel) {
                maxLevel = level + 1;
            }
            if (level >= difficulty + 7) {
                cutoffOccured = true;
                return Evaluation.evaluation(Auxiliary.result(board, move, "O"));
            }
            minValue = Math.min(minValue, maxValueSearch(Auxiliary.result(board, move, "O"), alpha, beta, move, level + 1, difficulty));
            if (minValue <= alpha) {
                minSearchPrunings++;
                return minValue;
            }
            beta = Math.min(beta, minValue);
        }
        return minValue;

    }
    private static int maxValueSearch(String[] board, int alpha, int beta, int lastMove, int level, int difficulty) {
        nodeCount++;
        TerminateResult ifTerminate = Auxiliary.checkTerminate(board, lastMove);
        if (ifTerminate.ifTerminated) {
            return ifTerminate.val;
        }
        int maxValue = Integer.MIN_VALUE;
        List<Integer> availabelMoves = Auxiliary.actions(board);

        for (int move : availabelMoves) {
            if (level + 1 > maxLevel) {
                maxLevel = level + 1;
            }
            // max depth 9, 10 ,11 in java
            if (level  >= difficulty + 7) {
                cutoffOccured = true;
                return Evaluation.evaluation(Auxiliary.result(board, move, "X"));
            }
            maxValue = Math.max(maxValue, minValueSearch(Auxiliary.result(board, move, "X"), alpha, beta, move, level + 1, difficulty));
            if (maxValue >= beta) {
                maxSearchPrunings++;
                return maxValue;
            }
            alpha = Math.max(alpha, maxValue);
        }
        return maxValue;

    }


    public static void main(String[] args) {
        while (true) {
            Auxiliary.drawInitBoard();

            String[] board = new String[17];
            Arrays.fill(board, " ");
            Scanner sc = new Scanner(System.in);
            System.out.println("Welcome, what difficulty you want to play? 1 ~ 3");
            int difficulty = sc.nextInt();
            System.out.println("Do you want to play first? y/n");;
            String goFirst = sc.next();
            String turn = goFirst.equals("y") ? "user" : "pc";
            boolean gameOver = false;
            while (!gameOver) {
                if (turn.equals("user")) {
                    int move = Auxiliary.playerMakeMove(board);
                    board[move] = "O";
                    turn = "pc";
                    if (Auxiliary.checkIfWin(board, move)) {
                        System.out.println("You Won!");
                        gameOver = true;
                    }
                    if (Auxiliary.checkIfFull(board)) {
                        System.out.println("It's a tie!");
                        gameOver = true;
                    }
                } else {
                    int move = alphaBetaSearch(board, difficulty);
                    board[move] = "X";
                    Auxiliary.drawBoard(board);
                    turn = "user";
                    if (Auxiliary.checkIfWin(board, move)) {
                        System.out.println("PC Won!");
                        gameOver = true;
                    }
                    if (Auxiliary.checkIfFull(board)) {
                        System.out.println("It's a tie!");
                        gameOver = true;
                    }
                }
            }
            System.out.println("Do you want to play agin? y/n");
            String playAgain = sc.next();
            if (playAgain.equals("n")) {
                System.out.println("bye bye");
                break;
            }
        }

    }

    private static int checkNumber() {
        try {
            System.out.println("Please input the difficulty");
            Scanner sc = new Scanner(System.in);
            return sc.nextInt();
        } catch (InputMismatchException e) {
            return 0;
        }
    }

}
