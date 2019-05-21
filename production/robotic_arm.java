public class robotic_arm {
	private int ID;

	public robotic_arm() {

	}

	public robotic_arm(int ID) {
		this.ID = ID;
	}

	public int getID() {
		return ID;
	}

	public void setID(int iD) {
		ID = iD;
	}

	public static void start() {
		System.out.println("正在开机");
	}

	public static void move1() {
		System.out.println("移动到位置1");
	}

	public boolean get(int x) {
		if (x > 0 && x < 20) {
			System.out.println("抓取成功");
			return true;
		} else {
			System.out.println("抓取失败");
			return false;
		}
	}

	public static void move2() {
		System.out.println("移动到位置2");
	}

	public static void release() {
		System.out.println("释放物体");
	}

	public static void stop() {
		System.out.println("已经停止");
	}

}
