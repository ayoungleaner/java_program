
public class set_top_box {
    private int ID;
    private String category;
    private boolean flag;
    private int stb_site;
     
     public int getStb_site() {
		return stb_site;
	}
	public void setStb_site(int stb_site) {
		this.stb_site = stb_site;
	}
	public set_top_box(){
    	 
     }
     public set_top_box(int ID,String category,boolean flag,int stb_site){
    	 this.flag=flag;
    	 this.ID=ID;
    	 this.category=category;
    	 this.stb_site=stb_site;
     }
	public int getID() {
		return ID;
	}
	public void setID(int ID) {
		this.ID = ID;
	}
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public boolean isFlag() {
		return flag;
	}
	public void setFlag(boolean flag) {
		this.flag = flag;
	}
     
}
