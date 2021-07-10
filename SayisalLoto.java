import java.util.Random;
import java.util.LinkedList;

class SayisalLoto {
	
	public static void main(String[] args) {
		System.out.println(sayisalLoto());
	}

	public static LinkedList<Integer> sayisalLoto() {
		Random rnd = new Random();
		int numbers = 0;
		LinkedList<Integer> lnk = new LinkedList<>();

		while (numbers < 6) {
			int draw = rnd.nextInt(49) + 1;
			if (lnk.contains(draw)) {
				continue;
			}
			lnk.add(draw);
			numbers++;
		}
		return lnk;
	}
}
