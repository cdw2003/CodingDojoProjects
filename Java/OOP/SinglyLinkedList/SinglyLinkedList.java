import java.util.*;

public class SinglyLinkedList{
  private Node head;

  public SinglyLinkedList(){
    this.head = null;
  }

  public Node add(int value){
    if(this.head == null){
      this.head = new Node(value);
      return this.head;
    }
    Node pointer = this.head;
    while(pointer.next != null){
        pointer = pointer.next;
    }
    pointer.next = new Node(value);
    return this.head;
  }

  public Node remove(){
    Node pointer = this.head;
    while(pointer.next.next != null){
        pointer = pointer.next;
    }
    pointer.next = null;
    return this.head;
  }

  public void printValues(){
    ArrayList<Integer> sll = new ArrayList<>();
    Node pointer = this.head;
    if(this.head != null){
      while(pointer.next != null){
        sll.add(pointer.getValue());
        pointer = pointer.next;
      }
    }
    System.out.println(sll);
  }
}
