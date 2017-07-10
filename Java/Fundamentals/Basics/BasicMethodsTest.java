import java.util.*;

class BasicMethodsTest {
    public static void main(String[] args) {
        BasicMethods output = new BasicMethods();

        int[] result1 = output.print1to255();
        System.out.println(Arrays.toString(result1));

        ArrayList<Integer> result2 = output.printOdd1to255();
        System.out.println(result2);

        ArrayList<Integer> result3 = output.printSum();
        System.out.println(result3);

        ArrayList<Integer> newArray = new ArrayList<Integer>();
        newArray.add(3);
        newArray.add(6);
        newArray.add(10);
        newArray.add(7);
        newArray.add(2);
        ArrayList<Integer> result4 = output.printArray(newArray);
        System.out.println(result4);

        int[] newArray = {3, 6, 10, 7, 2};
        int result5 = output.findMax(newArray);
        System.out.println(result5);

        int[] newArray = {3, 6, 10, 7, 2};
        int result6 = output.getAverage(newArray);
        System.out.println(result6);

        ArrayList<Integer> result7 = output.getOdd();
        System.out.println(result7);

        int[] newArray = {3, 6, 10, 7, 2};
        int result8 = output.greaterThanY(newArray, 5);
        System.out.println(result8);

        int[] newArray = {3, 6, 10, 7, 2};
        int[] result9 = output.squareTheValues(newArray);
        System.out.println(Arrays.toString(result9));

        int[] newArray = {-3, 6, -10, 7, -2};
        int[] result10 = output.eliminateNegativeNumbers(newArray);
        System.out.println(Arrays.toString(result10));

        int[] newArray = {2, 4, -10, 7, 9};
        int[] result11 = output.getMaxMinAverage(newArray);
        System.out.println(Arrays.toString(result11));
        //
        int[] newArray = {2, 4, 10, 7, 9};
        int[] result12 = output.shiftTheValues(newArray);
        System.out.println(Arrays.toString(result12));
    }
}
