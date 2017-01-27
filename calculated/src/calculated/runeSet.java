package calculated;

import org.json.*;

public class runeSet {
	JSONArray runes;
	
	double[] flatRuneMod;
	double[] perRuneMod;
	int[][] runeData;
	
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
	
	public runeSet(JSONArray r) throws JSONException {
		runes = r;
		setRunes();
	}
}
