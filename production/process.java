public class process {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		robotic_arm ra = new robotic_arm(1);
		set_top_box stb = new set_top_box();
		int count = 0;

		ra.start();//开机
		for(int i=0;i<++i;){
		ra.move1();//发现机顶盒，给机顶盒各个属性赋值
		//判断是否合格，合格直接跳过
		if(stb.isFlag()==true){
		count++;
	    continue;
		}
		
		if(ra.getinfo(stb.getID())==false){//抓取扫描，需要判断扫描信息类型是否符合
		continue;
		}
		int info=ra.saveinfo(stb.getID());//存储信息
		ra.move2();//抓机顶盒到置具仓
		ra.rotate_hand1();//旋转插入电源
		ra.rotate_move();//抓取移至缓存空余区，后需要一个判断机顶盒工作时间
		//if(stb_work_time>10)...,else,continue
		ra.move2();//抓取抓机顶盒到置具仓
		ra.rotate_hand2();//旋转抓手，插入接口
		if(ra.checkinfo(info, stb.getID())==false){//核对信息，如果错误转入不合格区
		continue;
		}
		ra.release();//拔出接口和电源
		ra.rorate_hand3();//旋转抓手，抓取移至皮带轮
		count++;
		}
		System.out.println("共生产了" + count + "个");
	}

}
