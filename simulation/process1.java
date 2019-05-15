public class process1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arry[][] = new int[][] { { 0, 0 }, { 0, 0 }, { 0, 0 }, { 0, 0 } };

		for (int i = 0; i < 4; i++) {
			if (arry[i][0] == 0) {
				System.out.println("正在为buffer" + i + "添加机顶盒");
				arry[i][0] = 1;
				System.out.println("buffer" + i + "添加机顶盒成功");
			}

		}

	}
}
