
public class Test {

	public static void main(String[] args) throws Exception{   
		String filename = "/Users/sandra/Desktop/asgn3/map.txt";
		MapConverter mc = new MapConverter(filename);
		MarsMatrix mm = new MarsMatrix(mc.getMatrix());
		System.out.println("Original map: ");
		mc.printMatrix();
		AStar as = new AStar();
		//A-B
		as.test(1, mm, 16, 1, 16, 31);
		System.out.println("length of the path A-B: " + as.getPathLength(mm, 16,1,16,31));
		//A-C
		as.test(2, mm,16,1, 0,24);   
		System.out.println("length of the path A-C: " + as.getPathLength(mm, 16,1,0,24));
	}

}
