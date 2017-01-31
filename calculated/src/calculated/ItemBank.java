package calculated;

import org.json.*;

import java.util.*;

public class ItemBank {
	JSONObject items;
	ArrayList<Item> itemBank;
	
	private void decodeItems() throws JSONException {
		JSONObject data = items.getJSONObject("data");
		Iterator<String> jkey = data.keys();
		while (jkey.hasNext()){
			String holder = (String)jkey.next();
			itemBank.add(new Item(data.getJSONObject(holder)));
		}
	}
	
	public double[][] itemBuild (int[] iBuild){
		double[][] statMods = new double[2][9];
		for (int i = 0; i < 2; i++){
			for (int j = 0; j < 9; j++){
				if (i == 0){
					statMods[i][j] = 0;
				}
				else {
					statMods[i][j] = 1;
				}
				statMods[1][6] = 0;
				statMods[1][7] = 0;
			}
		}
		for (int i = 0; i < iBuild.length; i++){
			if (iBuild[i] > 0){
				boolean notFound = true;
				int j = 0;
				while (notFound){
					if (iBuild[i] == itemBank.get(j).getId()){
						if (!itemBank.get(j).viktor()){
							for (int k = 0; k < 9; k++){
								statMods[0][k] += itemBank.get(j).getFlat()[k];
								if (k < 6){
									statMods[1][k] = statMods[1][k] * (1 + itemBank.get(j).getPer()[k]);
								}
							}
						}
					}
					else {
						statMods[1][6] = itemBank.get(j).viktorPerLevel[0];
						statMods[1][7] = itemBank.get(j).viktorPerLevel[1];
					}
				
					j++;
				}
			}
		}
		return statMods;
	}
	
	public ItemBank(JSONObject g) throws JSONException {
		items = g;
		itemBank = new ArrayList<Item>();
		decodeItems();
	}
}
