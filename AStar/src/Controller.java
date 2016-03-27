
public class Controller {

	public final static String START = "A";
	public final static String GOAL1 = "B";
	public final static String GOAL2 = "C";
	public static void main(String[] args) {
		//original matrix with A B and C
		String filename = "/Users/sandra/Desktop/asgn3/map.txt";
		MapConverter mc = new MapConverter(filename);
		mc.printMatrix();
		
		
		//find shortest path from Start to Goal
		//admissible - closetHeursitic
		//non-admissible - ManhattanHeuristic
		MarsMatrix mm = new MarsMatrix(mc.getMatrix());
		int[] start = mm.findCell(START);
		//System.out.println("start0 " +start[0] + "start1 +" + start[1]);
		int[] goal1 = mm.findCell(GOAL1);
		//int[] goal2 = mm.findCell(GOAL2);
		
		boolean admissible = true;
		boolean diagonal = admissible;
		
		AStarPathFinder aspf = new AStarPathFinder(mm, diagonal);
		Mover mover = new Mover();
		Path path = aspf.findPath(mover, start[0], start[1], goal1[0], goal1[1]);
		System.out.println("length of path from A to B is " + path.getLength());
		
	}

}
