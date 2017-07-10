import java.util.*;

public class Human{
  protected int strength = 3;
  protected int stealth = 3;
  protected int intelligence = 3;
  protected int health = 100;

  public void attack(Human human){
    human.health -= this.strength;
    System.out.println("Attacked another human and their health is decreased by " + this.strength);
  }
}
