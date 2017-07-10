import java.util.*;

public abstract class PokemonAbstract implements OperatePokemon{

  public Pokemon createPokemon(String name, String type, int health){
        Pokemon pokemon = new Pokemon(name, type, health);
        return pokemon;
  }

  public void attackPokemon(Pokemon pokemon){
      pokemon.health -= 10;
      System.out.println("You were attacked and your health is now " + pokemon.health);
  }
}
