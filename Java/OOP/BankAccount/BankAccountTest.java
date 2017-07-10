public class BankAccountTest {
  public static void main(String[] args) {
    BankAccount a = new BankAccount();
    BankAccount b = new BankAccount();
    BankAccount c = new BankAccount();

    a.depositMoney(100, 250);
    b.depositMoney(50, 300);
    c.depositMoney(500, 25);
    a.withdrawMoney(0, 100);
    b.withdrawMoney(10, 100);

    System.out.println(c.getChecking());
    System.out.println(a.getSaving());

    System.out.println(BankAccount.getTotalMoney());
  }
}
