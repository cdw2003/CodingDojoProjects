import java.util.*;

public class Dragon extends Mammal{

  protected int energyLevel = 300;

  public void displayEnergy(){
    System.out.println("My energy level is:" + energyLevel);
  }

  public int fly(){
    System.out.println("Arrrghhh.");
    energyLevel -= 50;
    return energyLevel;
  }

  public int eatHumans(){
    System.out.println("So well. Never mind.");
    energyLevel += 25;
    return energyLevel;
  }

  public int attackTown(){
    System.out.println("Whooosh.");
    energyLevel -= 100;
    return energyLevel;
  }
}
