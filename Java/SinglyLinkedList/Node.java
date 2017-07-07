public class Node{
  public int value;
  public Node next;

  public Node(int value){
    this.value = value;
    this.next = null;
  }

  public void setNext(Node next){
        this.next = next;
  }

  public void setValue(int value){
        this.value = value;
  }

  public Node getNext(){
        return this.next;
  }

  public int getValue(){
        return this.value;
  }
}
