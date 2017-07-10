public class StringManipulator {
  public String trimAndConcat(String A, String B) {
    String newStringA = A.trim();
    String newStringB = B.trim();
    String string1 = newStringA.concat(newStringB);
    return string1;
  }
  public String getIndexOrNull(String A, char one){
    int a = A.indexOf(one);
    if(a >= 0){
      return "" + a;
    }
    else{
      return "null";
    }
  }
  public String getIndexOrNull(String C, String D){
    int b = C.indexOf(D);
    if(b >= 0){
      return "" + b;
    }
    else{
      return "null";
    }
  }
  public String concatSubstring(String E, int one, int two, String F){
    String string2 = E.substring(one, two);
    String newString = string2.concat(F);
    return newString;
  }
}
