public class PokemonTest{
  public static void main(String[] args){
    Pokedex pokedex = new Pokedex();

    Pokemon pikachu = pokedex.createPokemon("pikachu", "electric", 120);
    Pokemon eevee = pokedex.createPokemon("eevee", "normal", 85);
    Pokemon rowlet = pokedex.createPokemon("rowlet", "grass", 50);
    Pokemon bulbasaur = pokedex.createPokemon("bulbasaur", "grass", 30);

    pokedex.pokemonInfo(bulbasaur);
    pokedex.pokemonInfo(rowlet);
    pokedex.pokemonInfo(pikachu);

    pokedex.attackPokemon(pikachu);
    pokedex.pokemonInfo(pikachu);

    Pokemon.getCountPokemon();
  }
}
