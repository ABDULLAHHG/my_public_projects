public class Main {
	
	static void printUpperMatrix(int[][] squareArray) {
		int length = squareArray.length;
		
		for (int i = 0; i < length; i++) {
			for (int j = i + 1; j < length; j++) {
				System.out.print(squareArray[i][j] + "\t");
			}
			System.out.println();
		}
	}
	
	static void printBottomMatrix(int[][] squareArray) {
		int length = squareArray.length;
		
		for (int i = 1; i < length; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print(squareArray[i][j] + "\t");
			}
			System.out.println();
		}
	}
	
	static void print3dArray(int[][][] array3D ){
        System.out.print("\n");

        for (int i = 0; i < array3D.length; i++) {
			for (int j = 0; j < array3D[i].length; j++) {
                for (int k = 0; k<array3D[i][j].length;k++){
                    System.out.print(array3D[i][k][j] + "\t");
                }
                System.out.print("\n");
            }
            System.out.print("\n\n\n");
        }
    }
    static void print2dArray(int[][] array2D ){
        System.out.print("\n");

        for (int i = 0; i < array2D.length; i++) {
			for (int j = 0; j < array2D[i].length; j++) {
           
                    System.out.print(array2D[i][j] + "\t");
                }
                System.out.print("\n");
          
        }
    }

	public static void main(String[] args) {
    
        int [][][] array3D = {
            {
                {1,2,3},
                {4,5,6},
                {7,8,9}
            },
            {
                {1,2,3},
                {4,5,6},
                {7,8,9}
            },

        };
        
		int[][] squareMatrix = {
			{1, 2, 3, 4, 5},
			{1, 2, 3, 4, 5},
			{1, 2, 3, 4, 5},
			{1, 2, 3, 4, 5},
			{1, 2, 3, 4, 5}
		};

        System.out.println("\nPrint Upper Tringle matrix");
		printUpperMatrix(squareMatrix);

        System.out.println("\nPrint Lower Tringle matrix");
		printBottomMatrix(squareMatrix);

        System.out.println("\nPrint 3D Matrix");
        print3dArray(array3D);
    
        int[][] matrix = {
			{1, 2, 3, 4, 5},
			{1, 2, 3, 4},
			{1, 2, 3},
			{1, 2},
			{1, }
		};
        System.out.println("\nPrint Matrix with diffrent shape");
        print2dArray(matrix);
    

    }
}
