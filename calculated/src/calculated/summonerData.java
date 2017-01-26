package calculated;

import org.json.*;

public class summonerData {
	
	JSONObject summonerInfo;
	int summonerId;
	String summonerName;
	
	public summonerData(JSONObject sI, String sn) throws JSONException {
		summonerInfo = sI;
		summonerName = sn;
		summonerId = summonerInfo.getJSONObject(sn).getInt("id");
	}
	
	// we could have an api call here that gets the player's rank
}
