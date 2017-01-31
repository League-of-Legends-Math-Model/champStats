package calculated;

import org.json.*;

import java.util.*;

public class runeTranslate {
	JSONObject runeData;
	ArrayList<Rune> statMods;
	
	public ArrayList<Rune> getStats(){
		return statMods;
	}
	
	private void setRuneInfo() throws JSONException {
		for (Iterator<?> jkey = runeData.keys(); jkey.hasNext(); ){
			String helper = (String)jkey.next();
			int friend = runeData.getJSONObject(helper).getInt("id");
			JSONObject stat = runeData.getJSONObject(helper).getJSONObject("stat");
			Iterator<String> skey = stat.keys();
			Rune blue = new Rune(1000, 0, 0);
			while (skey.hasNext()){
				String modifier = (String)skey.next();
				switch(modifier){
				case "FlatArmorMod":
					blue = new Rune(friend, 8, stat.getDouble(modifier));
					break;
				case "FlatHPPoolMod":
					blue = new Rune(friend, 0, stat.getDouble(modifier));
					break;
				case "FlatMPPoolMod":
					blue = new Rune(friend, 2, stat.getDouble(modifier));
					break;
				case "FlatMagicDamageMod":
					blue = new Rune(friend, 6, stat.getDouble(modifier));
					break;
				case "FlatPhysicalDamageMod":
					blue = new Rune(friend, 4, stat.getDouble(modifier));
					break;
				case "FlatSpellBlockMod":
					blue = new Rune(friend, 10, stat.getDouble(modifier));
					break;
				case "PercentAttackSpeedMod":
					blue = new Rune(friend, 14, stat.getDouble(modifier));
					break;
				case "PercentHPPoolMod":
					blue = new Rune(friend, 15, 1 + stat.getDouble(modifier));
					break;
				case "PercentMovementSpeedMod":
					blue = new Rune(friend, 16, stat.getDouble(modifier));
					break;
				case "rFlatArmorModPerLevel":
					blue = new Rune(friend, 9, stat.getDouble(modifier));
					break;
				case "rFlatHPModPerLevel":
					blue = new Rune(friend, 1, stat.getDouble(modifier));
					break;
				case "rFlatMPModPerLevel":
					blue = new Rune(friend, 3, stat.getDouble(modifier));
					break;
				case "rFlatMagicDamageModPerLevel":
					blue = new Rune(friend, 7, stat.getDouble(modifier));
					break;
				case "rFlatPhysicalDamageModPerLevel":
					blue = new Rune(friend, 5, stat.getDouble(modifier));
					break;
				case "rFlatSpellBlockModPerLevel":
					blue = new Rune(friend, 11, stat.getDouble(modifier));
					break;
				case "rPercentCooldownMod":
					blue = new Rune(friend, 12, stat.getDouble(modifier));
					break;
				case "rPercentCooldownModPerLevel":
					blue = new Rune(friend, 13, stat.getDouble(modifier));
					break;
				default:
				}
				statMods.add(blue);
			}
		}
		
	}
	
	/*
	 * double hp;
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
	 */
	
	public runeTranslate(JSONObject r) throws JSONException {
		runeData = r.getJSONObject("data");
		statMods = new ArrayList<Rune>();
		setRuneInfo();
	}
}
