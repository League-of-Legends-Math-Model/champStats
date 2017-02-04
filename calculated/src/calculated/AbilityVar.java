package calculated;

import org.json.*;

import java.math.*;

public class AbilityVar {

	int champ;
	int slot;
	String var;
	double coeff;
	double[] baseLevelArray;
	String stat;
	double base;
	double perlevel;
	double[] rankCoeff;
	double inCoeff;
	
	public AbilityVar (int c, int s, String v, double co, String st){
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		stat = st;
		rankCoeff = new double[4];
		inCoeff = 1;
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
			variable = su.eCoeff(slot, 1);
			break;
		case "effect2":
			variable = su.eCoeff(slot, 2);
			break;
		case "effect3":
			variable = su.eCoeff(slot, 3);
			break;
		case "abilityaug":
			variable = su.abilityAug;
			break;
		case "e1sd":
			variable = su.eCoeff(slot, 1) * coeff;
			variable += su.abilitypower * inCoeff;
			variable = variable / coeff;
			break;
		case "e2bad":
			variable = su.eCoeff(slot, 2) * coeff;
			variable += su.attackdamage - su.baseScaledArray[2];
			variable = variable / coeff;
			break;
		case "level":
			variable = su.level;
			break;
		case "e1ad":
			variable = su.eCoeff(slot, 1) * coeff;
			variable += su.attackdamage * inCoeff;
			variable = variable / coeff;
			break;
		case "e7ad":
			variable = su.eCoeff(slot, 7) * coeff;
			variable += su.attackdamage * inCoeff;
			variable = variable / coeff;
			break;
		case "e1hp":
			variable = su.eCoeff(slot, 1) * coeff;
			variable += su.hp * inCoeff;
			variable = variable / coeff;
			break;
		case "e1e4ad":
			variable = su.eCoeff(slot, 1);
			double help = su.eCoeff(slot, 4);
			if (help == 0){
				help = 3;
			}
			variable = (variable + (su.attackdamage - su.baseScaledArray[2]) * coeff) / help;
			variable = variable / coeff;
			break;
		case: "e3ad":
			variable = su.eCoeff(slot, 3) * coeff;
			variable += su.attackdamage * inCoeff;
			variable = variable / coeff;
			break;
		case "e6hp":
			variable = su.eCoeff(slot, 6) * coeff;
			variable += su.hp * inCoeff;
			variable = variable / coeff;
			break;
		case "spellblock":
			variable = su.spellblock;
			break;
		case "movespeed":
			variable = su.movespeed;
			break;
		case "spfloor":
			variable = Math.floor(su.abilitypower / 100);
			if (inCoeff > 1){
				variable = (variable * 7.5) + inCoeff;
			}
			break;
		case "baseE1ap":
			variable = su.eCoeff(slot, 1);
			variable += su.abilitypower * coeff;
			variable = variable / coeff;
			break;
		case "adap":
			variable = su.attackdamage - su.baseScaledArray[2] + su.abilitypower;
			break;
		case "flat":
			variable = 1;
			break;
		case "spd":
			int speeder = su.expectRank(su.level, slot) - 1;
			if (speeder == 0){
				speeder = 1;
			}
			variable = baseLevelArray[su.level] + rankCoeff[speeder];
			break;
		case "baseplad":
			variable = base + perlevel * su.level + inCoeff * su.attackdamage;
			break;
		case "cooldown":
			int cRank = su.expectRank(su.level, slot) - 1;
			if (cRank == 0){
				cRank = 1;
			}
			variable = su.cooldownCalc(su.spells.getJSONObject(slot), cRank);
			break;
		default:
			break;
		}
		if (variable == 0){
			variable = baseLevelArray[su.level - 1];
		}
		
		if (perlevel > 0 && inCoeff == 1){
			variable = variable * (base + perlevel * su.level);
		}
		if (rankCoeff.length == 5 && stat != "spd"){
			int ranker = su.expectRank(su.level, slot) - 1;
			if (ranker == 0){
				ranker = 1;
			}
			variable = variable * rankCoeff[ranker - 1];
		}
		
		value = coeff * variable;
		
		return value;
	}
	
	public AbilityVar(int c, int s, String v, double[] lvl, double[] co, String st){
		champ = c;
		slot = s;
		var = v;
		rankCoeff = co;
		baseLevelArray = lvl;
		inCoeff = 1;
		stat = st;
		coeff = 1;
	}
	public AbilityVar(int c, int s, String v, double co, double cs, String st){
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		inCoeff = cs;
		stat = st;
		rankCoeff = new double[4];
	}
	
	public AbilityVar(int c, int s, String v, double[] co, String st){
		champ = c;
		slot = s;
		var = v;
		rankCoeff = co;
		stat = st;
		coeff = 1;
		inCoeff = 1;
	}
	
	public AbilityVar (int c, int s, String v, double co, String st, double b, double pl){
		// for one ability whose damage is calculated by a level basis, no other stats
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		stat = st;
		base = b;
		perlevel = pl;
		rankCoeff = new double[4];
		inCoeff = 1;
	}
	public AbilityVar(int c, int s, String v, double co, double b, double pl, String st){
		// for an ability that has a per level component, but also has another stat
		champ = c;
		slot = s;
		var = v;
		coeff = 1;
		stat = st;
		base = b;
		perlevel = pl;
		rankCoeff = new double[4];
		inCoeff = co;
	}
	public AbilityVar (int c, int s, String v, double co, double[] ba){
		champ = c;
		slot = s;
		var = v;
		coeff = co;
		baseLevelArray = ba;
		stat = "";
		rankCoeff = new double[4];
		inCoeff = 1;
	}
}
