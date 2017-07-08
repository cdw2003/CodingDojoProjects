import java.util.*;

class Pokedex extends PokemonAbstract{

    public ArrayList<String> pokemonInfo(Pokemon pokemon){
        ArrayList<String> info = new ArrayList<String>();
        info.add(pokemon.name);
        info.add(pokemon.type);
        info.add(String.valueOf(pokemon.health));
        System.out.println("Your name is: " + pokemon.name + " Your type is: "+ pokemon.type + " You health is: " + pokemon.health);
        return info;
    }
  }
