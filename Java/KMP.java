import java.util.ArrayList;


public class Main {
	static void constructLps(String pattern , int[]lps){
		int len = 0;
		
		lps[0] = 0;
		int i = 1;
		while(i < pattern.length()){
			// if there is a match
			if(pattern.charAt(i) == pattern.charAt(len)){
				len++;
				lps[i] = len;
				i++;
				}
			// if there is a mismatch
			else{
				if(len !=0){
					len = lps[len -1];
				}
				else{
					lps[i] = 0;
					i++;
					}
				}
			}
		}
		
		static ArrayList<Integer> search (String pattern , String txt){
			int n = txt.length();
			int m = pattern.length();
			
			int[] lps = new int[m];
			ArrayList<Integer> res = new ArrayList<>();
			
			constructLps(pattern , lps);
			int i = 0;
			int j = 0;
			
			while (i < n){
				if(txt.charAt(i) == pattern.charAt(j)){
					i++;
					j++;
					
					if(j == m){
						res.add(i - j);
						
						j = lps[j - 1];
						}
					}else{
						if (j != 0){
							j = lps[j - 1];
							}
						else{
							i++;
							}
						}
					
				}
				return res;
			}
		
		
	public static void main(String[] args) {
		String txt = "aabaacaadaabaaba"; 
        String pat = "aaba"; 

        ArrayList<Integer> res = search(pat, txt);
        for (int i = 0; i < res.size(); i++) 
            System.out.print(res.get(i) + " ");
	}
}
