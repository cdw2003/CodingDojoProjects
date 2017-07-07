public class ProjectTest {
    public static void main(String[] args) {
        Project a = new Project();
        a.setName("ProGetter");
        a.setDescription("Applied learning platform for middle schoolers");
        a.setCost(2500.25f);
        a.elevatorPitch();

        Project b = new Project();
        b.setName("UdemyCourse");
        b.setDescription("A course on user experience in digital products");
        b.setCost(100.50f);
        b.elevatorPitch();

        Project c = new Project("NewProject", "Building my coding skills at Coding Dojo", 11000.75f);
        c.elevatorPitch();

        Portfolio portfolio = new Portfolio();
        portfolio.addProjects(a);
        portfolio.addProjects(b);
        portfolio.addProjects(c);
        portfolio.showPortfolio();

  }
}
