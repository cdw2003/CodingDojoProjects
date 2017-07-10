public class HumanTest {
  public static void main(String[] args) {
    Human a = new Human();
    Human b = new Human();

    a.attack(b);

    Wizard one = new Wizard();
    one.heal(b);
    one.throwFireball(a);

    Ninja two = new Ninja();
    two.steal(one);
    two.runAway();

    Samurai three = new Samurai();
    Samurai four = new Samurai();
    three.deathBlow(two);
    three.meditate();
    Samurai.howMany();
  }
}
