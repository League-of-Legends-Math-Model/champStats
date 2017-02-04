
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
	masterySet masteries;
	runeSet runes;
	ArrayList<AbilityVar> ability;
	JSONArray masteryData;
	JSONArray runeData;
	JSONArray[] effects;
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
	double bonusattackspeed;
	double attackspeed;
	double[] baseStatArray;
	double[] baseScaledArray;
	double summonerspellcd;
	int level;
	double abilityAug;
	
	public void placeItem(int iid, int slot){
		itemArray[slot] = iid;
	}
	
	public void putCharacterData(JSONObject cD) throws JSONException {
		characterData = cD;
		spells = characterData.getJSONArray("spells");
		buildEffects();
	}
	
	public void putLoadout(JSONArray ma, JSONArray ru) throws JSONException {
		masteryData = ma;
		runeData = ru;
		masteries = new masterySet(masteryData);
		runes = new runeSet(runeData);
	}
	
	public void setLevel (int l) {
		level = l;
		rebuildStats();
	}
	
	private void rebuildStats(){
		growthLevel();
		masteryFlat();
		runeFlat();
		itemStats(ibank); // need ibank as a global variable
		// after item calculation
		runePer();
		masteryPer();
		charAbil();
		
		// final attack speed
		setAttackSpeed();
	}
	
	private void charAbil() throws JSONException {
		abilityAug = 0;
		int ranker = 0;
		switch(champId){
		case 54:
			ranker = expectRank(level, 1);
			if (ranker > 0){
				abilityAug = armor * .01 * eCoeff(1, ranker);
				armor += abilityAug;
			}
			break;
		default:
			break;
		}
	}
	
	private void itemStats(ItemBank ib){
		double[][] precise = ib.itemBuild(itemArray);
		hp += precise[0][0];
		mp += precise[0][1];
		mp += precise[1][7] * level;
		attackdamage += precise[0][2];
		abilitypower += precise[0][3];
		abilitypower += precise[1][6] * level;
		armor += precise[0][4];
		spellblock += precise[0][5];
		bonusattackspeed += precise[0][6];
		movespeed += precise[0][7];
		cooldownreduction += precise[0][8];
		if (cooldownreduction > .4){
			cooldownreduction = .4;
		}
		hp += (hp - baseScaledArray[0]) * precise[1][0];
		attackdamage += mp * (1 - precise[1][2]);
		abilitypower += mp * (1 - precise[1][3]);
		attackdamage += (1 - precise[1][5]) * baseScaledArray[2];
		abilitypower = abilitypower * precise[1][1];
		movespeed = movespeed * precise[1][4];
	}
	private void runePer() {
		double[] modifiers = runes.getPer();
		hp = hp * modifiers[15];
		bonusattackspeed += modifiers[14];
		movespeed = movespeed * modifiers[16];
	}
	
	private void runeFlat(){
		double[] modifiers = runes.getFlat();
		hp += modifiers[0];
		hp += modifiers[1] * level;
		mp += modifiers[2];
		mp += modifiers[3] * level;
		attackdamage += modifiers[4];
		attackdamage += modifiers[5] * level;
		abilitypower += modifiers[6];
		abilitypower += modifiers[7] * level;
		armor += modifiers[8];
		armor += modifiers[9] * level;
		spellblock += modifiers[10];
		spellblock += modifiers[11] * level;
		cooldownreduction += modifiers[12];
		cooldownreduction += modifiers[13] * level;
	}
	
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
	
	// done after the per levels are updated
	
	private void growthLevel(){
		double [][] statHelper = new double[6][2];
		int row = 0;
		int col = 0;
		for (int i = 0; i < 12; i++){
			statHelper[row][col] =  baseStatArray[i];
			col++;
			if (col == 2){
				row++;
				col = 0;
			}
		}
		for (int i = 0; i < 6; i++){
			statHelper[i][0] += statHelper[i][1] * (level - 1) * (0.685 + 0.0175 * level);
		}
		hp = statHelper[0][0];
		mp = statHelper[1][0];
		attackdamage = statHelper[2][0];
		armor = statHelper[3][0];
		spellblock = statHelper[4][0];
		bonusattackspeed = statHelper[5][0];
		baseScaledArray[0] = hp;
		baseScaledArray[1] = mp;
		baseScaledArray[2] = attackdamage;
		baseScaledArray[3] = armor;
		baseScaledArray[4] = spellblock;
		baseScaledArray[5] = bonusattackspeed;
		
	}
	
	private void masteryFlat() {
		double[] mHelper = masteries.getFlat();
		hp += mHelper[0];
		attackdamage += mHelper[1] + mHelper[2] * level;
		abilitypower += mHelper[3] + mHelper[4] * level;
	}
	
	private void masteryPer() {
		double[] mHelper = masteries.getPer();
		armor += (armor - baseScaledArray[3]) * (1 + mHelper[0]);
		spellblock += (spellblock - baseScaledArray[4]) * (1 + mHelper[1]);
		cooldownreduction += mHelper[2];
		summonerspellcd = mHelper[3];
		bonusattackspeed += mHelper[4];
	}
	
	private void setAttackSpeed(){
		double rawattackspeed = 0.625 / (1 - attackspeedoffset) + ((0.625 / (1 - attackspeedoffset)) * bonusattackspeed);
		attackspeed = 1 / rawattackspeed;
		if (attackspeed > 2.5) {
			attackspeed = 2.5;
		}
	}
	
	public int expectRank(int inpLevel, int spellSlot){
		int count = 0;
		for (int i = 0; i < inpLevel; i++){
			if (abilitySequence[i] == spellSlot) {
				count++;
			}
		}
		return count;
	}
	
	public double spCoeff(int sslot, String var) throws JSONException {
		double res = 0;
		int spellVar = 0;
		while (!ability.get(spellVar).compare(sslot,  var)){
			spellVar++;
		}
		res = ability.get(spellVar).expectedResult(this);
		return res;
	}
	
	public double cooldownCalc (JSONObject sp, int rk) throws JSONException {
		double cd = sp.getJSONArray("cooldown").getDouble(rk - 1);
		cd = cd - (cd * cooldownreduction);
		return cd;
	}
	
	private void buildEffects() throws JSONException {
		effects = new JSONArray[4];
		for (int i = 0; i < 4; i++){
			effects[i] = spells.getJSONObject(i).getJSONArray("effects");
		}
	}
	
	public double eCoeff(int sslot, int efnum) throws JSONException {
		double res = 0;
		int ranketh = expectRank(level, sslot);
		if (ranketh > 0){
			res = effects[sslot].getJSONArray(efnum).getDouble(ranketh - 1);
		}
		return res;
	}
	
	public summoner(int tId, int sId, int cId, String sn){
		teamId = tId;
		summonerId = sId;
		champId = cId;
		summonerName = sn;
		summonerspellcd = 1;
		itemArray = new int[7];
		abilitySequence = new int[18];
		baseScaledArray = new double[6];
		// ability = (VariableInfo).getAbilityVars(champId);
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

