package calculated;

public class frequencyObject {
	int freq;
	int id;
	
	public frequencyObject(int x, int y ){
		id = x;
		freq = y; 
		
	}
	
	public int getFreq(){
		return freq;
	}
	public int getId(){
		return id;
	}
	public void setFreq(int newFreq){
		freq = newFreq;
	}
}
