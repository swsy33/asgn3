public class ClosestHeuristic implements AStarHeuristic {
	/**
	 * @see AStarHeuristic#getCost(TileBasedMap, Mover, int, int, int, int)
	 */
	public double getCost(MarsMatrix map, Mover mover, int x, int y, int tx, int ty) {		
		double dx = tx - x;
		double dy = ty - y;
		
		double result = (double) (Math.sqrt((dx*dx)+(dy*dy)));
		
		return result;
	}
}
