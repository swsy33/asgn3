
public class Test {

	public static void main(String[] args) throws Exception{   
		String filename = "/Users/sandra/Desktop/asgn3/map.txt";
		MapConverter mc = new MapConverter(filename);
		MarsMatrix mm = new MarsMatrix(mc.getMatrix());
		//mc.printMatrix();
		AStar as = new AStar();
		as.test(1, mm, 16, 1, 16, 31);
		as.test(2, mm,16,1, 0,24);   

	}

}