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
		System.out.println("移动到位置1，发现机顶盒");
	}

	public boolean getinfo(int stb_id) {
		if (stb_id > 0 ) {
			System.out.println("抓取，扫描成功");
			return true;
		} else {
			System.out.println("抓取扫描失败,移至不合格区");
			return false;
		}
	}
	public int saveinfo(int stb_id){
		return stb_id;
	}
    public static void move2(){
    	System.out.println("移动至置具仓，释放，置具仓夹紧");
    }
	public static void rotate_hand1() {
		System.out.println("旋转抓手，插入电源");
	}

	public static void rotate_move() {
		System.out.println("旋转抓手，抓取机顶盒，移至空余缓冲区");
	}
	public static void rotate_hand2(){
		System.out.println("旋转抓手，插入接口模块");
	}
	public boolean checkinfo(int save_id,int stb_id){
		if(save_id==stb_id){
			System.out.println("核对无误");
			return true;
		}else{
			System.out.println("核对有误，移至不合格区");
			return false;
		}	
	}
	public static void release(){
		System.out.println("拔出接口模块，拔出电源");
	}
	public static void rorate_hand3(){
		System.out.println("旋转抓手，抓取机顶盒到皮带轮");
	}

	public static void stop() {
		System.out.println("已经停止");
	}

}
