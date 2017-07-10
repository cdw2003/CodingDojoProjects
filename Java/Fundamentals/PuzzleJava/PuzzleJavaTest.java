import java.util.*;

class PuzzleJavaTest {
    public static void main(String[] args) {
      PuzzleJava output = new PuzzleJava();

      ArrayList<Integer> result1 = output.printSumAndGreaterThanTen();
      System.out.println(result1);

      ArrayList<String> result2 = output.printNames();
      System.out.println(result2);

      ArrayList<Character> result3 = output.printAlphabet();
      System.out.println(result3);

      int[] result4 = output.generateRandom();
      System.out.println(Arrays.toString(result4));

      int[] result5 = output.sortedRandom();
      System.out.println(Arrays.toString(result5));

      String result6 = output.randomString();
      System.out.println(result6);

      String[] result7= output.fiveStrings();
      System.out.println(Arrays.toString(result7));
  }
}
