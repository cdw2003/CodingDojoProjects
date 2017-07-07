import java.util.*;

public class Ninja extends Human{

  protected int stealth = 10;

  public void steal(Human human){
    human.health -= this.stealth;
    this.health += this.stealth;
    System.out.println("Stole from another human and their health is now " + human.health);

  }

  public void runAway(){
    this.health -= 10;
    System.out.println("Ran away and now my health is " + this.health);
  }
}
