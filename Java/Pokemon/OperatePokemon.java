import java.util.*;

public interface OperatePokemon{
  Pokemon createPokemon(String name, String type, int health);

  void attackPokemon(Pokemon pokemon);

  void pokemonInfo(Pokemon pokemon);
}
