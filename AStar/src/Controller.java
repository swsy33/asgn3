
public class Controller {

	public static void main(String[] args) {
		//original matrix with A B and C
		String filename = "/Users/sandra/Desktop/asgn3/map.txt";
		MapConverter mc = new MapConverter(filename);
		mc.printMatrix();
		
		//find shortest path from Start to Goal
		//admissible - closetHeursitic
		//non-admissible - ManhattanHeuristic

	}

}
