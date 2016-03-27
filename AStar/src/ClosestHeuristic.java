public class ClosestHeuristic implements AStarHeuristic {
	
	public double getCost(Mover mover, int x, int y, int tx, int ty) {		
		double dx = tx - x;
		double dy = ty - y;
		
		double result = (double) (Math.sqrt((dx*dx)+(dy*dy)));
		
		return result;
	}
}
