package calculated;

import org.json.*;

public class AbilityVar {

	int champ;
	int slot;
	String var;
	double coeff;
	double[] baseLevelArray;
	String stat;
	double base;
	double perlevel;
	
	public AbilityVar (int c, int s, String v, double co, String st){
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		stat = st;
	}
	
	public boolean compare(int s, String v){
		boolean helper = false;
		if (s == slot && var == v){
			helper = true;
		}
		return helper;
	}
	
	public AbilityVar makeACopy(){
		AbilityVar friend;
		if (stat != ""){
			if (perlevel == 0){
				friend = new AbilityVar(champ, slot, var, coeff, stat);
			}
			else {
				friend = new AbilityVar(champ, slot, var, coeff, stat, base, perlevel);
			}
		}
		else {
			friend = new AbilityVar(champ, slot, var, coeff, baseLevelArray);
		}
		return friend;
	}
	
	public boolean isChamp(int c){
		boolean found = false;
		if (champ == c){
			found = true;
		}
		return found;
	}
	
	public double expectedResult(summoner su) throws JSONException {
		double value = 0;
		double variable = 0;
		switch(stat){
		case "attackdamage":
			variable = su.attackdamage;
			break;
		case "health":
			variable = su.hp;
			break;
		case "mana":
			variable = su.mp;
			break;
		case "armor":
			variable = su.armor;
			break;
		case "spelldamage":
			variable = su.abilitypower;
			break;
		case "bonusattackdamage":
			variable = su.attackdamage - su.baseScaledArray[2];
			break;
		case "bonushealth":
			variable = su.hp - su.baseScaledArray[0];
			break;
		case "effect1":
			int erank = su.expectRank(su.level, slot);
			if (erank > 0){
				variable = su.effects[slot].getJSONArray(1).getDouble(erank - 1);
			}
			break;
		case "e1sd":
			int arank = su.expectRank(su.level, slot);
			if (arank > 0){
				variable = su.effects[slot].getJSONArray(1).getDouble(arank - 1);
			}
			variable += su.abilitypower * coeff;
			variable = variable * 2;
			break;
		case "spellblock":
			variable = su.spellblock;
			break;
		case "movespeed":
			variable = su.movespeed;
			break;
		default:
			break;
		}
		if (variable == 0){
			variable = baseLevelArray[su.level - 1];
		}
		
		if (perlevel > 0){
			variable = variable * (base + perlevel * su.level);
		}
		
		value = coeff * variable;
		
		return value;
	}
	
	public AbilityVar (int c, int s, String v, double co, String st, double b, double pl){
		
	}
	public AbilityVar (int c, int s, String v, double co, double[] ba){
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		baseLevelArray = ba;
		stat = "";
	}
}
