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
			}
		}
		for (int i = 0; i < iBuild.length; i++){
			if (iBuild[i] > 0){
				boolean notFound = true;
				while (notFound){
					
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
