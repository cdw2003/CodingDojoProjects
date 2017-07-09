public class CalculatorTest {
  public static void main(String[] args) {
    Calculator a = new Calculator();
    a.setOperandOne(10.25);
    a.setOperation("+");
    a.setOperandTwo(5.67);
    a.performOperation();
    a.getResults();

    Calculator b = new Calculator();
    b.setOperandOne(8.45);
    b.setOperation("-");
    b.setOperandTwo(3.89);
    b.performOperation();
    b.getResults();
  }
}
