import java.util.*;

public class BasicMethods{
  public int[] print1to255(){
    int[] newArray;
    newArray = new int[255];
    for(int i = 0; i < 255; i++){
      newArray[i] = i+1;
    }
    return newArray;
}
  public ArrayList<Integer> printOdd1to255(){
    ArrayList<Integer> newArray = new ArrayList<Integer>();
    for(int i = 0; i < 256; i++){
        if(i % 2 != 0){
        newArray.add(i);
      }
    }
    return newArray;
  }
  public ArrayList<Integer> printSum(){
    ArrayList<Integer> newArray = new ArrayList<Integer>();
    int sum = 0;
    for(int i = 0; i < 256; i++){
      sum = sum + i;
      newArray.add(i);
      newArray.add(sum);
    }
    return newArray;
  }
  public ArrayList<Integer> printArray(ArrayList<Integer> A){
    return A;
    }

  public int findMax(int[] arr){
    int max = 0;
    for(int i = 0; i < arr.length; i++){
      if(arr[i] > max){
        max = arr[i];
      }
    }
    return max;
  }
  public int getAverage(int[] arr){
    int sum = 0;
    for(int i = 0; i < arr.length; i++){
      sum = sum + arr[i];
    }
    return sum/arr.length;
  }
  public ArrayList<Integer> getOdd(){
    ArrayList<Integer> newArray = new ArrayList<Integer>();
    for(int i = 0; i < 256; i++){
        if(i % 2 != 0){
        newArray.add(i);
      }
    }
    return newArray;
  }
  public int greaterThanY(int[] arr, int Y){
    int count = 0;
    for(int i = 0; i < arr.length; i++){
      if(arr[i] > Y){
        count = count + 1;
      }
    }
    return count;
  }
  public int[] squareTheValues(int[] arr){
    for(int i = 0; i < arr.length; i++){
      arr[i] = arr[i] * arr[i];
    }
    return arr;
  }
  public int[] eliminateNegativeNumbers(int[] arr){
    for(int i = 0; i < arr.length; i++){
      if(arr[i] < 0){
        arr[i] = 0;
      }
    }
    return arr;
  }
  public int[] getMaxMinAverage(int[] arr){
    int sum = arr[0];
    int max = arr[0];
    int min = arr[0];
    for(int i = 1; i < arr.length; i++){
      sum = sum + arr[i];
      if(arr[i] > max){
        max = arr[i];
      }
      if(arr[i] < min){
        min = arr[i];
      }
    }
    int average = sum/arr.length;
    int[] result = {max, min, average};
    return result;
  }
//
  public int[] shiftTheValues(int[] arr){
    for(int i = 0; i < arr.length-1; i++){
      arr[i] = arr[i+1];
    }
    arr[arr.length-1] = 0;
    return arr;
  }
}
