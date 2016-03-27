public class MarsMatrix{

	int width = 0;
	int height = 0;
	private String[][] marsMatrix; 

	public MarsMatrix(String[][] matrix) {

		this.height = matrix.length;
		this.width = matrix[0].length;
		//System.out.println("this height " + this.height + " this wdith " + this.width);
		this.marsMatrix = matrix.clone();

	}

	public int[] findCell(String content)
	{
		int[] result = new int[2];
		for(int y = 0; y < this.height; y++)
		{
			for( int x = 0; x< this.width; x++)
			{
				if (getCell(y,x).equals(content))
				{
					System.out.println("! " + getCell(y,x));
					result[0] = y;
					result[1] = x;
				}
				
			}
		}
		return result;
	}
	
	public void replaceCell(int x, int y, String replacewith)
	{
		this.marsMatrix[x][y] = replacewith;
	}
	
	public MarsMatrix copy()
	{
		MarsMatrix nmm = new MarsMatrix(this.marsMatrix);
		return nmm;
	}
	
	public String getCell(int x, int y)
	{
		//System.out.println("marsmatrix 56 " + y + "  " + x + this.marsMatrix[y][x]);
		return this.marsMatrix[x][y];
	}

	public double getCost(int sx, int sy, int tx, int ty )
	{
		return 1;
	}
	
	public boolean blocked(int x, int y) {
		// if theres a "X" at the location, then it's blocked or Obstacle
		if (getCell(x,y).equals("X")) {
			//System.out.println("Obstacle!!!");
			return true;
		}
		else
		{
			//System.out.println("Not Obstacle!!!");
			return false;
		}
	}

	public int getHeightInMatrix() {
		return this.height;
	}


	public int getWidthInMatrix() {
		return this.width;
	}



}