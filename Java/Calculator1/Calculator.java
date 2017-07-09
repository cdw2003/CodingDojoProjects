import java.util.*;

class Calculator implements java.io.Serializable {
  protected double operand1;
  protected String operator;
  protected double operand2;

  public Calculator(){
  }

  public void setOperandOne(double operand1){
    this.operand1 = operand1;
  }

  public void setOperation(String operator){
    this.operator= operator;
  }

  public void setOperandTwo(double operand2){
    this.operand2 = operand2;
  }

  public double performOperation(){
    double result = 0;

    if(this.operator == "+"){
      result = this.operand1 + this.operand2;
    }
    else if (this.operator == "-"){
      result = this.operand1 - this.operand2;
    }
    else{
      System.out.println("That operation is not allowed.");
    }
    return result;
  }

  public double getResults(){
    double result = this.performOperation();
    System.out.println("The result is " + result);
    return result;
  }
}
