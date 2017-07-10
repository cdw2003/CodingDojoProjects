import java.util.*;

public class Portfolio{
  private ArrayList<Project> projects = new ArrayList<>();

  public Portfolio(){
  }

  public void addProjects(Project project){
    projects.add(project);
  }

  public ArrayList<Project> getProjects(){
    return projects;
  }

  public float getPortfolioCost(){
    float sum = 0;
    for(Project project: projects){
      sum = sum + project.getCost();
    }
    return sum;
  }

  public void showPortfolio(){
    for(Project project: projects){
      project.elevatorPitch();
    }
  System.out.println("\nTotal Cost: $" + this.getPortfolioCost());
  }
}
