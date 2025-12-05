class Solution {
    public int romanToInt(String s) {
       int len=s.length();
        char[] arr={'I','V','X','L','C','D','M'};
        int[] val={1,5,10,50,100,500,1000};
        int temp=0;
        int prevvalue=0;
        // example str=mcmxciv;

        for (int i=len-1;i>=0;i--){
            for(int j=0;j<arr.length;j++) {
                if (arr[j] == s.charAt(i)) {
                    int curvalue=val[j];
                    if (curvalue<prevvalue) {
                        temp -=curvalue;
                        prevvalue = curvalue;
                    } else {
                        temp += curvalue;
                                prevvalue=curvalue;
                    }
                    break;
                }
            }
        }//loop for input
    return temp;
        
    }
}
