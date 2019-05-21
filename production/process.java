public class process {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		robotic_arm ra = new robotic_arm(1);
		set_top_box stb = new set_top_box();
		int count = 0;

		ra.start();
        for(int i=0;i<++i;){
        	int l=(int)(Math.random()*20);
        	System.out.println(l);
        	stb.setStb_site(l);
		ra.move1();

		if (ra.get(stb.getStb_site()) == true) {
			ra.move2();
			ra.release();
			count++;
		} else {
			ra.stop();
			break;
		}
        }
		System.out.println("共生产了" + count + "个");
	}

}
