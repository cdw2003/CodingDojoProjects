import java.util.*;

public class Samurai extends Human{

  protected int health = 200;
  protected static int counter;

  public Samurai(){
     counter ++;
  }

  public void deathBlow(Human human){
    human.health = 0;
    this.health = this.health/2;
    System.out.println("Dealt a death blow to another human and they are dead and my health is now " + this.health);
  }

  public void meditate(){
    this.health = 200;
    System.out.println("Ran away and now my health is " + this.health);
  }

  public static int howMany(){
    System.out.println("There are "+ counter + " Samurai.");
    return counter;
  }
}
