package calculated;

import org.json.*;

public class masterySet {
	JSONArray mastery;
	double[] flatStatMods;
	double[] perStatMods;
	int[][] masteries;
	
	/*	stats
	 * 	0 = hp
	 *  1 = ad
	 *  2 = adperlevel
	 *  3 = ap
	 *  4 = apperlevel
	 *  
	 *  0 = bonus armor
	 *  1 = bonus mr
	 *  2 = cdr
	 *  3 = summoner cdr
	 *  4 = attack speed
	 */
	private void populateMastery() throws JSONException {
		masteries = new int[mastery.length()][2];
		
		for (int i = 0; i < mastery.length(); i++) {
			masteries[i][0] = mastery.getJSONObject(i).getInt("masteryId");
			masteries[i][1] = mastery.getJSONObject(i).getInt("rank");
		}
		
		for (int i = 0; i < masteries.length; i++) {
			switch(masteries[i][0]){
			case 6241:
				perStatMods[3] = .85;
				break;
			case 6232:
				flatStatMods[0] = 10 * masteries[i][1];
				break;
			case 6134:
				flatStatMods[1] = 0.4 * masteries[i][1];
				flatStatMods[2] = (1.6 * masteries[i][1]) / 18;
				flatStatMods[3] = 0.6 * masteries[i][1];
				flatStatMods[4] = (2.4 * masteries[i][1]) / 18;
				break;
			case 6111:
				perStatMods[4] = .008 * masteries[i][1];
				break;
			case 6352:
				perStatMods[2] = .01 * masteries[i][1];
				break;
			case 6212:
				perStatMods[0] = .01 * masteries[i][1];
				perStatMods[1] = .01 * masteries[i][1];
				break;
			default:
			}
		}
	}
	
	public double[] getFlat(){
		return flatStatMods;
	}
	
	public double[] getPer(){
		return perStatMods;
	}
	}
	
	public masterySet(JSONArray ms) throws JSONException {
		mastery = ms;
		flatStatMods = new double[5];
		perStatMods = new double[5];
		for (int i = 0; i < 5; i++){
			flatStatMods[i] = 0;
			perStatMods[i] = 1;
		}
		populateMastery();
	}
}
