package calculated;

import java.util.ArrayList;

import org.json.*;

public class runeSet {
	JSONArray runes;
	
	double[] flatRuneMod;
	double[] perRuneMod;
	int[][] runeData;
	ArrayList<double[]> flatRune;
	ArrayList<double[]> perRune;
	
	public double[] getFlat(){
		return flatRuneMod;
	}
	
	public double[] getPer(){
		return perRuneMod;
	}
	
	private void setRunes() throws JSONException {
		runeData = new int[runes.length()][2];
		
		for (int i = 0; i < runes.length(); i++){
			runeData[i][0] = runes.getJSONObject(i).getInt("runeId");
			runeData[i][1] = runes.getJSONObject(i).getInt("count");
		}
		
	}
	
	private void generateStats(ArrayList<Rune> stats) {
		for (int i = 0; i < runeData.length; i++){
			int lookup = runeData[i][0];
			for (int j = 0; j < stats.size(); j++){
				if (lookup == stats.get(j).key()){
					if (stats.get(j).isFlat()){
						double[] rHelp = stats.get(j).stat();
						for (int k = 0; k < 17; k++){
							rHelp[k] = rHelp[k] * runeData[i][1];
						}
						flatRune.add(rHelp);
					}
					else {
						double[] pHelp = stats.get(j).stat();
						for (int k = 0; k < 17; k++){
							pHelp[k] = pHelp[k] * runeData[i][1];
						}
						perRune.add(pHelp);
					}
				}
			}
		}
		for (int i = 0; i < flatRune.size(); i++){
			for (int j = 0; j < 14; j++){
				flatRuneMod[j] += flatRune.get(i)[j];
			}
		}
		for (int i = 0; i < perRune.size(); i++){
			perRuneMod[14] += perRune.get(i)[14];
			if (perRune.get(i)[15] > 1){
				perRuneMod[15] = perRuneMod[15] * perRune.get(i)[15];
			}
			if (perRune.get(i)[16] > 1){
				perRuneMod[16] = perRuneMod[16] * perRune.get(i)[16];
			}
		}
	}
	
	public runeSet(JSONArray r) throws JSONException {
		runes = r;
		flatRuneMod = new double[17];
		perRuneMod = new double[17];
		flatRune = new ArrayList<double[]>();
		perRune = new ArrayList<double[]>();
		
		for (int i = 0; i < 17; i++){
			flatRuneMod[i] = 0;
			perRuneMod[i] = 0;
		}
		perRuneMod[15] = 1;
		perRuneMod[16] = 1;
		setRunes();
	}
}
