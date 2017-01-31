package calculated;


public class VariableInfo {
	
	String fone;
	String ftwo;
	String aone;
	String atwo;
	
	public VariableInfo () {
		fone = "{{ f1 }}";
		ftwo = "{{ f2 }}";
		aone = "{{ a1 }}";
		atwo = "{{ a2 }}";
	}
	
	public double translate(summoner s, String k, int slot){
		double value = 0;
		switch(s.champId){
		case 14:
			value = sion(s, k, slot);
			break;
		case 136:
			value = aurelion(s, k, slot);
			break;
		default:
		}
		return value;
	}
	
	private double aurelion(summoner su, String ks, int sl){
		double val = 0;
		switch(sl){
		case 0:
			val = 0.65 * su.abilitypower;
			break;
		case 1:
			
		default:
		}
		return val;
	}
	private double sion(summoner su, String ks, int sl){
		double val = 0;
		switch(sl){
		case 0:
			if (ks == fone){
				val = .6 * su.attackdamage;
			}
			if (ks == ftwo){
				val = 1.8 * su.attackdamage;
			}
			break;
		case 1:
			if (ks == fone){
				val = .1 * su.hp;
			}
			if (ks == aone){
				val = .4 * su.abilitypower;
			}
			break;
		case 2:
			val = .4 * su.abilitypower;
			break;
		case 3:
			if (ks == fone){
				val = .4 * (su.attackdamage - su.baseScaledArray[2]);
			}
			if (ks == ftwo){
				val = .8 * (su.attackdamage - su.baseScaledArray[2]);
			}
			break;
		default:
		}
		return val;
	}
}
