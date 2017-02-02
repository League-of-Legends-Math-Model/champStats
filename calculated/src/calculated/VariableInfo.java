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
		abilities.add(new AbilityVar(117, 0, fsix, .5, "e1sd"));
		abilities.add(new AbilityVar(117, 2, aone, .6, "spelldamage"));
		abilities.add(new AbilityVar(117, 2, atwo, .4, "spelldamage"));
		abiliites.add(new AbilityVar(117, 3, aone, .5, "spelldamage"));
		
		
	}
}
