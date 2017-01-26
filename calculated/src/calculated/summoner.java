
package calculated;
import java.util.*;
import org.json.*;

public class summoner {
	int teamId;
	int summonerId;
	int champId;
	String summonerName;
	int[] itemArray;
	int[] abilitySequence;
	int[] frequentItems;
	JSONObject characterData;
	JSONArray spells;
	JSONArray masteries;
	JSONArray runes;
	double hp;
	double hpperlevel;
	double mp;
	double mpperlevel;
	double armor;
	double armorperlevel;
	double attackdamage;
	double attackdamageperlevel;
	double abilitypower;
	double abilitypowerperlevel;
	double spellblock;
	double spellblockperlevel;
	double movespeed;
	double attackspeedoffset;
	double attackspeedperlevel;
	double cooldownreduction;
	double[] baseStatArray;
	
	
	public void putCharacterData(JSONObject cD) throws JSONException {
		characterData = cD;
		spells = characterData.getJSONArray("spells");
	}
	
	public void putLoadout(JSONArray ma, JSONArray ru) {
		masteries = ma;
		runes = ru;
	}
	
	/* To build stats, passes:
	 * public void putBaseStats
	 */
	
	public void putBaseStats(JSONObject cS) throws JSONException {
		JSONObject stats = cS.getJSONObject("stats");
		armor = stats.getDouble("armor");
		armorperlevel = stats.getDouble("armorperlevel");
		attackdamage = stats.getDouble("attackdamage");
		attackdamageperlevel = stats.getDouble("attackdamageperlevel");
		attackspeedoffset = stats.getDouble("attackspeedoffset");
		attackspeedperlevel = stats.getDouble("attackspeedperlevel");
		hp = stats.getDouble("hp");
		hpperlevel = stats.getDouble("hpperlevel");
		movespeed = stats.getDouble("movespeed");
		mp = stats.getDouble("mp");
		mpperlevel = stats.getDouble("mpperlevel");
		spellblock = stats.getDouble("spellblock");
		spellblockperlevel = stats.getDouble("spellblockperlevel");
		baseStatArray = new double[13];
		baseStatArray[0] = hp;
		baseStatArray[1] = hpperlevel;
		baseStatArray[2] = mp;
		baseStatArray[3] = mpperlevel;
		baseStatArray[4] = attackdamage;
		baseStatArray[5] = attackdamageperlevel;
		baseStatArray[6] = armor;
		baseStatArray[7] = armorperlevel;
		baseStatArray[8] = spellblock;
		baseStatArray[9] = spellblockperlevel;
		baseStatArray[10] = attackspeedoffset;
		baseStatArray[11] = attackspeedperlevel;
		baseStatArray[12] = movespeed;
	}
	
	
	private int expectRank(int inpLevel, int spellSlot){
		int count = 0;
		for (int i = 0; i < inpLevel; i++){
			if (abilitySequence[i] == spellSlot) {
				count++;
			}
		}
		return count;
	}
	
	// ALL DAMAGE SPELLS RETURN AN ARRAY: [PHYS, MAG, TRUE, CD]
	// Spell Type: Phys, AD coefficient, no extra (Caitlyn Q)
	
	private double[] physAbilityCQ(int spellNum, int inputLevel) throws JSONException {
		double[] expectedDamage = {0, 0, 0, 0};
		
		JSONObject spell = spells.getJSONObject(spellNum);
		
		int rank = expectRank(inputLevel, spellNum);
		
		if (rank == 0){
			rank = 1;
		}
		
		double cooldown = spell.getJSONArray("cooldown").getDouble(rank);
		cooldown = cooldown - (cooldown * cooldownreduction);
		
		JSONArray effect = spell.getJSONArray("effect");
		
		double baseDamage = effect.getJSONArray(1).getDouble(rank);
		double extraDamage = attackdamage * effect.getJSONArray(5).getDouble(rank);
		double phys = baseDamage + extraDamage;
		
		expectedDamage[0] = phys;
		expectedDamage[3] = cooldown;
		
		return expectedDamage;
	}
	
	private double[] snareAugCW(int spellNum, int inputLevel) throws JSONException {
		double[] expectedSnare = {0, 0};
		
		double cooldown = spell.getJSONArray("cooldown").getDouble(rank);
		cooldown = cooldown - (cooldown * cooldownreduction);
		
		
		
		return expectedSnare;
	}
	
	public summoner(int tId, int sId, int cId, String sn){
		teamId = tId;
		summonerId = sId;
		champId = cId;
		summonerName = sn;
		itemArray = new int[7];
		abilitySequence = new int[18];
		for (int i = 0; i < 18; i++){
			if (i < 7){
				itemArray[i] = 0;
			}
			abilitySequence[i] = 0;
		}
	}
	
	public int getTeamId()
	{
		return teamId;
	}
	
	private boolean abRules(int[] skills, int slot, int skill){
		boolean ready = true;
		int[] soFar = new int [4];
		for (int i = 0; i < 4; i++){
			soFar[i] = 0;
		}
		int skillCap = 5;
		int ultSkillCap = 3;
		
		if (champId == 126){
			skillCap = 6;
		}
		if (champId == 77){
			ultSkillCap = 5;
		}
		for (int i = 0; i < slot; i++){
			soFar[skills[i]]++;
		}
		if (slot == 1 && skill == skills[0]){
			ready = false;
		}
		if (slot == 3 && soFar[skill] == 2){
			ready = false;
		}
		if (slot == 7 && soFar[skill] == 4){
			ready = false;
		}
		if (slot > 8){
			if (soFar[skill] == skillCap){
				ready = false;
			}
			if (skill == 3 && soFar[skill] == ultSkillCap){
				ready = false;
			}
		}
		return ready;
	}
	
	public void setAbilitySequence(int[][] skillOrder){
		int expected;
		int nExpected;
		int times;
		int nTimes;
		int[][] skillSet = new int[4][18];
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				skillSet[i][j] = 0;
			}
		}
		for (int i = 0; i < skillOrder.length; i++){
			for (int j = 0; j < 18; j++) {
				skillSet[skillOrder[i][j]][j]++;
			}
		}
		for (int i = 0; i < 18; i++){
			expected = 0;
			nExpected = 0;
			times = 0;
			nTimes = 0;
			for (int j = 0; j < 4; j++){
				if (skillSet[j][i] > times){
					nTimes = times;
					nExpected = expected;
					expected = j;
					times = skillSet[j][i];
				}
			}
			boolean works;
			works = abRules(abilitySequence, i, expected);
			if (works){
				abilitySequence[i] = expected;
			}
			else {
				abilitySequence[i] = nExpected;
			}
		}
	}
	
	public void setFrequentItems(int[][] itemHistory){
		int[] excluded = {2031, 2032, 2033, 2003, 2009, 3361, 3362, 3363, 3364, 3341, 3340};
		ArrayList<frequencyObject> itemData = new ArrayList<frequencyObject>();
		for (int i = 0; i < itemHistory.length; i++){
			for (int j = 0; j < 7; j++){
				boolean placed = false;
				for (int k = 0; k < itemData.size(); k++){
					if (itemData.get(k).getId() == itemHistory[i][j] && itemHistory[i][j] != 0){
						int oldFreq = itemData.get(k).getFreq();
						oldFreq++;
						itemData.get(k).setFreq(oldFreq);
						placed = true;
					}
				}
				if (!placed){
					frequencyObject unseen = new frequencyObject(itemHistory[i][j], 0);
					itemData.add(unseen);
				}
			}
		}
		for (int i = 0; i < excluded.length; i++) {
			for (int j = 0; j < itemData.size(); j++){
				if (itemData.get(j).getId() == excluded[i]){
					itemData.get(j).setFreq(0);
				}
			}
		}
		for (int i = 0; i < itemData.size() - 1; i++){
			for (int j = 1; j < itemData.size(); j++){
				if (itemData.get(i).getFreq()<itemData.get(j).getFreq()){
					frequencyObject holder = new frequencyObject(itemData.get(i).getId(),itemData.get(i).getFreq());
					itemData.set(i, itemData.get(j));
					itemData.set(j,  holder);
				}
			}
		}
		int itemSet = 7;
		if (itemData.size() < itemSet) {
			itemSet = itemData.size();
		}
		for (int i = 0; i < itemSet; i++){
			frequentItems[i] = itemData.get(i).getId();
		}
	}
}

