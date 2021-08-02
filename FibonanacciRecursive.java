public class FibonanacciRecursive {
	public static void main(String[] args) {
		System.out.println(fibonacci(5));
	}
	
	// Main function
	public static int fibonacci(int n) {
		return fibonacciRecursive(n, new int[n + 1]);
	}
	
	// Helper function
	public static int fibonacciRecursive(int n, int[] array) {
		if (n == 0 || n == 1) {
			return 1;
		}
		
		// Memoization
		if (array[n] == 0) {
			int result = fibonacciRecursive(n - 2, array) + fibonacciRecursive(n - 1, array);
			array[n] = result;
		}
		return array[n];
	}
}
