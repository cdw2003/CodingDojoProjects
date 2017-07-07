public class SinglyLinkedListTest{
  public static void main(String[] args) {
    SinglyLinkedList one = new SinglyLinkedList();
    one.add(5);
    one.add(10);
    one.add(25);
    one.add(51);
    one.add(67);
    one.printValues();
    one.remove();
    one.printValues();
  }
}
