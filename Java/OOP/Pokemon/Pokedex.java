import java.util.*;

public class Pokedex extends PokemonAbstract{

    public void pokemonInfo(Pokemon pokemon){
        System.out.println("Your name is: " + pokemon.getName() + " Your type is: "+ pokemon.getType() + " Your health is: " + pokemon.getHealth());
    }
  }
