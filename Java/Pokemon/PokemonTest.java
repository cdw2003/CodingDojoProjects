public class PokemonTest {
  public static void main(String[] args) {
    Pokedex a = new Pokedex();
    Pokedex b = new Pokedex();
    a.createPokemon("Emily", "Bug", 100);
    b.createPokemon("Flor", "Dragon", 50);

    a.attackPokemon(b);
    b.attackPokemon(c);

    Pokedex.pokemonInfo(a);
    Pokedex.pokemonInfo(b);
  }
}
