import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
/*convert graph file into 2D array*/
public class MapConverter {
	String[][] graph;
	int rowSize;
	int colSize;
	public MapConverter(String filename)
	{
		sizeOfMatrix(filename);
		this.graph = data(filename);
	}

	private void sizeOfMatrix(String filename) 
	{
		int row = 0;
		int col = 0;
		try(BufferedReader br = new BufferedReader(new FileReader(filename))) 
		{

			//StringBuilder sb = new StringBuilder();
			String line = br.readLine();
			while(line != null)
			{
				++row;
				String newline = line.trim().replaceAll("\\s", "");
				//System.out.println(newline);
				String[] rowData = newline.split("");
				if(rowData.length > col)
					col = rowData.length;
				line = br.readLine();
			}
			System.out.println("row # and col #: " + row + ", " +col );
			br.close();
			this.rowSize = row;
			this.colSize = col;

		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("no file exits!");
		}

	}

	//input data into 2D array
	private String[][] data(String filename)
	{
		String[][] result = new String[this.rowSize][this.colSize];
		try(BufferedReader br = new BufferedReader(new FileReader(filename))) 
		{
			String line = br.readLine();
			int row = 0;
			while (line != null && row < this.rowSize) 
			{
				//each char into 2D array
				//System.out.println(line);
				String[] singleRow = line.trim().replaceAll("\\s", "").split("");
				//System.out.println(singleRow[row]);
				for(int i = 0; i < singleRow.length; i++)
				{
					//System.out.print(singleRow[i]);
					result[row][i] = singleRow[i];
				}
				line = br.readLine();
				row++;
			}
		
		} catch (IOException e) {
			System.out.println("exception in data");
		}
		return result;
	}
	
	public void printMatrix()
	{
		for(int i = 0; i < this.rowSize; i++)
		{
			for(int j = 0; j< this.colSize; j++)
			{
				System.out.print(this.graph[i][j]);
			}
			System.out.print("\n");
		}
	}

}
