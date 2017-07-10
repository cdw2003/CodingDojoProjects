import java.util.*;

public class Pokemon{
  protected String name;
  protected int health;
  protected String type;
  protected static int countPokemon = 0;

  public Pokemon(){
  }

  public Pokemon(String name, String type, int health){
    this();
    this.name = name;
    this.type = type;
    this.health = health;
    countPokemon ++;
  }

  public void setName(String name){
    this.name = name;
 }

  public String getName(){
     return name;
  }

  public void setHealth(int health){
    this.health = health;
  }

   public int getHealth(){
      return health;
  }

  public void setType(String type){
    this.type = type;
  }

  public String getType(){
     return type;
  }

  public static int getCountPokemon(){
    System.out.println("There are: " + countPokemon + " Pokemon.");
    return countPokemon;
  }
}
