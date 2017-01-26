package calculated;

import org.json.*;

public class matchdata {
	JSONObject matchStream;
	JSONArray players;
	int summonerId;
	int summonerLevel;
	int champId;
	int[] items;
	int[] abilitySeq;
	int participantId;
	int inplayers;
	
	public int getSLevel() {
		return summonerLevel;
	}
	public int[] getItems(){
		return items;
	}
	
	public int[] getAbilitySeq() {
		return abilitySeq;
	}
	
	private void findLevel() throws JSONException {
		for (int i = 0; i < players.length(); i++){
			if (players.getJSONObject(i).getInt("championId") == champId){
				summonerLevel = players.getJSONObject(i).getJSONObject("stats").getInt("champLevel");
				inplayers = i;
				participantId = players.getJSONObject(i).getInt("participantId");
			}
		}
	}
	
	private void setItems() throws JSONException {
		String lookfor = "item";
		for (int i = 0; i < 7; i++){
			items[i] = players.getJSONObject(inplayers).getJSONObject("stats").getInt(lookfor + Integer.toString(i));			
		}
	}
	
	private void setAbilitySeq() throws JSONException {
		int levelFr = 0;
		JSONArray frames = matchStream.getJSONObject("timeline").getJSONArray("frames");
		for (int i = 1; i < frames.length(); i++){
			JSONArray events = frames.getJSONObject(i).getJSONArray("events");
			for (int j = 0; j < events.length(); j++){
				if (events.getJSONObject(j).getString("eventType") == "SKILL_LEVEL_UP"){
					if (events.getJSONObject(j).getString("levelUpType") == "NORMAL" && events.getJSONObject(j).getInt("participantId")==participantId){
						abilitySeq[levelFr] = events.getJSONObject(j).getInt("skillSlot");
						levelFr++;
					}
				}
			}
		}
	}
	
	public matchdata(JSONObject mS, int sId, int cId) throws JSONException{
		matchStream = mS;
		summonerId = sId;
		champId = cId;
		players = matchStream.getJSONArray("participants");
		findLevel();
		if (summonerLevel > 15){
			setItems();
			setAbilitySeq();
		}
	}
}
