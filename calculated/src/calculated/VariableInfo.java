package calculated;

import java.util.*;
import java.math.*;

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
	String kogult;
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
		kogult = "@Effect1Amount*1.5@"
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
		// Malphite
		abilities.add(new AbilityVar(54, 0, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(54, 1, aone, .1, "spelldamage"));
		abilities.add(new AbilityVar(54, 1, fone, 1, "abilityaug"));
		abilities.add(new AbilityVar(54, 1, ftwo, .15, "armor"));
		abilities.add(new AbilityVar(54, 2, fone, .3, "armor"));
		abilities.add(new AbilityVar(54, 2, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(54, 3, aone, 1, "spelldamage"));
		// Nami
		abilities.add(new AbilityVar(267, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(267, 1, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(267, 1, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(267, 1, fone, 1, 85, "spfloor"));
		abilities.add(new AbilityVar(267, 2, atwo, .05, "spelldamage"));
		abilities.add(new AbilityVar(267, 2, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(267, 3, aone, .6, "spelldamage"));
		// Jinx
		double [] jatkspd = {0, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70};
		double [] jbatkspd = {30, 40, 50, 60, 70};
		abilities.add(new AbilityVar(222, 0, ffour, jatkspd, jbatkspd, "spd"));
		abilities.add(new AbilityVar(222, 1, aone, 1.4, "attackdamage"));
		abilities.add(new AbilityVar(222, 2, aone, 1, "spelldamage"));
		abilities.add(new AbilityVar(222, 3, aone, .15, "bonusattackdamage"));
		abilities.add(new AbilityVar(222, 3, atwo, 1.5, "bonusattackdamage"));
		// Rengar
		abilities.add(new AbilityVar(107, 0, fone, 2.5, 104, 16, "baseplad"));
		abilities.add(new AbilityVar(107, 0, ftwo, 1, "e7ad"));
		abilities.add(new AbilityVar(107, 1, aone, .8, "spelldamage"));
		abilities.add(new AbilityVar(107, 1, fone, 1, "flat", 40, 10));
		abilities.add(new AbilityVar(107, 2, aone, .7, "attackdamage"));
		abilities.add(new AbilityVar(107, 2, fone, 1, "flat", 35, 15));
		// Xin Zhao
		abilities.add(new AbilityVar(5, 0, atwo, 1.2, "attackdamage"));
		abilities.add(new AbilityVar(5, 1, aone, .2, "adap"));
		abilities.add(new AbilityVar(5, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(5, 3, aone, 1, "bonusattackdamage"));
		// Singed
		abilities.add(new AbilityVar(27, 0, aone, .075, "spelldamage"));
		abilities.add(new AbilityVar(27, 2, aone, .75, "spelldamage"));
		// Kassadin
		abilities.add(new AbilityVar(38, 0, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(38, 0, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(38, 1, aone, .1, "spelldamage"));
		abilities.add(new AbilityVar(38, 1, atwo, .7, "spelldamage"));
		abilities.add(new AbilityVar(38, 2, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(38, 3, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(38, 3, ftwo, .02, "mana"));
		abilities.add(new AbilityVar(38, 3, fone, .1, "spelldamage"));
		abilities.add(new AbilityVar(38, 3, fthree, .01, "mana"));
		// Draven
		double [] axes = {.45, .55, .65, .75, .85};
		abilities.add(new AbilityVar(119, 0, fone, axes, "attackdamage"));
		abilities.add(new AbilityVar(119, 2, fone, .5, "bonusattackdamage"));
		abilities.add(new AbilityVar(119, 3, fone, 1.1, "bonusattackdamage"));
		// Dr. Mundo
		abilities.add(new AbilityVar(36, 1, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(36, 2, fone, .01, "e6hp"));
		abilities.add(new AbilityVar(36, 2, ftwo, 1, "e3ad"));
		abilities.add(new AbilityVar(36, 3, fone, .01, "e1hp"));
		// Tahm Kench
		abilities.add(new AbilityVar(223, 0, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(223, 1, aone, .02, "spelldamage"));
		abilities.add(new AbilityVar(223, 1, atwo, .6, "spelldamage"));
		// Pantheon
		abilities.add(new AbilityVar(80, 0, fone, 1.4, "bonusattackdamage"));
		abilities.add(new AbilityVar(80, 1, aone, 1, "spelldamage"));
		abilities.add(new AbilityVar(80, 2, aone, 3, "bonusattackdamage"));
		abilities.add(new AbilityVar(80, 2, fone, 3, "e1e4ad"));
		abilities.add(new AbilityVar(80, 3, aone, 1, "spelldamage"));
		// Maokai
		abilities.add(new AbilityVar(57, 0, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(57, 1, aone, .03, "spelldamage"));
		abilities.add(new AbilityVar(57, 2, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(57, 2, atwo, .6, "spelldamage"));
		abilities.add(new AbilityVar(57, 3, aone, .5, "spelldamage"));
		// Ivern
		abilities.add(new AbilityVar(427, 0, fone, .7, "spelldamage"));
		abilities.add(new AbilityVar(427, 1, ftwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(427, 2, fthree, .8, "spelldamage"));
		abilities.add(new AbilityVar(427, 2, ffour, .7, "spelldamage"));
		// Veigar
		abilities.add(new AbilityVar(45, 0, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(45, 1, aone, 1, "spelldamage"));
		abilities.add(new AbilityVar(45, 3, aone, .75, "spelldamage"));
		abilities.add(new AbilityVar(45, 3, atwo, 1.5, "spelldamage"));
		// Diana
		abilities.add(new AbilityVar(131, 0, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(131, 1, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(131, 1, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(131, 3, aone, .6, "spelldamage"));
		// Lissandra
		abilities.add(new AbilityVar(127, 0, aone, .65, "spelldamage"));
		abilities.add(new AbilityVar(127, 1, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(127, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(127, 3, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(127, 3, aone, .7, "spelldamage"));
		// Kog'Maw
		abilities.add(new AbilityVar(96, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(96, 1, fone, 1, "spfloor"));
		abilities.add(new AbilityVar(96, 2, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(96, 3, atwo, .65, "bonusattackdamage"));
		abilities.add(new AbilityVar(96, 3, aone, .25, "spelldamage"));
		abilities.add(new AbilityVar(96, 3, kogult, 1.5, "effect1"));
		abilities.add(new AbilityVar(96, 3, fthree, .975, "bonusattackdamage"));
		abilities.add(new AbilityVar(96, 3, ftwo, .375, "spelldamage"));
		abilities.add(new AbilityVar(96, 3, ffour, 2, "effect1"));
		abilities.add(new AbilityVar(96, 3, fsix, 1.3, "bonusattackdamage"));
		abilities.add(new AbilityVar(96, 3, ffive, .5, "spelldamage"));
		// Sona
		abilities.add(new AbilityVar(37, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(37, 0, atwo, .2, "spelldamage"));
		abilities.add(new AbilityVar(37, 1, aone, .25, "spelldamage"));
		abilities.add(new AbilityVar(37, 1, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(37, 2, ftwo, .06, "spelldamage"));
		abilities.add(new AbilityVar(37, 2, fone, .06, "baseE1ap"));
		abilities.add(new AbilityVar(37, 2, fthree, .06, "baseE1ap"));
		abilities.add(new AbilityVar(37, 3, aone, .5, "spelldamage"));
		// Mordekaiser
		abilities.add(new AbilityVar(82, 0, fone, 1, "e7ad"));
		abilities.add(new AbilityVar(82, 0, ftwo, .6, "spelldamage"));
		abilities.add(new AbilityVar(82, 0, ffive, 2, "effect3"));
		abilities.add(new AbilityVar(82, 0, fthree, 2, "e7ad"));
		abilities.add(new AbilityVar(82, 0, ffour, 1.2, "spelldamage"));
		abilities.add(new AbilityVar(82, 1, fthree, 0, "flat"));
		abilities.add(new AbilityVar(82, 1, aone, .9, "spelldamage"));
		abilities.add(new AbilityVar(82, 1, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(82, 2, aone, .3, "adap"));
		abilities.add(new AbilityVar(82, 3, aone, .04, "spelldamage"));
		abilities.add(new AbilityVar(82, 3, fone, 1, "bonusattackdamage"));
		abilities.add(new AbilityVar(82, 3, ftwo, .15, "health"));
		// Wukong
		abilities.add(new AbilityVar(62, 0, aone, .1, "attackdamage"));
		abilities.add(new AbilityVar(62, 1, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(62, 2, aone, .8, "bonusattackdamage"));
		abilities.add(new AbilityVar(62, 3, aone, 1.1, "attackdamage"));
		// Orianna
		abilities.add(new AbilityVar(61, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(61, 1, aone, .7, "spelldamage"));
		abilities.add(new AbilityVar(61, 2, aone, .4, "spelldamage"));
		abilities.add(new AbilityVar(61, 2, atwo, .3, "spelldamage"));
		abilities.add(new AbilityVar(61, 3, aone, .7, "spelldamage"));
		// Lucian
		abilities.add(new AbilityVar(236, 0, fone, .01, "e2bad"));
		abilities.add(new AbilityVar(236, 1, aone, .9, "spelldamage"));
		abilities.add(new AbilityVar(236, 3, aone, .1, "spelldamage"));
		abilities.add(new AbilityVar(236, 3, aone, .2, "attackdamage"));
		// Miss Fortune
		abilities.add(new AbilityVar(21, 0, fone, .85, "attackdamage"));
		abilities.add(new AbilityVar(21, 0, aone, .35, "spelldamage"));
		abilities.add(new AbilityVar(21, 0, ftwo, 1, "attackdamage"));
		abilities.add(new AbilityVar(21, 0, atwo, .5, "spelldamage"));
		abilities.add(new AbilityVar(21, 1, ftwo, 2, "cdr"));
		abilities.add(new AbilityVar(21, 2, aone, .8, "spelldamage"));
		abilities.add(new AbilityVar(21, 3, fone, .35, "bonusattackdamage"));
		abilities.add(new AbilityVar(21, 3, aone, .2, "spelldamage"));
		abilities.add(new AbilityVar(21, 3, fthree, 120, "flat"));
		abilities.add(new AbilityVar(21, 3, ftwo, .35, .2, "e2badap"));
		// Jhin
		double [] lotus = {28, 27, 26, 25, 24};
		abilities.add(new AbilityVar(202, 0, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(202, 0, fone, 1, "e3ad"));
		abilities.add(new AbilityVar(202, 1, aone, .5, "attackdamage"));
		abilities.add(new AbilityVar(202, 2, aone, 1.2, "attackdamage"));
		abilities.add(new AbilityVar(202, 2, atwo, 1, "spelldamage"));
		abilities.add(new AbilityVar(202, 2, fone, lotus, "flat"));
		abilities.add(new AbilityVar(202, 3, aone, .2, "attackdamage"));
		abilities.add(new AbilityVar(202, 3, fone, 1, "effect2"));
		abilities.add(new AbilityVar(202, 3, ftwo, 3.5, "effect1"));
		abilities.add(new AbilityVar(202, 3, fthree, .7, "attackdamage"));
		// Azir
		abilities.add(new AbilityVar(268, 0, aone, .5, "spelldamage"));
		abilities.add(new AbilityVar(268, 1, aone, .6, "spelldamage"));
		
		
		
	}
}
