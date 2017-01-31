package calculated;

import org.json.*;
import java.util.*;

public class Item {
	
	JSONObject item;
	int itemId;
	double[] flatMod;
	double[] perMod;
	double[] viktorPerLevel;
	String name;
	boolean viktorItem;
	
	public int getId(){
		return itemId;
	}
	
	public double[] getFlat(){
		return flatMod;
	}
	
	public boolean viktor(){
		return viktorItem;
	}
	
	public double[] getPer(){
		return perMod;
	}
	
	public String getStr(){
		return name;
	}
	
	private void interpretItem() throws JSONException {
		itemId = item.getInt("id");
		JSONObject stats = item.getJSONObject("stats");
		if (itemId != 3632 && itemId != 3648){
			name = item.getString("name");
		}
		Iterator<String> keys = stats.keys();
		while (keys.hasNext()){
			String statType = (String)keys.next();
			switch(statType){
			case "FlatArmorMod":
				flatMod[4] += stats.getDouble(statType);
				break;
			case "FlatHPPoolMod":
				flatMod[0] += stats.getDouble(statType);
				break;
			case "FlatMPPoolMod":
				flatMod[1] += stats.getDouble(statType);
				break;
			case "FlatMagicDamageMod":
				flatMod[3] += stats.getDouble(statType);
				break;
			case "FlatMovementSpeedMod":
				flatMod[7] += stats.getDouble(statType);
				break;
			case "FlatPhysicalDamageMod":
				flatMod[2] += stats.getDouble(statType);
				break;
			case "FlatSpellBlockMod":
				flatMod[5] += stats.getDouble(statType);
				break;
			case "PercentAttackSpeedMod":
				flatMod[6] += stats.getDouble(statType);
				break;
			case "PercentMovementSpeedMod":
				perMod[4] = 1 + stats.getDouble(statType);
				break;
			default:
			}
		}
		specialStats();
	}
	
	private void specialStats() throws JSONException {
		viktorItems();
		cdrItems();
		permStatItems();
		moveItems();
	}
	
	private void viktorItems() {
		switch(itemId){
		case 3198:
			viktorPerLevel[0] += 4;
			viktorPerLevel[1] += 5;
		case 3197:
			viktorPerLevel[0] += 3;
			viktorPerLevel[1] += 5;
		case 3196:
			viktorPerLevel[0] += 2;
			viktorPerLevel[1] += 5;
		case 3200:
			viktorPerLevel[0] += 1;
			viktorPerLevel[1] += 10;
			viktorItem = true;
		default:
		}
	}
	
	private void permStatItems() {
		// MP Items
		switch (itemId){
		case 3003:
		case 3007:
		case 3048:
		case 3040:
		case 3004:
		case 3008:
		case 3042:
		case 3043:
		case 3070:
		case 3073:
			flatMod[1] += 650;
		case 3029:
		case 3027:
			flatMod[1] += 100;
		default:
		}
		// HP Items
		switch (itemId){
		case 3029:
		case 3027:
			flatMod[0] += 50;
		case 3052:
			flatMod[0] += 150;
		default:
		}
		// AP Items
		switch (itemId){
		case 3041:
			flatMod[3] += 60;
		case 3029:
		case 3027:
			flatMod[3] += 10;
		case 1082:
			flatMod[3] += 15;
		case 3191:
			flatMod[3] += 15;
		default:
		}
		// Armor Items
		if (itemId == 3191){
			flatMod[4] += 15;
		}
		// Multiplier
		switch(itemId){
		case 3003:
		case 3007:
		case 3048:
		case 3040:
			perMod[3] = .03;
			break;
		case 3004:
		case 3008:
		case 3042:
		case 3043:
			perMod[2] = .02;
			break;
		case 1413:
		case 1409:
		case 1401:
		case 3672:
			perMod[0] = .15;
			break;
		case 3089:
			perMod[1] += .1;
		case 3090:
			perMod[1] += .25;
			break;
		case 3053:
			perMod[5] = .25;
			break;
		default:
		}
	}
	
	private void moveItems() {
		switch (itemId){
		case 3041:
			perMod[4] += .02;
		case 3508:
			perMod[4] += .01;
		case 3046:
			perMod[4] += .02;
		case 3086:
		case 3113:
			perMod[4] += .05;
		default:
		}
	}
	private void cdrItems(){
		switch(itemId){
		case 3110:
		case 3115:
		case 3187:
		case 3071:
		case 3078:
		case 3165:
			flatMod[8] += .1;
		case 1412:
		case 1408:
		case 1400:
		case 3671:
		case 3083:
		case 3092:
		case 2301:
		case 2302:
		case 3107:
		case 3108:
		case 3104:
		case 3100:
		case 3101:
		case 3812:
		case 3504:
		case 3508:
		case 3156:
		case 3152:
		case 3137:
		case 3001:
		case 3142:
		case 3222:
		case 3133:
		case 3114:
		case 3024:
		case 3050:
		case 3056:
		case 3301:
		case 3158:
		case 3157:
		case 3060:
		case 3065:
		case 3067:
			flatMod[8] += .1;
		default:
		}
	}
	
	public Item(JSONObject d) throws JSONException {
		item = d;
		flatMod = new double[9];
		perMod = new double[6];
		viktorPerLevel = new double[2];
		viktorItem = false;
		for (int i = 0; i < 9; i++){
			flatMod[i] = 0;
			if (i < 6){
				perMod[i] = 1;
				if (i < 2) {
					viktorPerLevel[i] = 0;
				}
			}
		}
		interpretItem();
	}
	
}
