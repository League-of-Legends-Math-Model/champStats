package calculated;

import org.json.*;

public class AbilityVar {

	int champ;
	int slot;
	String var;
	double coeff;
	double[] baseLevelArray;
	String stat;
	
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
			friend = new AbilityVar(champ, slot, var, coeff, stat);
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
	
	public double expectedResult(summoner su){
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
		case "magicdamage":
			variable = su.abilitypower;
			break;
		case "bonusattackdamage":
			variable = su.attackdamage - su.baseScaledArray[2];
			break;
		case "bonushealth":
			variable = su.hp - su.baseScaledArray[0];
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
		
		value = coeff * variable;
		
		return value;
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
