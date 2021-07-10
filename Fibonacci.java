public class Fibonacci {
	
	
	public static void main(String[] args) {
		// fibonacci(n);
	}

	public static int fibonacci(int n) {
		int first = 0;
		int second = 1;
		for (int i = 0; i < Math.abs(n); i++) {
			int temp = first + second;
			first = second;
			second = temp;
		}
		if (n >= -1 || n % 2 == -1) {
			return first;
		} else {
			return -first;
		}
	}
}
