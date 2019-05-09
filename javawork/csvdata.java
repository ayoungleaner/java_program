
import java.io.BufferedReader;
	import java.io.FileReader;
	public class csvdata {
		/**
		 * arm:获取.csv文件的某一行某一列数据的内容
		 * 
		 * 
		 */
	    
	   public static void main(String[]args){ 	
	    	double last=0.00;
	          try {           
	           BufferedReader reade = new BufferedReader(new FileReader("/home/ubuntu/javaspeedtext/stb_labels.csv"));//换成你的文件名             
	           String line = null;
	           int index=0;
	           int col=7;
	           while((line=reade.readLine())!=null){
	               String item[] = line.split(",");//CSV格式文件为逗号分隔符文件，这里根据逗号切分
	               for(int row=2;row<109;row++){
	            if(index==row-1){
	            	//System.out.println(item.length);
	                if(item.length>=col-1){
	                   // String last = item[col-1];//这就是你要的数据了
	                    //int  value = Integer.parseInt(last);
	                      last+=Double.parseDouble(item[col-1])-Double.parseDouble(item[col-3]);//差求和
	                    //System.out.println(last); 
	                    
	                }
	            }
	                
	         }
	            
	            
	            index++;
	            } 
	          
	           } catch (Exception e) {
	            e.printStackTrace();
	            }
	           
	           
	    
 
	    
	           System.out.println(last/107);  
	    }
	}
	

