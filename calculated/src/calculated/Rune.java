package calculated;

public class Rune {
	int runeId;
	double[] statMod;
	int count;
	
	public Rune(int rId, int stat, double by){
		runeId = rId;
		statMod = new double[17];
		for(int i = 0; i < 17; i++){
			statMod[i] = 0;
		}
		statMod[stat] = by;
	}
	
	public void setCount(int c){
		count = c;
	}
	
	public double[] stat() {
		return statMod;
	}
	
	public int key(){
		return runeId;
	}
}
