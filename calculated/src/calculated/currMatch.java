package calculated;

import org.json.*;

public class currMatch {
	JSONObject currentMatch;
	JSONArray players;
	int summonerId;
	int[][] playerInfo;
	String[] playerNames;
	JSONArray[] pMasteries;
	JSONArray[] pRunes;
	
	public int[][] getPlayerInfo() {
		return playerInfo;
	}
	
	public String[] getPlayerNames() {
		return playerNames;
	}
	
	private void populatePlayerInfo() throws JSONException {
		int ourTeam = 0;
		playerNames = new String[5];
		int[][] everybody = new int[10][3];
		for (int i = 0; i < players.length(); i++){
			everybody[i][0] = players.getJSONObject(i).getInt("teamId");
			everybody[i][1] = players.getJSONObject(i).getInt("summonerId");
			everybody[i][2] = players.getJSONObject(i).getInt("championId");
			if (players.getJSONObject(i).getInt("summonerId") == summonerId){
				ourTeam = everybody[i][0];
			}
		}
		int enPlayer = 0;
		for (int i = 0; i < players.length(); i++){
			if (!(ourTeam == everybody[i][0])){
				for (int j = 0; j < 3; j++){
					playerInfo[enPlayer][j] = everybody[i][j];
				}
				pMasteries[enPlayer] = players.getJSONObject(i).getJSONArray("masteries");
				pRunes[enPlayer] = players.getJSONObject(i).getJSONArray("runes");
				playerNames[enPlayer] = players.getJSONObject(i).getString("summonerName");
				enPlayer++;
			}
		}
	}
	
	public currMatch(JSONObject cM, int sId) throws JSONException {
		currentMatch = cM;
		summonerId = sId;
		playerInfo = new int[5][3];
		pMasteries = new JSONArray[5];
		pRunes = new JSONArray[5];
		players = currentMatch.getJSONArray("participants");
		populatePlayerInfo();
	}
}
