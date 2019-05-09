
public class beltspeed1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double distance=230.6;
		double t1=1557220369.6709645 ;
		double t2=1557220373.4141524;
		double belt_v=distance/(Math.abs(t1-t2));
		System.out.println("皮带速度大约为"+belt_v);

	}

}
