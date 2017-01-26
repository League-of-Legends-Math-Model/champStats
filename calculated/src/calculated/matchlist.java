package calculated;

import org.json.*;

public class matchlist {
	JSONObject matchList;
	JSONArray matches;
	long[] matchIds;
	int champId;
	int summonerId;
	int totalGames;
	// Potentially an arraylist of matchdatas?
	
	public long[] getIds(){
		return matchIds;
	}
	
	private void extractMatchIds() throws JSONException {
		if (totalGames > 0){
			int measuredGames = totalGames;
			if (totalGames > 25){
				measuredGames = 25;
			}
			matchIds = new long[measuredGames];
			for (int i = 0; i < measuredGames; i++){
				matchIds[i] = matches.getJSONObject(i).getLong("matchId");
			}
		}
	}
	
	public matchlist(JSONObject mL, int sId, int cId) throws JSONException {
		matchList = mL;
		summonerId = sId;
		champId = cId;
		totalGames = matchList.getInt("totalGames");
		matches = matchList.getJSONArray("matches");
		extractMatchIds();
	}
}
