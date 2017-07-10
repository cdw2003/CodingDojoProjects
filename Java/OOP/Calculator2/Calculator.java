import java.util.*;

class Calculator implements java.io.Serializable {
  protected static String operative;
  public static double result = 0;
  public static ArrayList<String> operations = new ArrayList<String>();

  public Calculator(){
  }

  public static void performOperation(String operative){
    operations.add(operative);

    if(operative == "="){
      result = Double.parseDouble(operations.get(0));
      for(int i = 0; i < operations.size(); i++){
        if(operations.get(i) == "+"){
        result += Double.parseDouble(operations.get(i+1));
        }
        if(operations.get(i) == "-"){
        result -= Double.parseDouble(operations.get(i+1));
        }
        if(operations.get(i) == "*"){
        result *= Double.parseDouble(operations.get(i+1));
        }
        if(operations.get(i) == "/"){
        result /= Double.parseDouble(operations.get(i+1));
        }
      }
      operations.clear();
    }
  }

  public static double getResults(){
    System.out.println("The value is now " + result);
    return result;
  }
}
