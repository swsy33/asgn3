public class ManhattanHeuristic implements AStarHeuristic {
	/** The minimum movement cost from any one square to the next */
	private int minimumCost;
	
	/**
	 * Create a new heuristic 
	 * 
	 * @param minimumCost The minimum movement cost from any one square to the next
	 */
	public ManhattanHeuristic(int minimumCost) {
		this.minimumCost = minimumCost;
	}
	
	public float getCost(MarsMap map, Mover mover, int x, int y, int tx, int ty) {
		return minimumCost * (Math.abs(x-tx) + Math.abs(y-ty));
	}

}