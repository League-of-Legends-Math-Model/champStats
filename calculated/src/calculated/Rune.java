package calculated;

public class Rune {
	int runeId;
	double[] statMod;
	int count;
	int initialS;
	double initialB;
	
	public Rune(int rId, int stat, double by){
		runeId = rId;
		initialS = stat;
		initialB = by;
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
	
	public boolean isFlat() {
		double tester = 0;
		boolean yesFlat = false;
		for (int i = 0; i < 14; i++){
			tester += statMod[i];
		}
		if (tester > 0){
			yesFlat = true;
		}
		return yesFlat;
	}
	
	public int key(){
		return runeId;
	}
}
