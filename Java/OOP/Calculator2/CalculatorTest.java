public class CalculatorTest {
  public static void main(String[] args) {
    Calculator.performOperation("10.25");
    Calculator.performOperation("+");
    Calculator.performOperation("2.57");
    Calculator.performOperation("-");
    Calculator.performOperation("3.12");
    Calculator.performOperation("*");
    Calculator.performOperation("4.5");
    Calculator.performOperation("/");
    Calculator.performOperation("6.8");
    Calculator.performOperation("+");
    Calculator.performOperation("2.3");
    Calculator.performOperation("=");
    Calculator.getResults();

    Calculator.performOperation("10.5");
    Calculator.performOperation("+");
    Calculator.performOperation("5.2");
    Calculator.performOperation("*");
    Calculator.performOperation("10");
    Calculator.performOperation("=");
    Calculator.getResults();
  }
}
