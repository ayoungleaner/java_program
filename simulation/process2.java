import java.util.Scanner;


public class process2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
          int arry[][]=new int[][]{{1,0},{1,0},{1,0},{1,0}};
          //模拟某个时间有部分目标完成
          for(int i=0;i<4;i++){
        	  arry[i][1]=(int)(Math.random()+0.5);
          }
          //判断是否需要取出和再次放入
          for(int i=0;i<4;i++){
        	  if(arry[i][1]==1){
        		  System.out.println("buffer"+i+"已经完成，正在取走机顶盒");
        		  arry[i][0]=0;
        		  arry[i][0]=0;
        		  System.out.println("是否继续放置机顶盒：(0或1)");
        		  Scanner sc=new Scanner(System.in);
        		  int x=sc.nextInt();
        		  if(x==1){
        			  System.out.println("buffer"+i+"正在放置机顶盒");
        			  arry[i][0]=1;
        			  System.out.println("buffer"+i+"放置机顶盒成功");
        		  }else{
        			  System.out.println("buffer"+i+"已闲置");
        		  }
        	  }
          }
	}

}
