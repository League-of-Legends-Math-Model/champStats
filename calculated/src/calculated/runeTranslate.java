package calculated;

import org.json.*;

import java.util.*;

public class runeTranslate {
	JSONObject runeData;
	ArrayList<rune> statMods;
	
	private void setRuneInfo() throws JSONException {
		for (Iterator<?> jkey = runeData.keys(); jkey.hasNext(); ){
			String helper = (String)jkey.next();
			int friend = runeData.getJSONObject(helper).getInt("id");
			JSONObject stat = runeData.getJSONObject(helper).getJSONObject("stat");
			Iterator<String> skey = stat.keys();
			Rune blue;
			while (skey.hasNext()){
				String modifier = (String)skey.next();
				switch(modifier){
				case "FlatArmorMod":
					blue = new Rune(friend, 0, stat.getDouble(modifier));
					break;
				default:
				}
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
		statMods = new ArrayList<rune>();
		setRuneInfo();
	}
}
