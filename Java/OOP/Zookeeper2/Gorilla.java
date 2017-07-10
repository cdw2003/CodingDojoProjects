import java.util.*;

public class Gorilla extends Mammal{

  public int throwFood(){
    System.out.println("The gorilla has thrown a pineapple.");
    energyLevel -= 5;
    return energyLevel;
  }

  public int eatBananas(){
    System.out.println("The gorilla is full now.");
    energyLevel += 10;
    return energyLevel;
  }

  public int climb(){
    System.out.println("The gorilla has climbed a tree.");
    energyLevel -= 10;
    return energyLevel;
  }
}
