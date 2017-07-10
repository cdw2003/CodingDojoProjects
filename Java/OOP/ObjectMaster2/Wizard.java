import java.util.*;

public class Wizard extends Human{

  protected int health = 50;
  protected int intelligence = 8;

  public void heal(Human human){
    human.health += this.intelligence;
    System.out.println("Healed another human and their health is increased by " + this.intelligence);

  }

  public void throwFireball(Human human){
    human.health -= this.intelligence;
    System.out.println("Threw a fireball at another human and their health is decreased by " + this.intelligence);

  }
}
