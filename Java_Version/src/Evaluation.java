import java.util.HashMap;
import java.util.Map;

/**
 * Created by qingyun on 5/2/17.
 */
public class Evaluation {
    public static int evaluation(String[] board) {

        Map<Integer, Integer> rowsX = new HashMap<>();
        Map<Integer, Integer> rowsO = new HashMap<>();
        Map<Integer, Integer> colsX = new HashMap<>();
        Map<Integer, Integer> colsO = new HashMap<>();
        for (int i = 1; i < 5; i++) {
            int rowX = 0;
            int rowO = 0;
            int colX = 0;
            int colO = 0;
            for (int j = 1; j < 5; j++) {
                if (board[(i - 1) * 4 + j].equals("X")) {
                    rowX++;
                } else if (board[(i - 1) * 4 + j].equals("O")) {
                    rowO++;
                }
                if (board[(j - 1) * 4 + i].equals("X")) {
                    colX++;
                } else if (board[(j - 1) * 4 + i].equals("O")) {
                    colO++;
                }
            }
            colsX.put(i, colX);
            colsO.put(i, colO);
            rowsX.put(i, rowX);
            rowsO.put(i, rowO);
        }
        int diagX1 = 0;
        int diagX2 = 0;
        int diagO1 = 0;
        int diagO2 = 0;
        int[] diag1 = new int[]{1,6,11,16};
        int[] diag2 = new int[]{4,7,10,13};
        for (int cell : diag1) {
            if (board[cell].equals("X")) {
                diagX1++;
            }
            if (board[cell].equals("O")) {
                diagO1++;
            }
        }
        for (int cell : diag2) {
            if (board[cell].equals("X")) {
                diagX2++;
            }
            if (board[cell].equals("O")) {
                diagO2++;
            }
        }
        int X3 = 0, X2 = 0, X1 = 0;
        for (int val : rowsX.values()) {
            if (val == 3) X3++;
            if (val == 2) X2++;
            if (val == 1) X1++;
        }
        for (int val : colsX.values()) {
            if (val == 3) X3++;
            if (val == 2) X2++;
            if (val == 1) X1++;
        }
        if (diagX1 == 3) X3++;
        if (diagX1 == 2) X2++;
        if (diagX1 == 1) X1++;

        if (diagX2 == 3) X3++;
        if (diagX2 == 2) X2++;
        if (diagX2 == 1) X1++;

        int O3 = 0, O2 = 0, O1 = 0;
        for (int val : rowsO.values()) {
            if (val == 3) O3++;
            if (val == 2) O2++;
            if (val == 1) O1++;
        }
        for (int val : colsO.values()) {
            if (val == 3) O3++;
            if (val == 2) O2++;
            if (val == 1) O1++;
        }
        if (diagO1 == 3) O3++;
        if (diagO1 == 2) O2++;
        if (diagO1 == 1) O1++;

        if (diagO2 == 3) O3++;
        if (diagO2 == 2) O2++;
        if (diagO2 == 1) O1++;
        return 6 * X3 + 3 * X2 + X1 - (6 * O3 + 3 * O2 + O1);
    }
}
