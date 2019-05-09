
public class text {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//横向平面坐标点及时间
        double x1=465.63,y1=364.36;
        double x2=235.00,y2=364.36;
        double t1=1557200340.15071,t2=1557200340.930645;
        //计算距离，时间差，及速度
        double distance1=Math.sqrt(Math.abs((x1-x2)*(x1-x2))+Math.abs((y1-y2)*(y1-y2)));
        double tx1=Math.abs(t2-t1);
        double v1=distance1/tx1;
        
        System.out.println("两点之间距离是"+distance1+"\n"+"时间差"+tx1+"\n"+"所需速度"+v1);
       //第一次纵向平面坐标点及时间
        double x3=364.36,y3=-90.00;
        double x4=364.36,y4=0.00;
        double t3=1557200340.930645,t4=1557200342.2738357;
        //计算距离，时间差，及速度
        double distance2=Math.sqrt(Math.abs((x3-x4)*(x3-x4))+Math.abs((y3-y4)*(y3-y4)));
        double tx2=Math.abs(t3-t4);
        double v2=distance2/tx2;
        
        System.out.println("两点之间距离是"+distance2+"\n"+"时间差"+tx2+"\n"+"所需速度"+v2);
      
      //第二次纵向平面坐标点及时间
        double x5=364.36,y5=0.00;
        double x6=364.36,y6=-90.00;
        double t5=1557200342.688715,t6=1557200344.0309398;
        //计算距离，时间差，及速度
        double distance3=Math.sqrt(Math.abs((x5-x6)*(x5-x6))+Math.abs((y5-y6)*(y5-y6)));
        double tx3=Math.abs(t5-t6);
        double v3=distance3/tx3;
        
        System.out.println("两点之间距离是"+distance3+"\n"+"时间差"+tx3+"\n"+"所需速度"+v3);
      
	}
    
}
