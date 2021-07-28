public class FibonanacciRecursive {
	public static void main(String[] args) {
		fibonacciRecursive(5);
	}

	public static int fibonacciRecursive(int n) {
		if (n == 0 || n == 1) {
			return 1;
		}
		return fibonacciRecursive(n - 2) + fibonacciRecursive(n - 1);
	}
}
