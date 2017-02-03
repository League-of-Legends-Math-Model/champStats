package calculated;

import java.util.*;

public class VariableInfo {
	
	String fone;
	String ftwo;
	String aone;
	String atwo;
	String fthree;
	String ffour;
	String ffive;
	String fsix;
	String shyvwone;
	String shyvwtwo;
	String shyvwthree;
	ArrayList<AbilityVar> abilities;
	
	public VariableInfo () {
		fone = "{{ f1 }}";
		ftwo = "{{ f2 }}";
		aone = "{{ a1 }}";
		atwo = "{{ a2 }}";
		fthree = "{{ f3 }}";
		ffour = "{{ f4 }}";
		ffive = "{{ f5 }}";
		fsix = "{{ f6 }}";
		shyvwone = "@Effect1Amount*0.25@";
		shyvwtwo = "@CharBonusPhysical*0.25@";
		shyvwthree = "@CharAbilityPower2*.25@";
		abilities = new ArrayList<AbilityVar>();
		buildDatabase();
	}

	public ArrayList<AbilityVar> getAbilityVars(int c){
		ArrayList<AbilityVar> helper = new ArrayList<AbilityVar>();
		for (int i = 0; i < abilities.size(); i++){
			if (abilities.get(i).isChamp(c)){
				helper.add(abilities.get(i).makeACopy());
			}
		}
		return helper;
	}
	
	private void buildDatabase() {
		// Sion
		abilities.add(new AbilityVar(14, 0, fone, .6, "attackdamage"));
		abilities.add(new AbilityVar(14, 0, ftwo, 1.8, "attackdamage"));
		abilities.add(new AbilityVar(14, 1, fone, 0, "health"));
		abilities.add(new AbilityVar(14, 1, ftwo, .1, "health"));
		abilities.add(new AbilityVar(14, 1, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(14, 2, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(14, 3, fone, .4, "bonusattackdamage"));
		abilities.add(new AbilityVar(14, 3, ftwo, .8, "bonusattackdamage"));
		// Aurelion Sol
		double[] aStars = {20, 24, 28, 32, 36, 39, 44, 49, 54, 60, 66, 72, 78, 84, 93, 102, 111, 130};
		abilities.add(new AbilityVar(136, 0, aone, .65, "spelldamage"));
		abilities.add(new AbilityVar(136, 1, fone, 1.5, aStars));
		abilities.add(new AbilityVar(136, 1, ftwo, 1.5, "spelldamage", .17, .01));
		abilities.add(new AbilityVar(136, 3, aone, .7, "spelldamage"));
		// Lulu
		abilities.add(new AbilityVar(117, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(117, 0, ffour, .7, "effect1"));
		abilities.add(new AbilityVar(117, 0, ffive, .35, "spelldamage"));
		abilities.add(new AbilityVar(117, 0, fsix, 1, .5, "e1sd"));
		abilities.add(new AbilityVar(117, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(117, 2, atwo, .4, "spelldamage"));
		abilities.add(new AbilityVar(117, 3, aone, .5, "spelldamage"));
		// Lux
		abilities.add(new AbilityVar(99, 0, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(99, 1, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(99, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(99, 3, aone, .75, "spelldamage"));
		// Shyvana
		double[] secondhit = {.4, .55, .7, .85, 1};
		abilities.add(new AbilityVar(102, 0, ftwo, 1, "attackdamage"));
		abilities.add(new AbilityVar(102, 0, fone, secondhit, "attackdamage"));
		abilities.add(new AbilityVar(102, 1, aone, .2, "bonusattackdamage"));
		abilities.add(new AbilityVar(102, 1, atwo, .1, "spelldamage"));
		abilities.add(new AbilityVar(102, 1, shyvwone, .25, "effect1"));
		abilities.add(new AbilityVar(102, 1, shyvwtwo, .05, "bonusattackdamage"));
		abilities.add(new AbilityVar(102, 1, shyvwthree, .025, "spelldamage"));
		abilities.add(new AbilityVar(102, 2, aone, .3, "spelldamage"));
		abilities.add(new AbilityVar(102, 2, fone, 1, "flat", 94.12, 5.88));
		abilities.add(new AbilityVar(102, 2, fthree, .6, "flat", 94.12, 5.88));
		abilities.add(new AbilityVar(102, 2, ftwo, .2, "spelldamage"));
		abilities.add(new AbilityVar(102, 3, aone, .7, "spelldamage"));
		// Twisted Fate
		abilities.add(new AbilityVar(4, 0, aone, .65, "spelldamage"));
		abilities.add(new AbilityVar(4, 1, atwo, 1, "attackdamage"));
		abilities.add(new AbilityVar(4, 1, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(4, 2, aone, .5, "spelldamage"));
		// Trundle
		double[] tBite = {.8, .9, 1, 1.1, 1.2};
		abilities.add(new AbilityVar(48, 0, fone, tBite, "attackdamage"));
		abilities.add(new AbilityVar(48, 3, aone, .02, "spelldamage"));
		// Riven
		double[] rivQ = {.4, .45, .5, .55, .6};
		abilities.add(new AbilityVar(92, 0, fone, rivQ, "attackdamage"));
		abilities.add(new AbilityVar(92, 1, fone, 1, "bonusattackdamage"));
		abilities.add(new AbilityVar(92, 2, fone, 1, "bonusattackdamage"));
		abilities.add(new AbilityVar(92, 3, fthree, .2, "bonusattackdamage"));
		abilities.add(new AbilityVar(92, 3, fone, .6, "bonusattackdamage"));
		abilities.add(new AbilityVar(92, 3, ftwo, 1.8, "bonusattackdamage"));
		// Sejuani
		abilities.add(new AbilityVar(113, 0, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(113, 1, atwo, .03, "spelldamage"));
		abilities.add(new AbilityVar(113, 1, fone, .1, "bonushealth"));
		abilities.add(new AbilityVar(113, 1, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(113, 2, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(113, 3, aone, .8, "spelldamage"));
		// Gragas
		abilities.add(new AbilityVar(79, 0, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(79, 1, aone, .3, "spelldamage"));
		abilities.add(new AbilityVar(79, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(79, 2, fone, 3, "flat"));
		abilities.add(new AbilityVar(79, 3, aone, .7, "spelldamage"));
		// Poppy
		abilities.add(new AbilityVar(78, 0, aone, .8, "bonusattackdamage"));
		abilities.add(new AbilityVar(78, 1, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(78, 1, fone, .15, "armor"));
		abilities.add(new AbilityVar(78, 1, ftwo, .15, "spellblock"));
		abilities.add(new AbilityVar(78, 2, aone, .5, "bonusattackdamage"));
		abilities.add(new AbilityVar(78, 3, aone, .9, "bonusattackdamage"));
		// Nautilus
		abilities.add(new AbilityVar(111, 0, aone, .75, "spelldamage"));
		abilities.add(new AbilityVar(111, 0, fone, .5, "cooldown"));
		abilities.add(new AbilityVar(111, 1, fone, .1, "bonushealth"));
		abilities.add(new AbilityVar(111, 1, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(111, 2, aone, .3, "spelldamage"));
		abilities.add(new AbilityVar(111, 3, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(111, 3, atwo, .8, "spelldamage"));
		// Renekton
		abilities.add(new AbilityVar(58, 0, aone, .8, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 0, fone, .04, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 0, ftwo, 3, "effect2"));
		abilities.add(new AbilityVar(58, 0, fthree, .12, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 0, ffour, .12, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 0, ffive, 9, "effect2"));
		abilities.add(new AbilityVar(58, 0, fsix, .36, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 1, fone, .75, "attackdamage"));
		abilities.add(new AbilityVar(58, 1, ftwo, 1.5, "attackdamage"));
		abilities.add(new AbilityVar(58, 1, fthree, 2.25, "attackdamage"));
		abilities.add(new AbilityVar(58, 2, fone, .9, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 2, ftwo, 1.35, "bonusattackdamage"));
		abilities.add(new AbilityVar(58, 3, aone, .1, "spelldamage"));
		// Nunu
		double[] stacks = {50, 55, 60, 65, 70};
		abilities.add(new AbilityVar(20, 0, ffive, stacks, "flat"));
		abilities.add(new AbilityVar(20, 0, aone, .75, "spelldamage"));
		abilities.add(new AbilityVar(20, 2, aone, .9, "spelldamage"));
		abilities.add(new AbilityVar(20, 3, aone, 2.5, "spelldamage"));
		abilities.add(new AbilityVar(20, 3, ftwo, .125, .3125, "e1sd"));
		// Bard
		abilities.add(new AbilityVar(432, 0, aone, .65, "spelldamage"));
		abilities.add(new AbilityVar(432, 1, aone, .3, "spelldamage"));
		abilities.add(new AbilityVar(432, 1, atwo, .6, "spelldamage"));
		abilities.add(new AbilityVar(432, 1, fone, 1, "flat"));
		abilities.add(new AbilityVar(432, 1, ftwo, 1, "flat"));
		// Skarner
		double[] shield = {.1, .11, .12, .13, .14};
		abilities.add(new AbilityVar(72, 0, fone, .8, "bonusattackdamage"));
		abilities.add(new AbilityVar(72, 0, aone, .3, "spelldamage"));
		abilities.add(new AbilityVar(72, 1, aone, .8, "spelldamage"));
		abilities.add(new AbilityVar(72, 1, fone, shield, "health"));
		abilities.add(new AbilityVar(72, 2, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(72, 3, atwo, .6, "attackdamage"));
		abilities.add(new AbilityVar(72, 3, aone, .5, "spelldamage"));
		// Malphite (54)
		abilities.add(new AbilityVar(54, 0, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(54, 1, aone, .1, "spelldamage"));
		
	}
}
