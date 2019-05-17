import java.util.Scanner;

public class process2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arry[][] = new int[][] { { 1, 0 }, { 1, 0 }, { 1, 0 }, { 1, 0 } };
		// 模拟某个时间有部分目标完成
		for (int i = 0; i < 4; i++) {
			comeplete(i, arry);
		}
		// 判断是否需要取出和再次放入
		for (int i = 0; i < 4; i++) {
			if (arry[i][1] == 1) {
				reduce(i, arry);
				System.out.println("是否继续放置机顶盒：(0或1)");
				Scanner sc = new Scanner(System.in);
				int x = sc.nextInt();
				if (x == 1) {
					add(i, arry);
				} else {
					free(i);
				}
			}
		}
	}

	public static void reduce(int i, int[][] arry) {
		// TODO Auto-generated method stub
		System.out.println("buffer" + i + "已经完成，正在取走机顶盒");
		arry[i][0] = 0;
		arry[i][1] = 0;
	}

	public static void add(int i, int[][] arry) {
		// TODO Auto-generated method stub
		System.out.println("正在为buffer" + i + "添加机顶盒");
		arry[i][0] = 1;
		System.out.println("buffer" + i + "添加机顶盒成功");

	}

	public static void free(int i) {
		System.out.println("buffer" + i + "已闲置");
	}

	public static void comeplete(int i, int[][] arry) {
		arry[i][1] = (int) (Math.random() + 0.5);
	}

}
