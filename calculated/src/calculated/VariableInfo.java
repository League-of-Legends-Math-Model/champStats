package calculated;

import java.util.*;

public class VariableInfo {
	
	String fone;
	String ftwo;
	String aone;
	String atwo;
	ArrayList<AbilityVar> abilities;
	
	public VariableInfo () {
		fone = "{{ f1 }}";
		ftwo = "{{ f2 }}";
		aone = "{{ a1 }}";
		atwo = "{{ a2 }}";
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
		abilities.add(new AbilityVar(14, 0, fone, .6, "attackdamage"));
	}
}
