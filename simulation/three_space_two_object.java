
public class three_space_two_object {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//定义一个二维数组，表示100次3个位置的情况
      int arry[][] = new int[100][3];
      //初始化起始都没有物体
       arry[0][0]=0;
       arry[0][1]=0;
       arry[0][2]=0;
       //循环100次，每个位置的变化情况
       for(int i=1;i<20;i++){
    	   //1号为如果为0则第二次必定为1
    	   if( arry[i-1][0]==0){
    		   arry[i][0]=1;
    	   }else{
    	   arry[i][0]=(int)(Math.random()+0.5);
    	   }
    	   //保证存在2个物体，
    	   if(arry[i][0]==0){
    		   arry[i][1]=1;
    		   arry[i][2]=1;
    	   }else{
    		   arry[i][1]=(int)(Math.random()+0.5);
    		   //保证1号位相同的情况下2号位相邻2次不同
    		   while(arry[i][1]==arry[i-1][1]){
    			   arry[i][1]=(int)(Math.random()+0.5);
    		   }
    		   arry[i][2]=2-arry[i][1]-arry[i][0];
    	   }
    	   System.out.println("第"+i+"次工作后3个位置的情况为"+"("+arry[i][0]+","+arry[i][1]+","+arry[i][2]+")");
    	   //位置变化，0不变，1获得目标，-1失去目标
    	   int a=arry[i][0]-arry[i-1][0];
    	   int b=arry[i][1]-arry[i-1][1];
    	   int c=arry[i][2]-arry[i-1][2];
    	   System.out.println("1号为情况"+a+","+"1号为情况"+b+","+"1号为情况"+c);
       }
    
	}

}
