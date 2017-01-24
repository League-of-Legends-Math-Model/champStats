
package calculated;
import java.util.*;
public class summoner {
	int teamId;
	int summonerId;
	int champId;
	String summonerName;
	double[] statsArray;
	int[] itemArray;
	int[] abilitySequence;
	int[] frequentItems;
	
	/* statsArray
	 0: health
	 1: hpperlevel
	 2: mana
	 3: mpperlevel
	 4: attack damage
	 5: adperlevel
	 6: ability power
	 7: armor
	 8: armorperlevel
	 9: spell block (mr)
	 10: mrperlevel
	 11: movement speed
	 12: cooldown reduction
	 */
	
	
	
	public summoner(int tId, int sId, int cId, String sn){
		teamId = tId;
		summonerId = sId;
		champId = cId;
		summonerName = sn;
		statsArray = new double[12];
		itemArray = new int[7];
		abilitySequence = new int[18];
		for (int i = 0; i < 18; i++){
			if (i < 12){
				statsArray[i] = 0;
			}
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
		for (int i = 0; i < itemData.size() - 1; i++){
			for (int j = 1; j < itemData.size(); j++){
				if (itemData.get(i).getFreq()<itemData.get(j).getFreq()){
					frequencyObject holder = new frequencyObject(itemData.get(i).getId(),itemData.get(i).getFreq());
					itemData.set(i, itemData.get(j));
					itemData.set(j,  holder);
				}
			}
		}
	}
}

