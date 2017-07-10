public class PokemonTest{
  public static void main(String[] args){
    Pokedex pokedex = new Pokedex();

    Pokemon pikachu = new Pokemon("pikachu", "electric", 120);
    Pokemon eevee = new Pokemon("eevee", "normal", 85);
    Pokemon rowlet = new Pokemon("rowlet", "grass", 50);
    Pokemon bulbasaur = new Pokemon("bulbasaur", "grass", 30);

    pokedex.pokemonInfo(bulbasaur);
    pokedex.pokemonInfo(rowlet);
    pokedex.pokemonInfo(pikachu);

    pokedex.attackPokemon(pikachu);
    pokedex.pokemonInfo(pikachu);

    Pokemon.getCountPokemon();
  }
}
